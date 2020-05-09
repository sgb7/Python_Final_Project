import math
import random

import pygame
import sys
import os
from pygame import mixer

# OBJECTS:
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.moveX = 0
        self.moveY = 0
        self.frame = 0
        self.images = []

        for i in range(1, 4):
            img = pygame.image.load(os.path.join('Images', 'PlayerRight' + str(i) + '.png')).convert()
            #img.convert_alpha()
            #img.set_colorkey(ALPHA)
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()

    def movement(self, x, y):
        self.moveX += x
        self.moveY += y

    def update(self):
        self.rect.x = self.rect.x + self.moveX
        self.rect.y = self.rect.y + self.moveY

        if self.moveX < 0:
            self.frame += 1
            if self.frame > 3*ani:
                self.frame = 0
            self.image = self.images[self.frame//ani]

        if self.moveX > 0:
            self.frame += 1
            if self.frame > 3*ani:
                self.frame = 0
            self.image = self.images[(self.frame//ani)+4]

pygame.init()

screen = pygame.display.set_mode((800, 600))

# Going to need to  upload a background image to use
# Also, I'll probably need to make the 'barriers' that make up the maze seperately.
# Figure out how  to make it so characters can't pass through them.

# Load sound, if I want background music.

pygame.display.set_caption("Pacman Remade")
icon = pygame.image.load('Images/GreenGhostForward.png')
pygame.display.set_icon(icon)
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

fps = 40
ani = 4
clock = pygame.time.Clock()

player = Player()
player.rect.x = 0
player.rect.y = 0
playerGroup =  pygame.sprite.Group()
playerGroup.add(player)
steps = 10 #How fast to move


# Okay, game loop time!
running = True
while running:

    screen.fill((0, 0, 0))
    # screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.movement(-steps,  0)
                #Player moves left
                #Shifts to left animation
            if event.key == pygame.K_RIGHT:
                player.movement(steps,  0)
                #Player moves right
                #Shifts to right animation
            if event.key == pygame.K_UP:
                player.movement(0, steps)
                #Player moves up
                #Animation rotates so its facing up
            if event.key == pygame.K_DOWN:
                player.movement(0,  -steps)
                #Player moves down
                #Animation rotates so its facing down

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_Left:
                player.movement(steps, 0)
            if event.key == pygame.K_RIGHT:
                player.movement(-steps, 0)
            if event.key == pygame.K_UP:
                player.movement(0, -steps)
            if event.key == pygame.K_DOWN:
                player.movement(0, steps)
                #Player doesn't move
                #Animation remains what it was OR switchs to forward?

    player.update()
    playerGroup.draw(screen)
    clock.tick(fps)

    pygame.display.update()