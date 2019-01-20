import pygame
from pygame import time, draw, init, display, event, QUIT, KEYDOWN, K_d, K_a, KEYUP, K_w, K_s, K_SPACE
from time import sleep


screen = display.set_mode((1024, 768))
screen.fill((0, 0, 0))

def text_get(txt = "", color = (0,0,0), x = 0, y = 0, size = 50):
    global screen
    myFont = pygame.font.SysFont("none", size)
    fontImage = myFont.render(txt, 0, (color)) 
    place = fontImage.get_rect(center=(x, y))
    screen.blit(fontImage, place)   
    display.update() 
    
    
def rating():
    init()
    text_get("Last 5 player results", (255 ,255,255), 512, 100, 100)
    sleep(0.5)
    with open("history.txt", "r") as file: 
        text = list(map(str, [line[:-1] for line in file]))[-5:]
        for i in range(5):
            text_get(text[i], (255,255,255), 512, 250 + i * 100, 79)
            sleep(0.5)
            
    # loop            
    while 1:
        for i in event.get():
            if i.type == QUIT:
                pygame.quit()
            elif i.type == KEYDOWN:
                if i.key == K_SPACE:
                    pygame.quit()
    # pygame.quit()
rating()
