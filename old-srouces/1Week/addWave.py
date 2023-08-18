import pygame
import random
import math

pygame.init()

win_width = 1200
win_height = 280
limitFPS = 30

def getInCirclePoint(center, radius, phi):
    return ((radius)*math.cos(phi) + center[0],
            (radius)*math.sin(phi) + center[1])

class Main:
    
    radius  = 80
    radius1 = 60
    omega   = 0.005
    phi     = 0
    waves   = []
    waves1   = []
    
    def __init__(self, windows,win_width,win_height):
        self.win = windows
        self.width = win_width
        self.height = win_height
    def Update(self):
        win.fill((0,0,0))
        
        self.phi += self.omega*math.pi
        
        #draw Unit Circle
        pygame.draw.circle( self.win,
                            (255,255,255),
                            (self.radius + self.radius1,self.radius + self.radius1),
                            self.radius,1)
                
        #angle
        inCirclePoint = getInCirclePoint((self.radius + self.radius1,self.radius + self.radius1),self.radius,self.phi)
        inCirclePoint1 = getInCirclePoint(inCirclePoint,self.radius1,self.phi+0.5*math.pi)
                
        #another circle
        pygame.draw.circle( self.win,
                            (255,255,0),
                            (int(inCirclePoint[0]),int(inCirclePoint[1])),
                            self.radius1,1)
        
        #angleLines
        pygame.draw.line(self.win,
                        (255,255,255),
                        (self.radius + self.radius1,self.radius + self.radius1),
                        inCirclePoint)
        pygame.draw.line(self.win,
                        (255,255,0),
                        inCirclePoint,
                        inCirclePoint1)                
                        
        #pointer
        pygame.draw.line(self.win,
                        (255,255,255),
                        inCirclePoint,
                        (300,inCirclePoint[1]))
        pygame.draw.line(self.win,
                        (255,255,0),
                        inCirclePoint1,
                        (300,inCirclePoint1[1]))
        
        #seperator
        pygame.draw.line(self.win,
                        (255,255,255),
                        (300,0),
                        (300,300))
                        
        self.waves.append((300,int(inCirclePoint[1])))
        self.waves1.append((300,int(inCirclePoint1[1])))
        for i in range(len(self.waves)):
            self.waves[i] = (self.waves[i][0]+1,self.waves[i][1])
            pygame.draw.circle(self.win,
                        (255,255,255),
                        self.waves[i],
                        1)
        for wave in self.waves:
            if wave[0] > self.width:
                self.waves.remove(wave)
                
        for i in range(len(self.waves1)):
            self.waves1[i] = (self.waves1[i][0]+1,self.waves1[i][1])
            pygame.draw.circle(self.win,
                        (255,255,0),
                        self.waves1[i],
                        3)
        for wave in self.waves1:
            if wave[0] > self.width:
                self.waves1.remove(wave)
                
        for i in range (30):
            if i != 4:
                pygame.draw.line(win, (150,150,150), (295,i*10),(305,i*10))
        for i in range (4,30,5):
                pygame.draw.line(win, (255,255,255), (293,i*10),(307,i*10),2)
        pygame.display.update()
        
        pass
    pass

win = pygame.display.set_mode((win_width,win_height))
pygame.display.set_caption("60 and 80 is 100")

main = Main(win,win_width,win_height)

run = True
while run:
    clock = pygame.time.Clock()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    main.Update()    
    clock.tick(limitFPS)
    
    pass
pygame.quit()