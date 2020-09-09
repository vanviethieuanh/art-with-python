import pygame
import random
import math

pygame.init()

win_width = 1200
win_height = 1000
limitfps = 30
title = "Perfect Ellipse Feynmen's Method"

def inCircle(center, angle, radius):
    return (center[0] + math.cos(math.pi*(angle/180))*radius,
            center[1] - math.sin(math.pi*(angle/180))*radius)

def perpendicularVector(pointA,pointB):
    return (pointB[1] - pointA[1], pointA[0]-pointB[0])

def midPoint(pointA,pointB):
    return ((pointA[0]+pointB[0])/2,(pointA[1]+pointB[1])/2)

class Main:

    center = (400,400)
    radius = 300
    focus  = 60
    focus1  = (center[0]+radius - focus,400)
    focus2  = (center[0],400)
    reDrawLineRatio = 0.5
    i = 0

    def __init__(self, windows,win_width,win_height):
        self.win = windows
        self.width = win_width
        self.height = win_height
        #outline circle
        pygame.draw.circle(win,(0,255,255),self.center,self.radius,3)
        #focus point
        pygame.draw.circle(win,(255,255,0),self.focus1,5)
        pygame.draw.circle(win,(255,255,0),self.focus2,2)
        
    def Update(self):
        self.i += 1
        end = inCircle(self.center,self.i,self.radius)
        mid = midPoint(self.focus1,end)
        perVec = perpendicularVector(self.focus1,end)
        perVec = (perVec[0]*self.reDrawLineRatio,perVec[1]*self.reDrawLineRatio)
        if self.i >= 360 and self.i<360*2:
            pygame.draw.line(win,(255,255,255),
                             (mid[0]-perVec[0],mid[1]-perVec[1]),
                             (mid[0]+perVec[0],mid[1]+perVec[1]))
            
        if self.i <= 360:
            pygame.draw.line(win,(30,30,30),self.focus1,end)
            win.set_at((int(mid[0]), int(mid[1])),(0,255,0))
            
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
    clock.tick(limitfps)
    
    pass
pygame.quit()
