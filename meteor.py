import pygame
WIDTH = 1024

class Meteor:
    def __init__(self, x, y, speed):
        self.image = pygame.image.load("assets/meteoro.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed

    def update(self):
        self.rect.x -= self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)
