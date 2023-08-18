import pygame
import random
import math

pygame.init()

win_width = 500
win_height = 500
title = "Net"

def dist(posA,posB):
    return ((posA[0]-posB[0])**2+(posA[1]-posB[1])**2)**0.5

def move(posA,posB,speed):
    return ((posA[0] + int((posB[0]-posA[0])*speed)),
            (posA[1] + int((posB[1]-posA[1])*speed)))

class Main:
    
    dots = []
    dotsTar = []
    dotRadius = 3
    
    def __init__(self, windows,win_width,win_height):
        self.win = windows
        self.width = win_width
        self.height = win_height
        
        for _ in range(50):
            x = random.randint(self.dotRadius,self.width)
            y = random.randint(self.dotRadius,self.height)
            self.dots.append((x,y))
            self.dotsTar.append((x + random.randint(-10,10),
                                 y + random.randint(-10,10)))
        
    def Update(self):
        win.fill((0,0,0))
        
        for i in range(len(self.dots)):
            self.dots[i] = move(self.dots[i],self.dotsTar[i],0.05)
            pygame.draw.circle(win,(200,200,200),self.dots[i],self.dotRadius)
            if dist(self.dotsTar[i],self.dots[i]) <= 29:
                #For the reason that the distance must be < ((step*2)/0.05)/100, the move function will return a point diffence with PosA
                self.dotsTar[i] = (self.dots[i][0] + random.randint(-70,70),
                                   self.dots[i][1] + random.randint(-70,70))
            if self.dotsTar[i][0] <= 0:
                self.dotsTar[i] = (0,self.dotsTar[i][1])
            if self.dotsTar[i][1] <= 0:
                self.dotsTar[i] = (self.dotsTar[i][0],0)
            if self.dotsTar[i][0] >= self.width:
                self.dotsTar[i] = (self.width,self.dotsTar[i][1])
            if self.dotsTar[i][1] >= self.height:
                self.dotsTar[i] = (self.dotsTar[i][0],self.height)
        for i in range(len(self.dots)):
            for j in range(i+1, len(self.dots)):
                if dist(self.dots[i],self.dots[j]) < 70:
                    pygame.draw.line(win,(200,200,200),self.dots[i],self.dots[j])
            
            
        pygame.display.update()
        pass
    pass

win = pygame.display.set_mode((win_width,win_height))
pygame.display.set_caption(title)

main = Main(win,win_width,win_height)

run = True
while run:
    clock = pygame.time.Clock()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    main.Update()    
    clock.tick()
    
    pass
pygame.quit()