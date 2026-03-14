import pygame

WIDTH = 1024
HEIGHT = 768

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.bg = pygame.image.load("assets/fundo menu.png").convert()
        self.bg = pygame.transform.scale(self.bg, (WIDTH, HEIGHT))

    def run(self):
        pygame.mixer.music.load("assets/sommenu.wav")
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.play(-1)

        font_title = pygame.font.SysFont(None, 130)
        font_text = pygame.font.SysFont(None, 55)
        font_controls = pygame.font.SysFont(None, 40)

        waiting = True
        while waiting:
            self.screen.blit(self.bg, (0, 0))

            title = font_title.render("FUGA ESPACIAL", True, (255, 255, 255))
            start = font_text.render("ENTER - Jogar", True, (255, 255, 255))
            exit_text = font_text.render("ESC - Sair", True, (255, 255, 255))

            ctrl1 = font_controls.render("SETAS - Mover a nave", True, (255, 255, 255))
            ctrl2 = font_controls.render("OBJETIVO - Desvie dos meteoros", True, (255, 255, 255))

            title_rect = title.get_rect(center=(WIDTH // 2, 200))
            start_rect = start.get_rect(center=(WIDTH // 2, 430))
            exit_rect = exit_text.get_rect(center=(WIDTH // 2, 500))

            ctrl1_rect = ctrl1.get_rect(center=(WIDTH // 2, 600))
            ctrl2_rect = ctrl2.get_rect(center=(WIDTH // 2, 640))

            self.screen.blit(title, title_rect)
            self.screen.blit(start, start_rect)
            self.screen.blit(exit_text, exit_rect)
            self.screen.blit(ctrl1, ctrl1_rect)
            self.screen.blit(ctrl2, ctrl2_rect)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        waiting = False

                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()