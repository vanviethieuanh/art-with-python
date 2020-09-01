import pygame
import random
import math

pygame.init()

win_width = 1200
win_height = 900
title = "Lissajous curve"

def getInCirclePoint(center, radius, phi):
    return (int((radius)*math.cos(phi) + center[0]),
            int((radius)*math.sin(phi) + center[1]))

class Main:
    
    radius = 30
    rows = []
    columns = []
    omega = 0.005
    
    def __init__(self, windows,win_width,win_height):
        self.win = windows
        self.width = win_width
        self.height = win_height
        for i in range(2,9):
            center = (self.radius+10,(self.radius + 10)*i*2)
            self.rows.append([center,0])
        
        for i in range(2,15):
            center = ((self.radius + 10)*i*2,self.radius+10)
            self.columns.append([center,0])
            
        self.canvas = pygame.Surface((self.width,self.height), pygame.SRCALPHA, 32)
        
    def Update(self):
        win.fill((0,0,0))
        
        ys = []
        xs = []
        
        for i in range(len(self.rows)):
            pygame.draw.circle(win, (250,250,250), 
                               self.rows[i][0],
                               self.radius,1)
        
        for i in range(len(self.columns)):
            pygame.draw.circle(win, (250,250,250), 
                               self.columns[i][0],
                               self.radius,1)
        
        for i in range(len(self.rows)):
            self.rows[i][1] += self.omega * (i+1)
            if self.rows[i][1] == 360 :
                self.rows[i][1] = 0
            inC = getInCirclePoint(self.rows[i][0],self.radius,self.rows[i][1])
            pygame.draw.circle(win, (255,255,255), (inC[0], inC[1]), 2)
            pygame.draw.line(win,(150,150,150),(0,inC[1]),(self.width,inC[1]))
            ys.append(inC[1])
            
        for i in range(len(self.columns)):
            self.columns[i][1] += self.omega * (i+1)
            if self.columns[i][1] == 360 :
                self.columns[i][1] = 0
                
            inC = getInCirclePoint(self.columns[i][0],self.radius,self.columns[i][1])
            pygame.draw.circle(win, (255,255,255), (inC[0], inC[1]), 2)
            pygame.draw.line(win,(150,150,150),(inC[0],0),(inC[0],self.height))
            xs.append(inC[0])
        
        for x in xs:
            for y in ys:
                self.canvas.set_at((x,y),(255,255,255))
        
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