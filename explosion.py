import pygame

class Explosion:
    def __init__(self, x, y):
        self.image = pygame.image.load("assets/explosao.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect(center=(x, y))
        self.timer = 15

    def update(self):
        self.timer -= 1

    def draw(self, screen):
        screen.blit(self.image, self.rect)