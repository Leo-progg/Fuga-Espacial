import pygame

WIDTH = 1024
HEIGHT = 768

class Player:
    def __init__(self, x, y):
        self.image = pygame.image.load("assets/nave.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 7

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed

        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed

        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed

        if keys[pygame.K_DOWN] and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)