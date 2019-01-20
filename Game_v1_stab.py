import random
from menu_t_v2 import menu
from map_ import make_map
import pygame

def keyPressed(inputKey):
    keysPressed = pygame.key.get_pressed()
    if keysPressed[inputKey]:
        return True
    else:
        return False
    
    

size = [26, 24]
show_border = [80, 80]
hero_place = [size[0] // 2, size[1] // 2]
images = []
field_width = 200
map_ = make_map(field_width, show_border, hero_place)

border_speed = [0,0]
hero_speed = [0,0]





wall_img = pygame.image.load('images/wall.png')#.resize((40, 40))
field_img = pygame.image.load('images/grass5.jpg')#.resize((40, 40))
road_img = pygame.image.load('images/road1.png')#.resize((40, 40))
rock_img = pygame.image.load('images/rock.png')#.resize((40, 40))
hero1_img = pygame.image.load('images/Рыцарь.png')#.resize((40, 40))
heroes_img = [hero1_img]
textures = [field_img, wall_img, rock_img, road_img]

hero_img = heroes_img[menu()]



window = pygame.display.set_mode((1050,768),0,0)
# window = pygame.display.set_mode((900,1600),pygame.FULLSCREEN ,0)
pygame.display.set_caption("towers and magic")
screen = pygame.Surface((1050,768))
pygame.init() 
FPS = 15
clock = pygame.time.Clock()

def buttons():
    for i in pygame.event.get():
            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_w:
                    if map_[show_border[1] + hero_place[1] - 1][show_border[0] + hero_place[0]] <= 0:
                        if show_border[1] > 0 and hero_place[1] == size[1] // 2:
                            border_speed[1] -= 1
                        else:
                            hero_speed[1] -= 1
                if i.key == pygame.K_a:
                    if map_[show_border[1] + hero_place[1]][show_border[0] + hero_place[0] - 1] <= 0:
                        if show_border[0] > 0 and hero_place[0] == size[0] // 2:
                            border_speed[0] -= 1
                        else:
                            hero_speed[0] -= 1
                if i.key == pygame.K_s:
                    if map_[show_border[1] + hero_place[1] + 1][show_border[0] + hero_place[0]] <= 0:
                        if show_border[1] < field_width - size[1] and hero_place[1] == size[1] // 2:
                            border_speed[1] += 1
                        else:
                            hero_speed[1] += 1
                if i.key == pygame.K_d:
                    if map_[show_border[1] + hero_place[1]][show_border[0] + hero_place[0] + 1] <= 0:
                        if show_border[0] < field_width - size[0] and hero_place[0] == size[0] // 2:
                            border_speed[0] += 1
                        else:
                            hero_speed[0] += 1
            elif i.type == pygame.K_UP:
                if i.key == pygame.K_w:
                    if map_[show_border[1] + hero_place[1] - 1][show_border[0] + hero_place[0]] <= 0:
                        if show_border[1] > 0 and hero_place[1] == size[1] // 2:
                            border_speed[1] = 0
                        else:
                            hero_speed[1] = 0
                if i.key == pygame.K_a:
                    if map_[show_border[1] + hero_place[1]][show_border[0] + hero_place[0] - 1] <= 0:
                        if show_border[0] > 0 and hero_place[0] == size[0] // 2:
                            border_speed[0] = 0
                        else:
                            hero_speed[0] = 0
                if i.key == pygame.K_s:
                    if map_[show_border[1] + hero_place[1] + 1][show_border[0] + hero_place[0]] <= 0:
                        if show_border[1] < field_width - size[1] and hero_place[1] == size[1] // 2:
                            border_speed[1] = 0
                        else:
                            hero_speed[1] = 0
                if i.key == pygame.K_d:
                    if map_[show_border[1] + hero_place[1]][show_border[0] + hero_place[0] + 1] <= 0:
                        if show_border[0] < field_width - size[0] and hero_place[0] == size[0] // 2:
                            border_speed[0] = 0
                        else:
                            hero_speed[0] = 0
    show_border[0], show_border[1] = border_speed[0] + show_border[0], border_speed[1] + show_border[1]
    hero_place[0], hero_place[1] = hero_speed[0] + hero_place[0], hero_speed[1] + hero_place[1]


# main loop
while 1:
    buttons()
    clock.tick(FPS)
    bgColor = (0,0,0) 
    screen.fill(bgColor) 
    if  keyPressed(pygame.K_q):
        break
    pygame.mouse.set_visible(0)
    for t in range(show_border[1], show_border[1] + size[1]):
        for g in range(show_border[0], show_border[0] + size[0]):
            if map_[t][g] == 1.1:
                prob = (map_[t + 1][g] + map_[t][g + 1] + map_[t - 1][g] + map_[t][g - 1]) * 12.5
                a = random.randint(1, 100)
                res = 0
                if prob >= 2.5 * a:
                    res = 2
                elif prob >= 1.1 * a:
                    res = 1
                map_[t][g] = res
            img = textures[map_[t][g]]
            screen.blit(img,((g - show_border[0]) * 40, (t - show_border[1]) * 40))
            
    
    screen.blit(hero_img,((g - show_border[0]) * 40, (t - show_border[1]) * 40))
    pygame.display.update()
    window.blit(screen,(0,0))
         

pygame.quit()