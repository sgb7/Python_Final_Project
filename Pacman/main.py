import math
import random

import pygame
from pygame import mixer

pygame.init()

screen = pygame.display.set_mode((800, 600))

# Going to need to  upload a background image to use
# Also, I'll probably need to make the 'barriers' that make up the maze seperately.
# Figure out how  to make it so characters can't pass through them.

# Load sound, if I want background music.

pygame.display.set_caption("Pacman Remade")
# Set icon

# Player image?
# Enemy images?

# Also what about points, and those things that make the ghosts eatable? Fruits?
# Start with points and killable ghosts, then add fruit if there's time.

score_value = 0
#font = pygame.font.Font('freesanbold.ttf', 32)

# Game over
#over_font = pygame.font.Font('freesanbold.ttf', 64)

def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

# Need a defintion for collisions between ghosts and pacman.
# Also maybe one for pacman and points/fruit?
# Characters and walls?


# Okay, game loop time!
running = True
while running:

    screen.fill((0, 0, 0))
    # screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()