import pygame
import utils
from enemy import get_random_enemy

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
MAX_FPS_COUNT = 30
WINDOW_SIZES = (600, 700)
CELLS_COUNT = 5
CELL_SIZE = int(min(WINDOW_SIZES) / CELLS_COUNT)

screen = pygame.display.set_mode(WINDOW_SIZES)
NEED_RELOAD_ENEMY_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(NEED_RELOAD_ENEMY_EVENT, 1000)

clock = pygame.time.Clock()

field = utils.get_new_field(CELLS_COUNT)
enemy_x, enemy_y = utils.get_coords_by_field(field, CELL_SIZE)
enemy = get_random_enemy()
enemy.set_sizes(CELL_SIZE, CELL_SIZE)
enemy.set_coords(enemy_x, enemy_y)

running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == NEED_RELOAD_ENEMY_EVENT:
            field = utils.get_new_field(CELLS_COUNT)
            enemy_x, enemy_y = utils.get_coords_by_field(field, CELL_SIZE)
            enemy = get_random_enemy()
            enemy.set_sizes(CELL_SIZE, CELL_SIZE)
            enemy.set_coords(enemy_x, enemy_y)

    enemy.draw(screen)
    pygame.display.flip()
    clock.tick(MAX_FPS_COUNT)

pygame.quit()
