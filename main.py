import pygame
import random
import math
from tower import *
from enemy import *
from gunman import *

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
grassBackground = pygame.transform.scale(grassBackground,(1200,600))
skyBackground = pygame.image.load('images/sky.png')
skyBackground = pygame.transform.scale(skyBackground,(1200,200))

# towers
tower1 = Tower(0,0)
tower2 = Tower(100,150)
tower3 = Tower(0,300)

# enemies
enemies = []
bigZombies = []
# bigZombie = BigZombie(tower1, tower2, tower3)

# gunman
gunman = Gunman()
rotationAngle = 0
potatoMan = PotatoMan()

# create enemies
for i in range(10):
    enemy = Enemy(tower1, tower2, tower3)
    enemies.append(enemy)

# create bigZombies
for i in range(2):
    bigZombie = BigZombie(tower1, tower2, tower3)
    bigZombies.append(bigZombie)

# game variables
running = True
clock = pygame.time.Clock()
current_image = 0
mouseColor = (189, 197, 39)
jumping = False


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                clickPosition = event.pos        # take the position of mouse click
                gunman.isShooting = True

                # to detect hits for bigzombie
                distance = pygame.math.Vector2(bigZombie.posX + 80 - clickPosition[0],
                                               bigZombie.posY + 70 - clickPosition[1]).length()
                if distance < bigZombie.radius:
                    bigZombie.isHitted = True

                # to detect hits for enemies
                for enemy in enemies:
                    distance = pygame.math.Vector2(enemy.posX + 50 - clickPosition[0],enemy.posY - clickPosition[1]).length()
                    if distance < enemy.radius:
                        enemy.isHitted = True
                        break
    keys = pygame.key.get_pressed()

    mousePosition = pygame.mouse.get_pos()

    rotationAngle = math.atan2(-(mousePosition[1] - gunman.posY), mousePosition[0] - gunman.posX)

    # dt = saat.tick(60) / 1000.0

    # Draw the game elements on the screen
    screen.fill((50, 220, 50)) # grass background
    screen.blit(skyBackground,(0,0))
    screen.blit(grassBackground,(0,110))

    pygame.draw.rect(screen,color=(135,62,35),rect=(0,120,window_width,70)) # road 1 (top)
    pygame.draw.rect(screen,color=(135,62,35),rect=(0,270,window_width,70)) # road 2 (mid)
    pygame.draw.rect(screen,color=(135,62,35),rect=(0,420,window_width,70)) # road 3 (bottom)

    # set towers out of screen when they run out of health
    if tower1.health >= 0:
        tower1.drawTower(screen)
    else: tower1.posX = -300
    if tower2.health >= 0:
        tower2.drawTower(screen)
    else:
        tower2.posX = -300
    if tower3.health >= 0:
        tower3.drawTower(screen)
    else:
        tower3.posX = -300

    # kill the enemies who  out of health
    enemies = [enemy for enemy in enemies if enemy.isAlive]
    bigZombies = [bigZombie for bigZombie in bigZombies if bigZombie.isAlive]
    # draw the enemies
    for enemy in enemies:
        enemy.drawEnemy(screen)
        enemy.takeDamage()

    bigZombie.drawEnemy(screen)
    bigZombie.takeDamage()

    # draw the gunman
    # gunman.drawGunman(screen=screen,rotationAngle=rotationAngle*50)
    potatoMan.drawPotatoMan(screen = screen, rotationAngle= rotationAngle*50)


    pygame.draw.circle(screen, mouseColor, mousePosition, 10)
    if 'clickPosition' in locals():
        pygame.draw.circle(screen, (236, 133, 21), clickPosition, 5)

        del clickPosition

    pygame.display.update()
    clock.tick(60)

pygame.quit()
