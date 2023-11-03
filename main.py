import pygame
import random
import math
from tower import *
from enemy import *
from player import *
from bullet import *
from buttons import *
from score import *

# Initialize pygame
pygame.init()

# Window settings
window_width = 1200
window_height = 600
window = (window_width, window_height)
screen = pygame.display.set_mode(window)
pygame.display.set_caption("Tower Defense")
game_font = pygame.font.Font(None, 50)  # Font for game over text
grassBackground = pygame.image.load('images/grassBackground.jpg')
grassBackground = pygame.transform.scale(grassBackground, (1200, 600))
skyBackground = pygame.image.load('images/sky.png')
skyBackground = pygame.transform.scale(skyBackground, (1200, 200))
stoneBackground = pygame.image.load('images/stone.png')
stoneBackground = pygame.transform.scale(stoneBackground, (1250, 70))

# score
score = Score(screen)

# towers
tower1 = Tower(0, 0)
tower2 = Tower(100, 150)
tower3 = Tower(0, 300)

# enemies
enemies = []
bigZombies = []
towerList = [tower1, tower2, tower3]


# player
playerName = "cartoonboy"
gunName = "pistol"

player = Player(screen, playerName, gunName)
rotationAngle = None


# create enemies
def createEnemies():
    for i in range(10):
        enemy = Enemy(tower1, tower2, tower3,"zombie", score, screen)
        enemies.append(enemy)

# button held actions
def buttonHeldAction():
    if player.gunName == "ak47":
        bullet = Bullet(player.posX + 100, player.posY + 35,
                        mousePosition[0], mousePosition[1], screen, rotationAngle, "bullet")
        bullets.append(bullet)
        player.hopBack()


# bullet list
bullets = []

# buttons
button1 = Button(350, 550, screen, 50, imageName="pistol")
button2 = Button(450, 550, screen, 50,text="ak47", imageName="ak47")
button3 = Button(550, 550, screen, 50, imageName="gunman")
button4 = Button(650, 550, screen, 50, imageName="cartoonboy")

# game variables
running = True
clock = pygame.time.Clock()
current_image = 0
mouseColor = (190, 37, 59)
jumping = False
tick = 60
button_held = False
button_held_delay = 200     # weapon shooting speed ^-1

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:

                if button1.rect.collidepoint(event.pos):    # detects pressing button
                    gunName = "pistol"
                    player = Player(screen, playerName=playerName, gunName=gunName)
                if button2.rect.collidepoint(event.pos):  # detects pressing button
                    gunName = "ak47"
                    player = Player(screen, playerName=playerName, gunName=gunName)
                if button3.rect.collidepoint(event.pos):  # detects pressing button
                    playerName = "gunman"
                    player = Player(screen, playerName=playerName, gunName=gunName)
                if button4.rect.collidepoint(event.pos):  # detects pressing button
                    playerName = "cartoonboy"
                    player = Player(screen, playerName=playerName, gunName=gunName)


                clickPosition = event.pos  # take the position of mouse click
                player.isShooting = True
                player.isHop = True

                # create a new bullet when click
                bullet = Bullet(player.posX + 100, player.posY + 35,
                                clickPosition[0], clickPosition[1], screen, rotationAngle, "bullet")
                bullets.append(bullet)

                button_held = True      # bool for button is helding
                button_held_start_time = pygame.time.get_ticks()    # the time held has been started

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                button_held = False

    if button_held:
        current_time = pygame.time.get_ticks()
        if current_time - button_held_start_time >= button_held_delay:
            buttonHeldAction()
            button_held_start_time = pygame.time.get_ticks()



    keys = pygame.key.get_pressed()

    mousePosition = pygame.mouse.get_pos()

    rotationAngle = 50 * math.atan2(-(mousePosition[1] - player.posY), mousePosition[0] - player.posX)


    # Draw the game elements on the screen
    screen.fill((50, 220, 50))  # grass background
    screen.blit(skyBackground, (0, 0))
    screen.blit(grassBackground, (0, 110))

    screen.blit(stoneBackground, (0, 120))  # road 1 (top)
    screen.blit(stoneBackground, (0, 270))  # road 2 (mid)
    screen.blit(stoneBackground, (0, 420))  # road 3 (bottom)

    # set towers out of screen when they run out of health
    for tower in towerList:
        if tower.health >= 0:
            tower.drawTower(screen)
        else:
            tower.posX = -300

    towerList = [tower for tower in towerList if tower.health > 0]

    # kill the enemies who  out of health
    enemies = [enemy for enemy in enemies if enemy.isAlive]
    bigZombies = [bigZombie for bigZombie in bigZombies if bigZombie.isAlive]

    # draw the enemies
    for enemy in enemies:
        enemy.drawEnemy()
        enemy.takeDamage(0)

    # update and draw the bullets
    for bullet in bullets:
        bullet.update(enemies, bullets)


    # draw the player
    player.drawPlayer(rotationAngle=rotationAngle)
    player.hopBack()

    # recreate the enemies when all dead
    if not len(enemies):
        createEnemies()

    # draw buttons
    button1.drawButton()
    button2.drawButton()
    button3.drawButton()
    button4.drawButton()

    # draw the score
    score.drawScore()

    pygame.draw.circle(screen, mouseColor, mousePosition, 5)
    if 'clickPosition' in locals():
        pygame.draw.circle(screen, (236, 133, 21), clickPosition, 5)

        del clickPosition

    pygame.display.update()
    clock.tick(tick)

pygame.quit()
