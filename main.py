import pygame
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
MAX_FPS_COUNT = 30
WINDOW_SIZES = (800, 600)

screen = pygame.display.set_mode(WINDOW_SIZES)

running = True
clock = pygame.time.Clock()

while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)

        pygame.display.flip()
        clock.tick(MAX_FPS_COUNT)

pygame.quit()