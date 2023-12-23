import pygame
from pygame import *

from settings import *

class Brick:
    def __init__(self,surface,posx = 50,posy  = 40):
        self.width  = 60
        self.height = 10
        self.color  = RED
        
        self.posx   = posx
        self.posy   = posy
    
        self.rect = pygame.Rect(self.posx, self.posy, self.width, self.height)
        self.brickRect = pygame.draw.rect(surface, self.color,self.rect)
        
    def update(self,surface):
        self.rect = pygame.Rect(self.posx, self.posy, self.width, self.height)
        self.brickRect = pygame.draw.rect(surface, self.color,self.rect)
        
    def collisionDetect(self,rect_obj):
        return pygame.Rect.colliderect(self.brickRect, rect_obj)
    


class Enemies:
    def __init__(self,surface):
        self.n_enemies = 27 #A 2d array of 5 coloumns in each row
        self.Bricks = []
        startx = 10
        starty = 30
        width  = 60
        height = 10
        col_no = 0
        space = 10
        bricks_per_row = 9
        
        #tmp = Brick(surface, startx, starty)
        #tmp1 = Brick(surface, startx+10+60, starty)
        #self.Bricks.append(tmp)
        #self.Bricks.append(tmp1) 
        
        for brick in range(0,self.n_enemies):
            row_no = brick // bricks_per_row
            col_no = brick % bricks_per_row
            newx   = startx + col_no*(width + space)
            newy   = starty + row_no*(height + space)
            tmp    = Brick(surface, newx, newy)
            
            self.Bricks.append(tmp)
            
    def refill(self,surface):
        startx = 10
        starty = 30
        width  = 60
        height = 10
        col_no = 0
        space = 10
        bricks_per_row = 9
        
        #tmp = Brick(surface, startx, starty)
        #tmp1 = Brick(surface, startx+10+60, starty)
        #self.Bricks.append(tmp)
        #self.Bricks.append(tmp1) 
        
        for brick in range(0,self.n_enemies):
            row_no = brick // bricks_per_row
            col_no = brick % bricks_per_row
            newx   = startx + col_no*(width + space)
            newy   = starty + row_no*(height + space)
            tmp    = Brick(surface, newx, newy)
            
            self.Bricks.append(tmp)
        
    def update(self,surface):
        for brick in self.Bricks:
            brick.update(surface)
     
    def collisionDetect(self,rect_obj):
        idx = 0
        for brick in self.Bricks:
            if brick.collisionDetect(rect_obj):
                #Remove That Brick
                self.Bricks.pop(idx)
                return True
            idx = idx + 1
        return False
    def allEnemiesKilled(self):
        if len(self.Bricks) == 0:
            return True
        else:
            return False
    def reset(self,surface):
        #Refill Bricks list
        self.Bricks.clear()
        self.refill(surface)