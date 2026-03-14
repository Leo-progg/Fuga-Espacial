import pygame

WIDTH = 1024
HEIGHT = 768

class Background:
    def __init__(self):
        self.layers = [
            pygame.transform.scale(pygame.image.load("assets/bg/bg1.png").convert(), (WIDTH, HEIGHT)),
            pygame.transform.scale(pygame.image.load("assets/bg/bg2.png").convert_alpha(), (WIDTH, HEIGHT)),
            pygame.transform.scale(pygame.image.load("assets/bg/bg3.png").convert_alpha(), (WIDTH, HEIGHT)),
            pygame.transform.scale(pygame.image.load("assets/bg/bg4.png").convert_alpha(), (WIDTH, HEIGHT)),
            pygame.transform.scale(pygame.image.load("assets/bg/bg5.png").convert_alpha(), (WIDTH, HEIGHT)),
        ]

        self.speeds = [0.2, 0.5, 1, 2, 3]

        self.positions = [0, 0, 0, 0, 0]

    def draw(self, screen):
        for i, layer in enumerate(self.layers):
            self.positions[i] -= self.speeds[i]

            if self.positions[i] <= -WIDTH:
                self.positions[i] = 0

            screen.blit(layer, (self.positions[i], 0))
            screen.blit(layer, (self.positions[i] + WIDTH, 0))