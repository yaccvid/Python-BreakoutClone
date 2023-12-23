from pickle import REDUCE
import pygame
from pygame import *

import sys
from Bricks import *
from player import *
from Ball import *
from settings import *


#Initialise

pygame.init()
pygame.font.init()

SCREEN_SURFACE = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breakout")

FRAMES_PER_SECOND = pygame.time.Clock()

running = True
gameOvr = False


P = Player(SCREEN_SURFACE)
B = Ball(SCREEN_SURFACE)
#E = Brick(SCREEN_SURFACE)
E1 = Enemies(SCREEN_SURFACE)
#Game Loop

def printYouLose(surface, score):
    font = pygame.font.Font('freesansbold.ttf', 32)
    string = "You Lose! Game Over " + "Score: " + str(score)
    text = font.render(string, True, GREEN, BLACK)
    textRect = text.get_rect()
    textRect.center = (WIDTH // 2, HEIGHT // 2)
    surface.blit(text, textRect)
    #print("You Lose")

def printYouWin(surface, score):
    font = pygame.font.Font('freesansbold.ttf', 32)
    string = "You Win! Game Over " + "Score: " + str(score)
    text = font.render(string, True, GREEN, BLACK)
    textRect = text.get_rect()
    textRect.center = (WIDTH // 2, HEIGHT // 2)
    surface.blit(text, textRect)
#    print("You Win")

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
    if not gameOvr:
        SCREEN_SURFACE.fill(BLACK)
        P.update(SCREEN_SURFACE)
        #if pygame.Rect.colliderect(P.paddleRect, B.ballRect):
        if P.collisionDetect(B.ballRect):
            B.reverseYDir()
        if E1.collisionDetect(B.ballRect):# or E.collisionDetect(B.ballRect):
            B.reverseYDir()
            P.updateScore()
        

        B.update(SCREEN_SURFACE)
        E1.update(SCREEN_SURFACE)
    
      
    else:
        #Keep showing Game over and wait for a key event then reset game
        keys_pressed = pygame.key.get_pressed()
        #print("Her")
        if keys_pressed[K_y]:
            gameOvr = False
            P.reset(SCREEN_SURFACE)
            E1.reset(SCREEN_SURFACE)
            B.reset(SCREEN_SURFACE)
     
    if B.hasBallHitGround():
        printYouLose(SCREEN_SURFACE, P.score)
        gameOvr = True
    if E1.allEnemiesKilled():
        printYouWin(SCREEN_SURFACE, P.score)
        gameOvr = True
    
    pygame.display.flip() #Update Screen
    FRAMES_PER_SECOND.tick(FPS)