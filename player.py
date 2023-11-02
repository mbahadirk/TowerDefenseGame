import pygame


class Player:
    def __init__(self, screen, playerName, gunName):
        self.screen = screen
        self.health = 100
        self.posX = 0
        self.posY = 200
        self.isShooting = False
        self.playerName = playerName
        self.gunName = gunName
        self.playerSize = [100, 100]
        self.gunSize = [60, 40]
        self.player_image = pygame.image.load(f'images/{self.playerName}.png')
        self.player_image = pygame.transform.scale(self.player_image, self.playerSize)  # transform player png
        self.gun_image = pygame.image.load(f"images/{self.gunName}.png")
        self.gun_image = pygame.transform.scale(self.gun_image, self.gunSize)  # transform player png

    def drawPlayer(self, rotationAngle):
        self.screen.blit(self.player_image, (self.posX, self.posY))  # draw the character
        pygame.draw.rect(self.screen, (203, 23, 96),
                         rect=(self.posX + self.playerSize[0] - self.health, self.posY - 5, self.health, 5))
        rotatedGun = pygame.transform.rotate(self.gun_image, rotationAngle)
        self.screen.blit(rotatedGun,
                         (self.posX + self.playerSize[0] / 2 + self.gunSize[0], self.posY + self.gunSize[1]))
        self.isShooting = False
