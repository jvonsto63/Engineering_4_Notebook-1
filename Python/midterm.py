import pygame
import sys
import os
import random

pygame.init()
pygame.display.set_caption('nice little title')

screenWidth = 500
screenHeight = 500
screenSize = [screenWidth, screenHeight]
screen = pygame.display.set_mode(screenSize)
hotOrange = (248,113,70)
screen.fill(hotOrange)

length = 10
width = 10
loopcount = 4096
minPos = 0
maxPos = 490
colorMin = 0
colorMax = 255
solid = 0
for i in range(loopcount):
    left = random.randint(minPos,maxPos)
    top = random.randint(minPos,maxPos)
    rect1 = pygame.Rect(left, top, length, width)

    color = (random.randint(colorMin,colorMax), random.randint(colorMin,colorMax), random.randint(colorMin,colorMax))

    pygame.draw.rect(screen, color, rect1, solid)

pygame.display.update()

while(True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit();


