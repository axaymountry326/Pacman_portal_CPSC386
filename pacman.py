# Aaron Xaymountry
# CPSC 386-01
# MW 5:30-6:45pm
# Pacman game with portals

import pygame


class Pacman():
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings
        self.height = 35
        self.width = 35
        self.image = [pygame.image.load('images/pacman1.png'), pygame.image.load('images/pacman2.png'),
                      pygame.image.load('images/pacman3.png')]
        self.image[0] = pygame.transform.scale(self.image[0], (self.height, self.width))
        self.image[1] = pygame.transform.scale(self.image[1], (self.height, self.width))
        self.image[2] = pygame.transform.scale(self.image[2], (self.height, self.width))
        self.rect = self.image[0].get_rect()
        #self.rect.x, self.rect.y = 310, 515
        self.rect.left -= self.rect.width
        self.rect.top -= self.rect.height

        self.x, self.y = 300, 500
        self.rect.x, self.rect.y = self.x, self.y
        # For updating pacman and to rotate depending on direction
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False
        self.orientation = "Right"

    # Updates pacman direction and sprite depending on direction
    def update(self):
        if self.moving_right:
            self.x += self.settings.pacmanspeed
        if self.moving_left:
            self.x -= self.settings.pacmanspeed
        if self.moving_up:
            self.y -= self.settings.pacmanspeed
        if self.moving_down:
            self.y += self.settings.pacmanspeed

        self.rect.x, self.rect.y = self.x, self.y
        # if self.moving_left == True:
        #     if self.orientation == "Right":
        #         self.image[1] = pygame.transform.flip(self.image[1], True, False)
        #     elif self.orientation == "Down":
        #         self.image[1] = pygame.transform.rotate(self.image[1], -90)
        #     elif self.orientation == "Up":
        #         self.image[1] = pygame.transform.rotate(self.image[1], 90)
        #     self.orientation = "Left"
        #     self.rect.x -= 1
        #
        # elif self.moving_right == True:
        #     if self.orientation == "Left":
        #         self.image[1] = pygame.transform.flip(self.image[1], True, False)
        #     elif self.orientation == "Down":
        #         self.image[1] = pygame.transform.rotate(self.image[1], 90)
        #     elif self.orientation == "Up":
        #         self.image[1] = pygame.transform.rotate(self.image[1], -90)
        #     self.orientation = "Right"
        #     self.rect.x += 1
        #
        # elif self.moving_up == True:
        #     if self.orientation == "Down":
        #         self.image[1] = pygame.transform.flip(self.image[1], False, True)
        #     elif self.orientation == "Left":
        #         self.image[1] = pygame.transform.rotate(self.image[1], -90)
        #     elif self.orientation == "Right":
        #         self.image[1] = pygame.transform.rotate(self.image[1], 90)
        #     self.orientation = "Up"
        #     self.rect.y -= 1
        #
        # elif self.moving_down == True:
        #     if self.orientation == "Up":
        #         self.image[1] = pygame.transform.flip(self.image[1], False, True)
        #     elif self.orientation == "Left":
        #         self.image[1] = pygame.transform.rotate(self.image[1], 90)
        #     elif self.orientation == "Right":
        #         self.image[1] = pygame.transform.rotate(self.image[1], -90)
        #     self.orientation = "Down"
        #     self.rect.y += 1

    def blitpacman(self):
        if pygame.time.get_ticks() % 200 <= 50:
            self.screen.blit(self.image[0], self.rect)
        elif pygame.time.get_ticks() % 200 <= 100:
            self.screen.blit(self.image[1], self.rect)
        elif pygame.time.get_ticks() % 200 <= 150:
            self.screen.blit(self.image[2], self.rect)
        else:
            self.screen.blit(self.image[2], self.rect)

