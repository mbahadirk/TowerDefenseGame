import pygame
import math

class Bullet:
    def __init__(self, x, y, target_x, target_y, screen, rotationAngle, bulletType):
        self.bulletType = bulletType

        # check bullettype and arange things
        if bulletType == "bullet":
            self.bulletSize = [20, 10]
        elif bulletType == "fireball":
            self.bulletSize = [50, 30]

        self.image = pygame.image.load(f'images/{bulletType}.png')
        self.image = pygame.transform.scale(self.image, self.bulletSize)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.target_x = target_x  # x position of mouseclick
        self.target_y = target_y  # y position of mouseclick
        self.speed = 15
        self.attack_damage = 5
        self.screen = screen
        self.rotationAngle = rotationAngle

    def update(self, enemies, bullets):
        dx = self.target_x - self.rect.centerx
        dy = self.target_y - self.rect.centery
        distance = math.sqrt(dx ** 2 + dy ** 2)

        rotatedBullet = pygame.transform.rotate(self.image, self.rotationAngle)
        self.screen.blit(rotatedBullet, self.rect)

        # bullet goes in direction
        if distance >= 10:
            direction_x = dx / distance
            direction_y = dy / distance
            self.rect.x += direction_x * self.speed
            self.rect.y += direction_y * self.speed

        else:
            bullets.remove(self)    # remove stopped bullets

        for enemy in enemies:
            if self.rect.colliderect(enemy.rect):
                enemy.isHitted = True
                enemy.takeDamage(self.attack_damage)
                if self in bullets:         # if bullet exists
                    bullets.remove(self)  # remove the bullet
                    break
