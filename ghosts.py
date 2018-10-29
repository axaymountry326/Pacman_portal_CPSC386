# Aaron Xaymountry
# CPSC 386-01
# MW 5:30-6:45pm
# Pacman game with portals

import pygame
from pygame.sprite import Group


class Ghosts():
    def __init__(self, screen, color):
        super(Ghosts, self).__init__()
        i = 0
        self.screen = screen
        self.height = 35
        self.width = 35

        if color == "red":
            img = pygame.image.load('images/red_ghost.bmp')
        elif color == "cyan":
            img = pygame.image.load('images/cyan_ghost.bmp')
            i = 36
        elif color == "orange":
            img = pygame.image.load('images/orange_ghost.bmp')
            i = 105
        elif color == "pink":
            img = pygame.image.load('images/pink_ghost.bmp')
            i = 72


        img = pygame.transform.scale(img, (self.height, self.width))
        self.rect = img.get_rect()
        self.rect.x, self.rect.y = 275 + i, 315
        self.rect.left -= self.rect.width
        self.rect.top -= self.rect.height
        self.image = img

        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

    def update(self):
        if self.moving_left == True:
            self.rect.x -= 1
        elif self.moving_right == True:
            self.rect.x += 1
        elif self.moving_up == True:
            self.rect.y -= 1
        elif self.moving_down == True:
            self.rect.y += 1

    def blitghosts(self):
        self.screen.blit(self.image, self.rect)
