import pygame

class Button:
    def __init__(self, x, y, screen, size, text=None, imageName=None, color=(250, 223, 169)):
        self.size = size
        self.text = text
        self.imageName = imageName
        self.color = color
        self.x = x
        self.y = y
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)
        self.active = False


    def drawButton(self):
        pygame.draw.rect(self.screen, self.color, (self.x-5,self.y-5,self.size+10,self.size+10))
        pygame.draw.rect(self.screen, (self.color[0]-50, self.color[1]-50, self.color[2]-50), self.rect)

        if self.imageName:
            buttonImage = pygame.image.load(f'images/{self.imageName}.png')
            buttonImage = pygame.transform.scale(buttonImage, (self.size-10,self.size-10))
            self.screen.blit(buttonImage, (self.x+5, self.y+5))
        if self.text:
            text = self.font.render(self.text, True, (0, 0, 0))
            textRect = text.get_rect(center=self.rect.center)
            self.screen.blit(text, textRect)
