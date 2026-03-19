import pygame
import random
from player import Player
from meteor import Meteor
from background import Background
from menu import Menu
from explosion import Explosion

WIDTH = 1024
HEIGHT = 768

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Fuga Espacial")
        self.clock = pygame.time.Clock()

        self.menu = Menu(self.screen)
        self.bg = Background()

        self.player = Player(WIDTH // 2, HEIGHT - 100)
        self.meteors = []
        self.explosions = []

        self.spawn_timer = 0
        self.score = 0
        self.lives = 3

        self.difficulty_timer = 0
        self.meteor_speed = 6
        self.spawn_delay = 40

    def spawn_meteor(self):
        y = random.randint(0, HEIGHT)
        self.meteors.append(Meteor(WIDTH + 60, y, self.meteor_speed))

    def check_collision(self):
        for meteor in self.meteors:
            if self.player.rect.colliderect(meteor.rect):
                self.explosions.append(Explosion(meteor.rect.centerx, meteor.rect.centery))
                self.meteors.remove(meteor)
                self.lives -= 1

    def run(self):
        self.menu.run()

        pygame.mixer.music.load("assets/somfundo.wav")
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)

        running = True
        while running:
            self.clock.tick(70)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # dificuldade progressiva
            self.difficulty_timer += 1
            if self.difficulty_timer > 500:
                self.meteor_speed += 1
                if self.spawn_delay > 15:
                    self.spawn_delay -= 3
                self.difficulty_timer = 0

            # spawn meteoros
            self.spawn_timer += 1
            if self.spawn_timer > self.spawn_delay:
                self.spawn_meteor()
                self.spawn_timer = 0

            self.player.update()

            for meteor in self.meteors:
                meteor.update()

            self.check_collision()

            self.score += 1

            # atualizar explosões
            for explosion in self.explosions:
                explosion.update()

            # remover explosões antigas
            self.explosions = [e for e in self.explosions if e.timer > 0]

            # desenhar
            self.bg.draw(self.screen)
            self.player.draw(self.screen)

            for meteor in self.meteors:
                meteor.draw(self.screen)

            for explosion in self.explosions:
                explosion.draw(self.screen)

            font = pygame.font.SysFont(None, 36)
            hud = font.render(f"Pontos: {self.score}   Vidas: {self.lives}", True, (255, 255, 255))
            self.screen.blit(hud, (20, 20))

            fps = int(self.clock.get_fps())
            fps_text = font.render(f"FPS: {fps}", True, (255, 255, 255))
            self.screen.blit(fps_text, (20, 50))

            pygame.display.flip()

            if self.lives <= 0:
                self.game_over()
                return self.run()

        pygame.quit()

    def game_over(self):
        font_big = pygame.font.SysFont(None, 100)
        font_small = pygame.font.SysFont(None, 50)

        waiting = True
        while waiting:
            self.screen.fill((0, 0, 0))

            text1 = font_big.render("GAME OVER", True, (255, 0, 0))
            text2 = font_small.render(f"Pontos: {self.score}", True, (255, 255, 255))
            text3 = font_small.render("ENTER - Reiniciar", True, (200, 200, 200))
            text4 = font_small.render("ESC - Sair", True, (200, 200, 200))

            rect1 = text1.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 120))
            rect2 = text2.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 20))
            rect3 = text3.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 60))
            rect4 = text4.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 120))

            self.screen.blit(text1, rect1)
            self.screen.blit(text2, rect2)
            self.screen.blit(text3, rect3)
            self.screen.blit(text4, rect4)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.restart()
                        waiting = False

                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()

    def restart(self):
        self.meteors.clear()
        self.explosions.clear()

        self.score = 0
        self.lives = 3

        self.spawn_timer = 0
        self.difficulty_timer = 0
        self.meteor_speed = 6
        self.spawn_delay = 40

        self.player.rect.center = (WIDTH // 2, HEIGHT - 100)