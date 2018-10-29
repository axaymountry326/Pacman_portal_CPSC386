# Aaron Xaymountry
# CPSC 386-01
# MW 5:30-6:45pm
# Pacman game with portals

import pygame
import game_functions as gf
from maze import Maze
from pacman import Pacman
from startscreen import StartScreen
from pygame.sprite import Group
from ghosts import Ghosts
from settings import Settings
from gameStats import GameStats


BLACK = (0, 0, 0)
WHITE = (250, 250, 250)


def __str__(self):
    return 'Game(Pacman Portal), maze=' + str(self.maze) + ')'


def Game():
    pygame.init()

    gamesettings = Settings()
    screen = pygame.display.set_mode((gamesettings.screen_width, gamesettings.screen_height))
    pygame.display.set_caption("Pacman Portal")

    # Start screen
    startScreen = StartScreen(screen, gamesettings)
    showgamestats = GameStats(screen, gamesettings)

    # Grouping blocks and pellets
    blocks = Group()
    powerpills = Group()
    shield = Group()
    portal = Group()

    thepacman = Pacman(screen, gamesettings)

    # Making the ghosts
    redghost = Ghosts(screen, "red")
    cyanghost = Ghosts(screen, "cyan")
    orangeghost = Ghosts(screen, "orange")
    pinkghost = Ghosts(screen, "pink")


    startScreen.makeScreen(screen)
    gf.readFile(screen, blocks, shield, powerpills, portal)

    screen.fill(BLACK)
    while True:
        screen.fill(BLACK)
        showgamestats.blitstats()
        gf.check_events(thepacman)
        gf.check_collision(thepacman, blocks, powerpills, shield)
        thepacman.update()
        for block in blocks:
            block.blitblocks()
        for theshield in shield:
            theshield.blitshield()
        for pill in powerpills:
            pill.blitpowerpills()
        for theportal in portal:
            theportal.blitportal()
        thepacman.blitpacman()
        redghost.blitghosts()
        cyanghost.blitghosts()
        orangeghost.blitghosts()
        pinkghost.blitghosts()

        pygame.display.flip()


game = Game()
game.play()

