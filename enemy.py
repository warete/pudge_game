import random

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

    def set_sizes(self, width, height):
        self.width = width
        self.height = height
        self.init_img()

    def init_img(self):
        if len(self.img_path) > 0:
            self.img = pygame.transform.scale(pygame.image.load(self.img_path), (self.width, self.height))

    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen):
        if self.img is not None:
            screen.blit(self.img, (self.x, self.y))


class Pudge(Enemy):
    img_path = 'images/pudge.png'


class Techie(Enemy):
    img_path = 'images/techies.png'


class Heal(Enemy):
    img_path = 'images/heal.jpg'
