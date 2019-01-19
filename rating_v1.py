import pygame
from pygame import time, draw, init, display, event, QUIT, KEYDOWN, K_d, K_a, KEYUP, K_w, K_s, K_SPACE
from time import sleep

def menu():
    init()
    
    screen = display.set_mode((500, 500))
    screen.fill((255, 255, 255))
    
    with open("history.txt", "r") as file: 
        text = list(map(str, [line[:-1] for line in file]))[-5:]
        for i in range(5):
            (x,y,fontSize) = (50,50 + 50 * i,50)
            myFont = pygame.font.SysFont("none", fontSize)
            fontColor = (0,0,0)
            fontImage = myFont.render(text[i], 0, (fontColor)) 
            screen.blit(fontImage,(x,y))
            display.update()
            
                
    while 1:
        for i in event.get():
            if i.type == QUIT:
                break
            elif i.type == KEYDOWN:
                if i.key == K_SPACE:
                    break
    pygame.quit()
menu()