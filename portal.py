# Aaron Xaymountry
# CPSC 386-01
# MW 5:30-6:45pm
# Pacman game with portals

import pygame
from pygame.sprite import Sprite


class Portal(Sprite):
    def __init__(self, screen):
        super(Portal, self).__init__()
        self.screen = screen
        self.height = 30
        self.width = 30
        img = pygame.image.load('images/portal.png')
        img = pygame.transform.scale(img, (self.height, self.width))
        self.rect = img.get_rect()
        self.image = img

    def blitportal(self):
        self.screen.blit(self.image, self.rect)

