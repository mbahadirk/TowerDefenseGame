import pygame
class Tower:
    def __init__(self, posX, posY):
        self.health = 100
        self.posX = posX
        self.posY = posY
        self.tower_image = pygame.image.load('images/tower.png')
        self.tower_image = pygame.transform.scale(self.tower_image, (200,200))  # transform your img


    def drawTower(self,screen):
        screen.blit(self.tower_image, (self.posX,self.posY))
        pygame.draw.rect(screen, color=(44, 246, 37), rect=(self.posX + 80, self.posY , self.health, 5))

