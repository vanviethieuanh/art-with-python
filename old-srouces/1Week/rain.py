import pygame
import random
import math

pygame.init()

def newRain(width, rainlength):
    return (random.randint(-50,width),random.randint(-(rainlength),-(rainlength/2)),random.randint(1,3),0)

def endpoint(start,length,angle):
    return ((start[0]+length*math.cos((angle/180)*math.pi)),(start[1])+length)
    pass

class Main:
    elements = []
    gravity = 70
    rainlength = 150
    angle = 80
    
    def __init__(self, windows,win_height,win_width):
        self.win = windows
        self.width = win_width
        self.height = win_height
        for i in range(50):
            self.elements.append(newRain(self.width,self.rainlength))
        pass
    def Update(self):
        win.fill((0,0,0))
        
        for i in range(4):
            self.elements.append(newRain(self.width,self.rainlength))
           
        for e in range(len(self.elements)):
            self.elements[e] = (self.elements[e][0] + self.elements[e][3]*math.cos((self.angle/180)*math.pi),
                                self.elements[e][1] + self.elements[e][3],
                                self.elements[e][2],
                                self.gravity/self.elements[e][2])
        
        #draw rain
        for e in self.elements:
            if e[1] >= self.height + 20:
                self.elements.remove(e)
                continue
            length = self.rainlength / e[2]
            thickness = 3 / e[2]
            color = (240/e[2],240/e[2],240/e[2])
       
            pygame.draw.line(win, color,(e[0],e[1]),endpoint((e[0],e[1]),length,self.angle))
        
        pygame.display.update()
        pass
win_width = 1200
win_height = 500
limitFPS = 40

win = pygame.display.set_mode((win_width,win_height))
pygame.display.set_caption("It's heavy rain now")

main = Main(win,win_height,win_width)

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