# Aaron Xaymountry
# CPSC 386-01
# MW 5:30-6:45pm
# Pacman game with portals

import pygame
from pygame.sprite import Group
import sys
from blocks import Blocks
from shield import Shield
from powerpills import Powerpills
from portal import Portal

def check_events(pacman):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, pacman)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, pacman)

def check_keydown_events(event, pacman):
    """Respond to keypresses."""
    if event.key == pygame.K_UP:
        pacman.moving_up = True
    elif event.key == pygame.K_DOWN:
        pacman.moving_down = True
    elif event.key == pygame.K_RIGHT:
        pacman.moving_right = True
    elif event.key == pygame.K_LEFT:
        pacman.moving_left = True
    elif event.key == pygame.K_SPACE:
        pass
    elif event.key == pygame.K_QUIT:
        sys.exit()


def check_keyup_events(event, pacman):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        pacman.moving_right = False
    elif event.key == pygame.K_LEFT:
        pacman.moving_left = False
    elif event.key == pygame.K_UP:
        pacman.moving_up = False
    elif event.key == pygame.K_DOWN:
        pacman.moving_down = False


# Check direction pacman is going to compare and see if he can't go a direction anymore if he hit a block
def check_direction(pacman, block):
    left = False
    right = False
    up = False
    down = False
    if pacman.rect.centerx <= block.rect.centerx:
        right = True
    else:
        left = True
    if pacman.rect.y + pacman.rect.height / 2 <= block.rect.y + block.rect.height / 2:
        up = True
    else:
        down = True

    if left:
        pacman.x += 1
    elif right:
        pacman.x -= 1
    if up:
        pacman.y -= 1
    elif down:
        pacman.y += 1

# Check the direction pacman is going for the collision with the shield
def check_shield_direction(pacman, shield):
    left = False
    right = False
    up = False
    down = False

    if pacman.rect.centerx <= shield.rect.centerx:
        right = True
    else:
        left = True
    if pacman.rect.y + pacman.rect.height / 2 <= shield.rect.y + shield.rect.height / 2:
        up = True
    else:
        down = True

    if left:
        pacman.x += 1
    elif right:
        pacman.x -= 1
    if up:
        pacman.y -= 1
    elif down:
        pacman.y += 1

# Pacman collision handling
def check_collision(pacman, blocks, powerpills, shield):
    for block in blocks:
        if pygame.sprite.collide_rect(pacman, block):
            print("collided")
            check_direction(pacman, block)
    for theshield in shield:
        if pygame.sprite.collide_rect(pacman, theshield):
            print("shield")
            check_shield_direction(pacman, theshield)
    for powerpill in powerpills:
        if pygame.sprite.collide_rect(pacman, powerpill):
            print("Eaten")
            powerpill.remove(powerpills)


# Read in text file of maze and then fill in X's with a block
def readFile(screen, blocks, shield, powerpills, portal):
    file = open("images/otherpacmanportalmaze.txt", "r")
    contents = file.read()
    line = ''
    all_lines = []
    for chars in contents:
        if chars != '\n':
            line += chars
        else:
            all_lines.append(line)
            line = ''
    i = 0
    j = 0
    for rows in all_lines:
        for chars in rows:
            if chars == 'X':
                new = Blocks(screen)
                new.rect.x, new.rect.y = 13 * i, 13 * j
                blocks.add(new)
            elif chars == 'd':
                thepowerpill = Powerpills(screen)
                thepowerpill.rect.x, thepowerpill.rect.y = 13 * i, 13 * j
                powerpills.add(thepowerpill)
            elif chars == 'o':
                theshield = Shield(screen)
                theshield.rect.x, theshield.rect.y = 13 * i, 13 * j
                shield.add(theshield)
            # This is where the horizontal portal is supposed to be
            elif chars == 'h':
                pass
            # Vertical portal?
            elif chars == 'P':
                theportal = Portal(screen)
                theportal.rect.x, theportal.rect.y = 13 * i, 13 * j
                portal.add(theportal)
                pass
            i += 1
        i = 0
        j += 1
