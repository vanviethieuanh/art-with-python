import pygame
import random
import math

pygame.init()

win_width = 700
win_height = 700
limitfps = 30
title = "Perfect Ellipse Feynmen's Method"

def inCircle(origin, angle, radius):
    return (origin[0] + math.cos(math.pi*(angle/180))*radius,
            origin[1] - math.sin(math.pi*(angle/180))*radius)

def perpendicularVector(pointA,pointB):
    return (pointB[1] - pointA[1], pointA[0]-pointB[0])

def midPoint(pointA,pointB):
    return ((pointA[0]+pointB[0])/2,(pointA[1]+pointB[1])/2)

class Main:
    radius = 300

    # This is origin of the big circle also the first focus    
    origin = (350,350)

    # The abs(eccentricity) should be less than radius - 50px for best result
    eccentricity = 250
    focus = (origin[0] + eccentricity, origin[1])    
    
    reDrawLineRatio = 0.5
    i = 0

    def __init__(self, windows,win_width,win_height):
        self.win = windows
        self.width = win_width
        self.height = win_height
        #outline circle
        pygame.draw.circle(win,(0,255,255),self.origin,self.radius,3)
        #focus point
        pygame.draw.circle(win,(255,255,0),self.focus,5)
        pygame.draw.circle(win,(255,255,0),self.origin,2)
        
    def Update(self):
        self.i += 1
        end = inCircle(self.origin,self.i,self.radius)
        mid = midPoint(self.focus,end)
        perVec = perpendicularVector(self.focus,end)
        perVec = (perVec[0]*self.reDrawLineRatio,perVec[1]*self.reDrawLineRatio)
        if self.i >= 360 and self.i<360*2:
            pygame.draw.line(win,(255,255,255),
                             (mid[0]-perVec[0],mid[1]-perVec[1]),
                             (mid[0]+perVec[0],mid[1]+perVec[1]))
            
        if self.i <= 360:
            pygame.draw.line(win,(30,30,30),self.focus,end)
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
