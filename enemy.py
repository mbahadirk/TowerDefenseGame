import time
import pygame
import random


class Enemy:
    def __init__(self, tower1, tower2, tower3):
        road1 = 120
        road2 = road1 + 150
        road3 = road2 + 150

        self.isJump = False
        self.isAlive = True

        self.posX = random.randrange(1150, 1300)
        self.posY = random.choice([road1, road2, road3])
        self.width = 70
        self.height = 60
        self.rect = None

        # load images
        self.zombie_image = pygame.image.load('images/zombie.png')
        self.zombie_image = pygame.transform.scale(self.zombie_image, (self.width, self.height))
        self.zombie_shooted_image = pygame.image.load('images/zombieShooted.png')
        self.zombie_shooted_image = pygame.transform.scale(self.zombie_shooted_image, (self.width, self.height))

        self.health = 20
        self.speed = 2
        self.attack_damage = 0.1

        if self.posY == road1:
            self.tower = tower1
        elif self.posY == road2:
            self.tower = tower2
        elif self.posY == road3:
            self.tower = tower3

        self.range = 120
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


    def is_tower_in_range(self):
        distance = abs(self.posX - self.tower.posX)
        return distance <= self.range

    def enemyMove(self):
        if self.is_tower_in_range():
            self.attack()
        else:
            self.isJump = False
            self.posX -= self.speed

    def attack(self):
        self.tower.health -= self.attack_damage

    def drawEnemy(self, screen):
        self.rect = pygame.Rect(self.posX, self.posY, self.width, self.height)
        # pygame.draw.rect(screen,color = (0,255,0),rect=self.rect)
        if self.isHitted:
            image = self.zombie_shooted_image
        else:
            image = self.zombie_image
        screen.blit(image, (self.posX, self.posY))
        pygame.draw.rect(screen, color=(203, 23, 96),
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