import pygame

class Gunman:
    def __init__(self):
        self.health = 100
        self.posX = 0
        self.posY = 200
        self.isShooting = False


    def drawGunman(self,screen,rotationAngle):
        if self.isShooting:
            self.gunman_image = pygame.image.load('images/gunmanShooting.png')
        else:
            self.gunman_image = pygame.image.load('images/gunman.png')

        self.gunman_image = pygame.transform.scale(self.gunman_image, (130,70))  # transform your img
        rotatedGunman = pygame.transform.rotate(self.gunman_image, rotationAngle)


        screen.blit(rotatedGunman, (self.posX, self.posY))
        pygame.draw.rect(screen, color=(203, 23, 96),
                         rect=(self.posX + 40, self.posY - 5, self.health, 5))
        self.isShooting = False

class PotatoMan(Gunman):
    def __init__(self):
        super().__init__()
        self.potato_image = pygame.image.load('images/potatoguy.png')
        self.potato_image = pygame.transform.scale(self.potato_image,(130, 100))
        self.gun_image = pygame.image.load('images/pistol.png')
        self.gun_image = pygame.transform.scale(self.gun_image,(60,30))


    def drawPotatoMan(self,screen, rotationAngle):
        screen.blit(self.potato_image,(self.posX,self.posY))
        rotatedPistol = pygame.transform.rotate(self.gun_image, rotationAngle)
        screen.blit(rotatedPistol,(self.posX+60,self.posY+40))
