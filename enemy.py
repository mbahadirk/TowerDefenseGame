import time
import pygame
import random


class Enemy:
    def __init__(self, tower1, tower2, tower3, enemyType, score, screen, player):
        road1 = 200
        road2 = road1 + 150
        road3 = road2 + 150

        self.enemyValue = 10  # arange for another enemy types
        self.score = score

        self.screen = screen
        self.isJump = False
        self.isAlive = True
        self.player = player

        self.posX = random.randrange(1150, 1300)
        self.posY = random.choice([road1, road2, road3])
        self.width = 70
        self.height = 60
        self.rect = None
        self.enemyType = enemyType

        # load images
        self.enemy_image = pygame.image.load(f'images/{self.enemyType}.png')
        self.enemy_image = pygame.transform.scale(self.enemy_image, (self.width, self.height))
        try:
            self.enemy_shooted_image = pygame.image.load(f'images/{self.enemyType}Shooted.png')
            self.enemy_shooted_image = pygame.transform.scale(self.enemy_shooted_image, (self.width, self.height))
        except FileNotFoundError:
            print("shooted animation couldn't found")
            self.enemy_shooted_image = pygame.image.load('images/none.png')

        self.health = 15
        self.speed = 2
        self.attack_damage = 0.05

        if self.posY == road1:
            self.tower = tower1
        elif self.posY == road2:
            self.tower = tower2
        elif self.posY == road3:
            self.tower = tower3

        self.range = 0
        self.radius = 50

        self.jump_height = 5
        self.jump_h = 5

        self.isHitted = False

    def takeDamage(self, damage):
        if self.isHitted:
            self.jumpBack()
            self.health -= damage

        if not self.isJump:
            self.isHitted = False

        if self.health <= 0:
            self.isAlive = False
            self.score.score += self.enemyValue
            self.score.isJumping = True
            self.score.jumpScore()



    def is_tower_in_range(self, tower):
        distance = abs(self.posX - tower.posX)
        return distance <= self.range + tower.width

    def enemyMove(self):
        if self.is_tower_in_range(self.tower):
            self.attack(self.tower)
        else:
            self.posX -= self.speed
        if self.is_tower_in_range(self.player):
            self.attack(self.player)
        else:
            self.posX -= self.speed

    def attack(self, opponent):
        opponent.health -= self.attack_damage
        self.jumpBack()

    def drawEnemy(self):
        self.rect = pygame.Rect(self.posX, self.posY, self.width, self.height)
        # pygame.draw.rect(self.screen,color = (0,255,0),rect=self.rect)   # you can use it for check hitbox
        if self.isHitted:
            image = self.enemy_shooted_image
        else:
            image = self.enemy_image
        self.screen.blit(image, (self.posX, self.posY))
        pygame.draw.rect(self.screen, color=(203, 23, 96),
                         rect=(self.posX + 40, self.posY - 5, self.health, 5))  # road 1 (top)
        self.enemyMove()


    def jumpBack(self):
        self.isJump = True
        if self.jump_height >= -self.jump_h:
            self.posY -= self.jump_height
            self.jump_height -= 1
            self.posX -= -3
        else:
            self.isJump = False
            self.jump_height = self.jump_h