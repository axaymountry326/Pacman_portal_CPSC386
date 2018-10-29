# Aaron Xaymountry
# CPSC 386-01
# axaymountry@csu.fullerton.edu
# MW 5:30-6:45pm
# Start screen for pacman game

import sys
import pygame
import pygame.font

from pygame.sprite import Group
from settings import Settings

# Globals for ease
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class StartScreen():
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings
        self.screen_rect = screen.get_rect()

        # Load in ghost images
        self.image = pygame.image.load('images/cyan_ghost.bmp')
        self.image2 = pygame.image.load('images/orange_ghost.bmp')
        self.image3 = pygame.image.load('images/pink_ghost.bmp')
        self.image4 = pygame.image.load('images/red_ghost.bmp')

        # Load in Pacman image
        self.height = 125
        self.width = 125
        img = pygame.image.load('images/Pacman.png')
        img = pygame.transform.scale(img, (self.height, self.width))
        self.rect = img.get_rect()
        self.rect.x, self.rect.y = 310, 515
        self.rect.left -= self.rect.width
        self.rect.top -= self.rect.height
        self.pacmanimage = img
        self.rect = self.pacmanimage.get_rect()

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        screen.fill(BLACK)

    def makeScreen(self, screen):
        pygame.init()
        pygame.display.set_caption("PACMAN")

        background = pygame.Surface(screen.get_size())
        background = background.convert()
        background.fill(BLACK)

        # Display P in front of the PACMAN pic
        font = pygame.font.Font(None, 144)
        text1 = font.render("PA", 2, WHITE)
        textpos1 = text1.get_rect()
        textpos1 = ((self.settings.screen_width / 2) - 300, (self.settings.screen_height / 8) - 75)
        font = pygame.font.Font(None, 144)

        # Display "CMAN" after the PACMAN pic
        text2 = font.render("CMAN", 2, WHITE)
        textpos2 = text2.get_rect()
        textpos2 = ((self.settings.screen_width / 2), (self.settings.screen_height / 8) - 75)

        # Ghosts position and text
        # Cyan Ghost
        font = pygame.font.Font(None, 44)
        text3 = font.render(" INKY", 2, (250, 250, 250))
        textpos3 = text3.get_rect()

        # Orange Ghost
        text4 = font.render(" CLYDE", 2, (250, 250, 250))
        textpos4 = text4.get_rect()

        # Pink Ghost
        text5 = font.render(" PINKY", 2, (250, 250, 250))
        textpos5 = text5.get_rect()

        # Pink Ghost
        text6 = font.render(" BLINKY", 2, (250, 250, 250))
        textpos6 = text5.get_rect()

        # Pink Ghost position
        textpos5 = ((self.settings.screen_width / 2) - 120, (self.settings.screen_height / 2) - 150)
        pinkghost = ((self.settings.screen_width / 2) + 5, (self.settings.screen_height / 2) - 100)

        # Cyan ghost position
        textpos3 = ((self.settings.screen_width / 2) - 10, (self.settings.screen_height / 2) - 150)
        cyanghost = ((self.settings.screen_width / 2) - 100, (self.settings.screen_height / 2) - 100)

        # Orange ghost position
        textpos4 = ((self.settings.screen_width / 2) + 85, (self.settings.screen_height / 2) - 150)
        orangeghost = ((self.settings.screen_width / 2) + 100, (self.settings.screen_height / 2) - 100)

        # Red Ghost position
        textpos6 = ((self.settings.screen_width / 2) - 250, (self.settings.screen_height / 2) - 150)
        redghost = ((self.settings.screen_width / 2) - 220, (self.settings.screen_height / 2) - 100)

        # PACMAN position
        pacman_pos = ((self.settings.screen_width / 2) - 150, (self.settings.screen_height / 8) - 55)

        # Draw onto screen
        background.blit(text1, textpos1)
        background.blit(self.pacmanimage, pacman_pos)
        background.blit(text2, textpos2)
        background.blit(self.image, pinkghost)
        background.blit(text3, textpos3)
        background.blit(self.image2, orangeghost)
        background.blit(text4, textpos4)
        background.blit(self.image3, cyanghost)
        background.blit(text5, textpos5)
        background.blit(self.image4, redghost)
        background.blit(text6, textpos6)

        # Blit everything to screen
        screen.blit(self.image, (self.settings.screen_width / 2, self.settings.screen_height / 3))
        screen.blit(background, (200, 200))

        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    return

            screen.blit(background, (0, 0))
            pygame.display.flip()