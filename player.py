from settings import *
import pygame
from pygame import *

class Player:
    def __init__(self, surface):
        #Variable to store
        # 1. color
        # 2. speed
        # 3. posx, posy
        # 4. rect object
        # 5. width and height

        self.color = GREEN
        
        self.speed = 6
        self.posx  = WIDTH//2
        self.posy  = HEIGHT - 20
       
         
        self.width = 80
        self.height = 10
        
        self.rect = pygame.Rect(self.posx, self.posy, self.width, self.height)
        self.paddleRect = pygame.draw.rect(surface, self.color,self.rect)
        
        self.score = 0
       
    def move(self):
        keys_pressed = pygame.key.get_pressed()
        if self.posx > 0:
            if keys_pressed[K_LEFT]:
                self.posx -= self.speed
        if (self.posx + self.width) < WIDTH:
            if keys_pressed[K_RIGHT]:
                self.posx += self.speed
                
            
    def update(self,surface):
        self.move()
        self.rect = pygame.Rect(self.posx, self.posy, self.width, self.height)
        self.paddleRect = pygame.draw.rect(surface, self.color,self.rect)
        
    def collisionDetect(self,rect_obj):
        return pygame.Rect.colliderect(self.paddleRect, rect_obj)

    def updateScore(self):
        self.score += 1
    def reset(self, surface):
        self.score = 0
        self.posx  = WIDTH//2
        self.posy  = HEIGHT - 20
       
        