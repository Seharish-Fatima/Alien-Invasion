import pygame

class Bt21:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        original_image = pygame.image.load('assets/bt21.bmp')
        self.image = pygame.transform.scale(original_image, (250, 250))
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.bottomleft
        self.rect.x += 80
        self.rect.y += 20

    def blitme(self):
        self.screen.blit(self.image, self.rect)