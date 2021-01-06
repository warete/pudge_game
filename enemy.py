import random
import os
import pygame


def get_random_enemy():
    rand_number = random.randint(0, 10)
    if 0 <= rand_number <= 5:
        return Pudge()
    if 6 <= rand_number <= 8:
        return Techie()
    if rand_number > 8:
        return Heal()


class Enemy:
    x = 0
    y = 0
    width = 0
    height = 0
    img_path = ''
    img = None

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        self.rect = pygame.Rect((0, 0), (self.width, self.height))
        self.is_clicked = False

    def get_rect(self):
        return self.rect

    def set_sizes(self, width, height):
        self.width = width
        self.height = height
        self.init_img()

    def init_img(self):
        if len(self.img_path) > 0:
            self.rect = pygame.Rect((self.x, self.y), (self.width, self.height))
            self.img = pygame.transform.scale(pygame.image.load(self.img_path), (self.width, self.height))

    def set_coords(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect((self.x, self.y), (self.width, self.height))

    def draw(self, screen):
        if self.img is not None:
            screen.blit(self.img, (self.x, self.y))

    def on_click(self, lifes, points):
        return lifes, points


class Pudge(Enemy):
    img_path = os.path.join('images', 'pudge.png')

    def on_click(self, lifes, points):
        if not self.is_clicked:
            self.is_clicked = True
            return lifes, points + 1
        else:
            return lifes, points


class Techie(Enemy):
    img_path = os.path.join('images', 'techies.png')

    def on_click(self, lifes, points):
        if not self.is_clicked:
            self.is_clicked = True
            return 0, points
        else:
            return lifes, points


class Heal(Enemy):
    img_path = os.path.join('images', 'heal.jpg')

    def on_click(self, lifes, points):
        if not self.is_clicked:
            self.is_clicked = True
            return lifes if lifes == 3 else lifes + 1, points
        else:
            return lifes, points
