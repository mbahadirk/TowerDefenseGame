import pygame

class Score:
    def __init__(self, screen):
        self.x = 600
        self.y = 0
        self.score = 0
        self.screen = screen
        self.coinSize = [40, 40]
        self.score_image = pygame.image.load("images/coin.png")
        self.score_image = pygame.transform.scale(self.score_image, self.coinSize)
        self.font = pygame.font.Font(None, 36)

        # jump Score
        self.jump_height = 5
        self.jump_h = 5
        self.isJump = False
        self.isJumping = False

    def drawScore(self):
        self.screen.blit(self.score_image, (self.x,self.y))
        text = self.font.render(f"{self.score}", True, (255, 255, 255))
        self.screen.blit(text,(self.x+self.coinSize[0], self.y+10))

        # to jump score
        if self.isJumping:
            self.jumpScore()
        if not self.isJump:
            self.isJumping = False

    def jumpScore(self):
        self.isJump = True
        if self.jump_height >= -self.jump_h:
            self.y -= self.jump_height
            self.jump_height -= 1
        else:
            self.isJump = False
            self.jump_height = self.jump_h
