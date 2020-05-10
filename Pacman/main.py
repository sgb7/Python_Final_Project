import math
import random

import pygame
import sys
import os
from pygame import mixer

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
#font = pygame.font.Font('freesanbold.ttf', 32)

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

        '''if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerPosX -= steps
                #Player moves left
                #Shifts to left animation
            if event.key == pygame.K_RIGHT:
                playerPosX += steps
                #Player moves right
                #Shifts to right animation
            if event.key == pygame.K_UP:
                playerPosY -= steps
                #Player moves up
                #Animation rotates so its facing up
            if event.key == pygame.K_DOWN:
                playerPosY += steps
                #Player moves down
                #Animation rotates so its facing down

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerPosX = playerPosX'''

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