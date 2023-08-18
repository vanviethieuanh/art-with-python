import pygame
import random
import math

pygame.init()

win_width = 500
win_height = 500
title = "Ellipse"

def getInCirclePoint(center, radius, phi):
    return (int((radius)*math.cos(phi) + center[0]),
            int((radius)*math.sin(phi) + center[1]))

class Main:

    radius1 = 150
    radius2 = 70
    
    phi1 = 0
    phi2 = 0
    
    center1 = (radius1+2*radius2+40,20+radius1)
    center2 = (20+radius2,radius2+2*radius1+40)
    
    omega = 0.01
    
    def __init__(self, windows,win_width,win_height):
        self.win = windows
        self.width = win_width
        self.height = win_height
        
        self.canvas = pygame.Surface((self.width,self.height),pygame.SRCALPHA, 32)
        pygame.draw.circle(self.canvas,(255,255,255),self.center1,self.radius1,1)
        pygame.draw.circle(self.canvas,(255,255,255),self.center2,self.radius2,1)
        
    def Update(self):
        win.fill((0,0,0))
        
        self.phi1 += self.omega
        self.phi2 += self.omega
        
        c1 = getInCirclePoint(self.center1, self.radius1, self.phi1)
        c2 = getInCirclePoint(self.center2, self.radius2, self.phi2)
        
        pygame.draw.circle(win,(255,255,255),c1,3)
        pygame.draw.circle(win,(255,255,255),c2,3)
        
        pygame.draw.line(win,(150,150,150),(c1[0],0),(c1[0],self.height))
        pygame.draw.line(win,(150,150,150),(0,c2[1]),(self.width,c2[1]))
        
        self.canvas.set_at((c1[0],c2[1]),(255,255,0))
        
        win.blit(self.canvas,(0,0))
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
