# import pygame
import pygame

# initialize pygame
pygame.init()

#create screen
screen = pygame.display.set_mode((1204,720))

# title and icon
pygame.display.set_caption('Galaxy Wars')
icon = pygame.image.load('download.png')
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load('space-invaders.png')
playerX = 602
playerY = 600

def player():
    screen.blit(playerImg, (playerX, playerY))

#game running loop
running  = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # screen background color
    screen.fill((200, 200, 255))

    player()
    pygame.display.update()