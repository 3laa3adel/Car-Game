import pygame
import sys
import random
import time
from pygame.locals import*
from tkinter import *
from pygame import mixer
mixer.init()
mixer.music.load("Images & Sounds/Versace.wav")
mixer.music.play(-1)
pygame.init()
screen = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("Car Game")
car1 = pygame.image.load("Images & Sounds/Car1.png")
left = pygame.image.load("Images & Sounds/left.png")
right = pygame.image.load("Images & Sounds/right.png")
line = pygame.image.load("Images & Sounds/Line.png")
width = 25
######################################################


def drawcar(x, y):

    screen.blit(car1, (x, y))  # set Positin
######################################################


def enemycar(enemey_at_x, enemey_at_y, enemy):
    if enemy == 0:
        screen.blit(pygame.image.load(
            "Images & Sounds/Enemy1.png"), (enemey_at_x, enemey_at_y))  # Load Enemy1 Car
    if enemy == 1:
        screen.blit(pygame.image.load(
            "Images & Sounds/Enemy2.png"), (enemey_at_x, enemey_at_y))  # Load Enemy2 Car
    if enemy == 2:
        screen.blit(pygame.image.load(
            "Images & Sounds/Enemy3.png"), (enemey_at_x, enemey_at_y))  # Load Enemy3 Car
    if enemy == 3:
        screen.blit(pygame.image.load(
            "Images & Sounds/Enemy4.png"), (enemey_at_x, enemey_at_y))  # Load Enemy4 Car
    if enemy == 4:
        screen.blit(pygame.image.load(
            "Images & Sounds/Enemy5.png"), (enemey_at_x, enemey_at_y))  # Load Enemy5 Car
######################################################


def text_edit(text, font):
    tt = font.render(text, True, (255, 0, 0))
    return tt, tt.get_rect()
######################################################


def gameover(text):
    txt = pygame.font.Font("Images & Sounds/FreeSansBold.ttf", 80)
    txt1, txt2 = text_edit(text, txt)
    txt2.center = ((500), (300))
    screen.blit(txt1, txt2)
    pygame.display.update()
    time.sleep(0)
######################################################


def pressspace(text):
    txt = pygame.font.Font("Images & Sounds/FreeSansBold.ttf", 30)
    txt1, txt2 = text_edit(text, txt)
    txt2.center = ((500), (500))
    screen.blit(txt1, txt2)
    pygame.display.update()
    time.sleep(0)
    out = True
    while out:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Quit
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:  # Return The Game
                if event.key == pygame.K_SPACE:
                    out = False
    Game()
######################################################


def Game():
    play = True
    x = 385
    y = 400
    x_new = 0
    enemyspeed = 12
    enemy = 0
    enemey_at_x = random.randrange(500, 600)
    enemey_at_y = -800
    enemyheight = 55
    enemywidth = 25
    while play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYUP:  # Don't Press Any Button
                x_new = 0
            if event.type == pygame.KEYDOWN:  # Press Any Button
                if event.key == pygame.K_LEFT:
                    x_new = - 15
                if event.key == pygame.K_RIGHT:
                    x_new = 15
        x += x_new  # Update x Position
        screen.fill((170, 170, 170))  # Set Color Gray
        screen.blit(left, (-440, 1))  # Draw Left Side
        screen.blit(line, (7, 1))  # Draw Line
        screen.blit(right, (440, 1))  # Draw Right Side
        drawcar(x, y)  # Draw Car
        enemycar(enemey_at_x, enemey_at_y, enemy)  # Draw Enemy Car
        enemyspeed += 0.001  # Update Speed(Enemy) Position
        enemey_at_y -= (enemyspeed/4)  # Update Y(Enemy) Position
        enemey_at_y += enemyspeed  # Update Y(Enemy) Position
        if enemey_at_y > 600:  # Update Enemy
            enemey_at_x = random.randrange(130, 700)
            enemey_at_y = -enemyheight
            enemy = random.randrange(0, 5)
        if x < 131 or x > 640:  # Hit In Right Side Or Left Side
            gameover("Game Over")
            pressspace("Press Space To Return")
        if y < enemey_at_y+enemyheight:  # Hit Enemy
            if x < enemey_at_x+enemywidth and x > enemey_at_x or x+width > enemey_at_x and x+width < enemey_at_x+enemywidth:
                gameover("Game Over")
                pressspace("Press Space To Return")
        pygame.display.update()


######################################################
# Main
Game()
pygame.quit()
quit()
