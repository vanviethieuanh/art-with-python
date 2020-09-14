import pygame
import random
import math

pygame.init()

win_width = 400
win_height = 400

def distance(posA,posB):
    return ((posA[0]-posB[0])**2+(posA[1]-posB[1])**2)**0.5

class Wave:
    phi = 0
    def __init__(self,center):
        self.center = center

class Main:
    
    waves  = []
    lamda  = 10
    omega  = -0.1
    
    def __init__(self, windows,win_width,win_height):
        self.win = windows
        self.width = win_width
        self.height = win_height
        self.waves.append(Wave((50,50)))
        self.waves.append(Wave((200,200)))
    
    def Update(self):
        win.fill((0,0,0))
        
        for i in range(len(self.waves)):
            self.waves[i].phi += self.omega
        
        for x in range(self.width):
            for y in range(self.height):
                a = 0
                for w in self.waves:
                    a += math.cos(w.phi+(distance((x,y),w.center)/self.lamda)*2*math.pi)
                a += 2
                color = int(60*a)
                win.set_at((x, y), (color,color,color))
        
        pygame.display.update()
        pass
    pass

win = pygame.display.set_mode((win_width,win_height))
pygame.display.set_caption("Wave Interference")

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