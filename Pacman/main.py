import math
import random

import pygame
import sys
import os
from pygame import mixer

class Player(pygame.sprite.Sprite):
    def __init__(self, xPos, yPos):
        self.image = pygame.image.load('Images/PlayerRight3.png')
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.x = xPos
        self.y = yPos
        self.rect = pygame.Rect(self.x, self.y, 40, 40)

    def image_switch(self, direction):
        playerLeft = pygame.image.load('Images/PlayerLeft3.png')
        playerLeft = pygame.transform.scale(playerLeft, (40, 40))
        playerRight = pygame.image.load('Images/PlayerRight3.png')
        playerRight = pygame.transform.scale(playerRight, (40, 40))
        playerDown = pygame.transform.rotate(self.image, -90)
        playerUp = pygame.transform.rotate(self.image, 90)

        if direction == "left":
            self.image = playerLeft
        elif direction == "right":
            self.image = playerRight
        elif direction == "up":
            self.image == playerUp
        elif direction == "down":
            self.image == playerDown
        else:
            self.image = self.image

    def update(self, x, y):
        screen.blit(self.image, (x, y))

class Walls(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

class Enemies(pygame.sprite.Sprite):
    def __init__(self, color, xPos, yPos):
        ghosts = ['Images/GreenGhostForward.png', 'Images/OrangeGhostForward.png', 'Images/PinkGhostForward.png', 'Images/YellowGhostForward.png']
        if color == "green":
            self.image = pygame.image.load(ghosts[0])
            self.image = pygame.transform.scale(self.image, (40, 40))
        elif color == "orange":
            self.image = pygame.image.load(ghosts[1])
            self.image = pygame.transform.scale(self.image, (40, 40))
        elif color == "pink":
            self.image = pygame.image.load(ghosts[2])
            self.image = pygame.transform.scale(self.image, (40, 40))
        elif color == "yellow":
            self.image = pygame.image.load(ghosts[3])
            self.image = pygame.transform.scale(self.image, (40, 40))
        else:
            self.image = pygame.image.load(ghosts[0])
            self.image = pygame.transform.scale(self.image, (40, 40))

        self.x = xPos
        self.y = yPos
        self.rect = pygame.Rect(self.x, self.y, 40, 40)

    #def target_player(playerX, playerY):
        # Get ghost to move towards player. How?

    def update(self, x, y):
        screen.blit(self.image, (x, y))

# Need some sort of tilemap class?




pygame.init()

screen = pygame.display.set_mode((800, 800))

# Player
playerPosX = 100
playerPosY = 100
player = Player(playerPosX, playerPosY)
steps = 5

# Ghosts
enemyPosX = 200
enemyPosY = 200
ghostG = Enemies("green", enemyPosX, enemyPosY)
steps = 3

# Map of Walls

wallMap = ["CHHHHHHC",
           "V......V",
           "V......V",
           "V......V",
           "V......V",
           "V......V",
           "V......V",
           "CHHHHHHC"]

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
#font = pygame.font.SysFont('comicsansms', 32)
#This works, but the game takes longer to start up

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

# Note for enemy programming: enemy just needs to target player (and not try and go through walls to do it; do a 180 towards player
# each time a wall is collided with?)


# Okay, game loop time!
running = True
while running:

    screen.fill((0, 0, 0))
    # screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        player.image_switch("left")
        playerPosX -= steps
        if playerPosX <= 0:
            playerPosX = 0

    if keys[pygame.K_RIGHT]:
        player.image_switch("right")
        playerPosX += steps
        if playerPosX >= 760:
            playerPosX = 760

    if keys[pygame.K_UP]:
        player.image_switch("up")
        playerPosY -= steps
        if playerPosY <= 0:
            playerPosY = 0

    if keys[pygame.K_DOWN]:
        player.image_switch("down")
        playerPosY += steps
        if playerPosY >= 760:
            playerPosY = 760

    #screen.blit(WallVS, (-15, 0))
    #player(playerPosX, playerPosY)
    player.update(playerPosX, playerPosY)
    ghostG.update(enemyPosX, enemyPosY)
    pygame.display.update()