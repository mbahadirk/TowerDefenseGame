import pygame

class Bullet:
    def __init__(self, startX, startY, targetX, targetY, type):
        self.startX = startX
        self.startY = startY
        self.targetX = targetX
        self.targetY = targetY
        self.type = type
        if self.type == 'bullet':
            self.image = pygame.image.load('images/bullet.png')
            self.image = pygame.transform.scale(self.image,(20,20))
        self.posX = None
        self.posY = None

    def drawBullet(self,screen):
        screen.blit(image, (self.posX, self.posY))

    def moveBullet(self,dt):


