# Aaron Xaymountry
# CPSC 386-01
# MW 5:30-6:45pm
# Pacman game with portals

import pygame
from pygame.sprite import Sprite


class Powerpills(Sprite):
    def __init__(self, screen):
        super(Powerpills, self).__init__()
        self.screen = screen
        self.height = 7
        self.width = 7
        img = pygame.image.load('images/powerpill.png')
        img = pygame.transform.scale(img, (self.height, self.width))
        self.rect = img.get_rect()
        self.image = img

    def blitpowerpills(self):
        self.screen.blit(self.image, self.rect)

