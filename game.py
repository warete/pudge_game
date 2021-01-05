import pygame
import utils
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

    def __init__(self, max_fps=30, window_sizes=(600, 700), field_cells_count=5):
        self.max_fps = max_fps
        self.window_sizes = window_sizes
        self.field_cells_count = field_cells_count

        self.field_cell_size = int(min(self.window_sizes) / self.field_cells_count)

        pygame.init()
        pygame.time.set_timer(self.need_reload_field_event['code'], self.need_reload_field_event['time'])
        self.screen = pygame.display.set_mode(self.window_sizes)
        self.clock = pygame.time.Clock()
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

    def run(self):
        while self.isRunning:
            self.screen.fill(self.bg_color)

            self.handle_events()

            self.enemy.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(self.max_fps)

        pygame.quit()
