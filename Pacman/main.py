import math
import random

import pygame
import sys
import os
from pygame import mixer

'''class Player(pygame.sprite.Sprite):
    def  __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.xPos = 0
        self.yPos =  0
        self.image = pygame.image.load('Images/PlayerRight3.png')
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = pygame.Rect(self.x, self.y, 40, 40)

    def movement(self, x, y):
        self.xPos += x
        self.yPos += y

    def update(self, x, y):
        screen.blit(self, (x, y))'''

pygame.init()

screen = pygame.display.set_mode((800, 600))

playerImgRight = pygame.image.load('Images/PlayerRight3.png')
playerImgRight = pygame.transform.scale(playerImgRight, (40, 40))
playerImgLeft = pygame.image.load('Images/PlayerLeft3.png')
playerImgLeft = pygame.transform.scale(playerImgLeft,  (40, 40))

playerImg = playerImgRight
playerImg = pygame.transform.scale(playerImg, (40, 40))

playerImgDown = pygame.transform.rotate(playerImg, -90)
playerImgUp = pygame.transform.rotate(playerImg, 90)

playerPosX = 100
playerPosY = 100
steps = 5
# Idea: create an array of player images, and a variable "playerImg", which changes for
# the situation. Images are selected from the array.

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

def player(x, y):
    screen.blit(playerImg, (x, y))

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

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        playerImg = playerImgLeft
        playerPosX -= steps
        if playerPosX <= 0:
            playerPosX = 0

    if keys[pygame.K_RIGHT]:
        playerImg = playerImgRight
        playerPosX += steps
        if playerPosX >= 760:
            playerPosX = 760

    if keys[pygame.K_UP]:
        playerImg = playerImgUp
        playerPosY -= steps
        if playerPosY <= 0:
            playerPosY = 0

    if keys[pygame.K_DOWN]:
        playerImg = playerImgDown
        playerPosY += steps
        if playerPosY >= 560:
            playerPosY = 560

    player(playerPosX, playerPosY)
    pygame.display.update()