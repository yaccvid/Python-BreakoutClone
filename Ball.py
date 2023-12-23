import pygame
from pygame import *

from settings import *
import random
class Ball:
    def __init__(self, surface):
        #Variables to store:
        # 1. Radius of ball
        # 2. posx, posy
        # 3. rect object
        # 4. color
    
        self.radius = 5
        self.color  = WHITE
        
        self.posy   = HEIGHT//2
        self.posx   = WIDTH//2
        
        self.ballRect = pygame.draw.circle(surface, self.color, (self.posx, self.posy), self.radius)
        
        self.xslope    = random.choice(SLOPES)
        self.yslope    = random.choice(SLOPES)
        self.speed    = 5
        
    def reverseYDir(self):
        self.yslope *= -1
            
    def move(self):
        if self.posx <= 0 or self.posx >= WIDTH:
            self.xslope *= -1
        if self.posy <= 0 or self.posy >= HEIGHT:
            self.yslope *= -1
            
        self.posx += self.xslope*self.speed
        self.posy += self.yslope*self.speed
        
    def update(self,surface):
        self.move()
        self.ballRect = pygame.draw.circle(surface, self.color, (self.posx, self.posy), self.radius)

    def hasBallHitGround(self):
        if self.posy >= HEIGHT:
            return True
        else:
            return False
     
    def reset(self, surface):
        self.posy   = HEIGHT//2
        self.posx   = WIDTH//2
        self.xslope    = random.choice(SLOPES)
        self.yslope    = random.choice(SLOPES)