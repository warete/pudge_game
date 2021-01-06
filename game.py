import pygame
import utils
import os
from enemy import get_random_enemy


class Game:
    bg_color = (0, 0, 0)
    max_fps = 30
    window_sizes = (600, 800)
    field_cells_count = 5
    need_reload_field_event = {
        'code': pygame.USEREVENT + 1,
        'time': 1000
    }
    field = []
    enemy = None
    isRunning = True

    lifes = 3
    points = 0
    isGameStarted = False

    def __init__(self, max_fps=30, window_sizes=(600, 700), field_cells_count=5):
        self.max_fps = max_fps
        self.window_sizes = window_sizes
        self.field_cells_count = field_cells_count

        self.field_cell_size = int(min(self.window_sizes) / self.field_cells_count)

        pygame.init()
        pygame.font.init()
        pygame.display.set_caption('PudgeGame')
        pygame.time.set_timer(self.need_reload_field_event['code'], self.need_reload_field_event['time'])
        self.screen = pygame.display.set_mode(self.window_sizes)
        self.clock = pygame.time.Clock()

        self.optimus_font_big = pygame.font.Font(os.path.join('fonts', 'OptimusPrinceps.ttf'), 120)
        self.optimus_font = pygame.font.Font(os.path.join('fonts', 'OptimusPrinceps.ttf'), 35)

        self.retry_btn = self.optimus_font.render('Retry?', False, (173, 0, 0))

        self.start_game()

    def start_game(self):
        self.isGameStarted = True
        self.lifes = 3
        self.points = 0
        self.reload_enemy_and_field()

    def reload_enemy_and_field(self):
        self.field = utils.get_new_field(self.field_cells_count)
        enemy_x, enemy_y = utils.get_coords_by_field(self.field, self.field_cell_size)
        self.enemy = get_random_enemy()
        self.enemy.set_sizes(self.field_cell_size, self.field_cell_size)
        self.enemy.set_coords(enemy_x, enemy_y)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.isRunning = False
            if event.type == self.need_reload_field_event['code']:
                self.reload_enemy_and_field()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = event.pos
                if self.isGameStarted:
                    if self.enemy.get_rect().collidepoint(pos[0], pos[1]):
                        self.lifes, self.points = self.enemy.on_click(self.lifes, self.points)
                    else:
                        self.lifes -= 1
                else:
                    self.start_game()

    def check_game_over(self):
        if self.lifes == 0:
            self.isGameStarted = False

            points_text = self.optimus_font.render('Pudges banned: ' + str(self.points), False, (173, 0, 0))
            self.screen.blit(points_text, points_text.get_rect(center=(self.window_sizes[0] / 2, 35)))

            self.screen.blit(self.retry_btn,
                             self.retry_btn.get_rect(center=(self.window_sizes[0] / 2, self.window_sizes[1] * 0.75)))

            gameover_text = self.optimus_font_big.render('You died', False, (173, 0, 0))
            self.screen.blit(gameover_text,
                             gameover_text.get_rect(center=(self.window_sizes[0] / 2, self.window_sizes[1] / 2)))

    def run(self):
        pixel_font = pygame.font.Font(os.path.join('fonts', 'pixel.ttf'), 35)

        life = pygame.image.load(os.path.join('images', 'lives.png'))
        life_x_start = self.window_sizes[0] / 2 - (life.get_width() + 5) * 3
        while self.isRunning:
            self.screen.fill(self.bg_color)

            self.handle_events()

            self.check_game_over()

            if self.isGameStarted:
                points_text = pixel_font.render('Pudges banned: ' + str(self.points), False, (255, 255, 255))
                self.screen.blit(points_text, points_text.get_rect(center=(self.window_sizes[0] / 2, 17)))

                for i in range(1, self.lifes + 1):
                    self.screen.blit(life, (life_x_start + ((life.get_width() + 5) * i), 70))

                self.enemy.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(self.max_fps)

        pygame.quit()
