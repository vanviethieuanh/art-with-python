import pygame
import random
import math

pygame.init()

win_width = 1200
win_height = 500
title = "Title gonna hear"

class Main:

    def __init__(self, windows,win_width,win_height):
        self.win = windows
        self.width = win_width
        self.height = win_height
    def Update(self):
        win.fill((0,0,0))
        
        
        
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
