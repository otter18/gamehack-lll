import random
from menu_t_v2 import menu
from map_ import make_map
import pygame


size = [25, 13]
show_border = [88, 94]
hero_place = [size[0] // 2, size[1] // 2]
images = []
field_width = 200
map_ = make_map(field_width)
wall_img = pygame.image.load('images/wall.png')
field_img = pygame.image.load('images/grass5.jpg')
road_img = pygame.image.load('images/road1.png')
rock_img = pygame.image.load('images/rock.png')
knight_img1 = pygame.image.load('images/images/Рыцарь/Стоит.png')
knight_img2 = pygame.image.load('images/images/Рыцарь/Бежит 1.png')
knight_img3 = pygame.image.load('images/images/Рыцарь/Бежит 2.png')
knight_img4 = pygame.image.load('images/images/Рыцарь/Атака.png')
knight_img5 = pygame.image.load('images/images/Рыцарь/спец атака.png')
knight_img6 = pygame.image.load('images/images/Рыцарь/2(Стоит).png')
knight_img7 = pygame.image.load('images/images/Рыцарь/2(Бежит 1).png')
knight_img8 = pygame.image.load('images/images/Рыцарь/2(Бежит 2).png')
knight_img9 = pygame.image.load('images/images/Рыцарь/2(Атака).png')
monster1_img = pygame.image.load('images/images/лучник2.png')
tower1 = pygame.image.load('images/images/Хорошие лучники.png')
right_ = [knight_img1, knight_img2, knight_img3, knight_img1]
left_ = [knight_img6, knight_img7, knight_img8, knight_img6]
attack_right = [knight_img1, knight_img4, knight_img1]
attack_left = [knight_img6, knight_img9, knight_img6]
heroes_img = [(knight_img1, knight_img6)]
textures = [field_img, wall_img, rock_img, road_img]
qq = menu()
hero_img = heroes_img[qq][0]
knight = {'attack': 2, 'special': 4, 'hp': 6, 'hp_left': 6}
archer_tower = {'attack': 3, 'range': 3, 'hp': 3, 'hp_left': 3, 'cost': 15}
towers = []
map_[98][101] = -3
heroes = [knight]
hero = heroes[qq]
tower_counter = 0
monster1 = {'attack': 1, 'hp': 1, 'hp_left': 1, 'reward': 10}
monsters = []
map_[101][99] = 3
monster1counter = 0
money = 0

window = pygame.display.set_mode((1025, 768))
pygame.display.set_caption("towers and magic")
pygame.init()
FPS = 30
clock = pygame.time.Clock()
dir = [0, 1]

def draw_bullet(xs, ys, xf, yf):
    window.draw.line(((xs - show_border[0]) * 40, (ys - show_border[1]) * 40), ((xf - show_border[0]) * 40, (yf - show_border[1]) * 40), (214, 214, 214), 5)
    pygame.time.delay(10)


def animation(img_list, x, y):
    for i in range(len(img_list)):
        window.blit(img_list[i], (x * 40, y * 40))
        pygame.display.update()
        pygame.time.delay(40)
        window.blit(textures[map_[y + show_border[1]][x + show_border[0]]], (x * 40, y * 40))


while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        else:
            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_w:
                    animation(right_, hero_place[0], hero_place[1])
                    dir = [0, -1]
                    if -1 <= map_[show_border[1] + hero_place[1] - 1][show_border[0] + hero_place[0]] <= 0:
                        if hero_place[1] == size[1] // 2:
                            show_border[1] -= 1
                        else:
                            hero_place[1] -= 1

                if i.key == pygame.K_a:
                    animation(left_, hero_place[0], hero_place[1])
                    hero_img = heroes_img[qq][1]
                    dir = [-1, 0]
                    if -1 <= map_[show_border[1] + hero_place[1]][show_border[0] + hero_place[0] - 1] <= 0:
                        if hero_place[0] == size[0] // 2:
                            show_border[0] -= 1
                        else:
                            hero_place[0] -= 1

                if i.key == pygame.K_s:
                    animation(right_, hero_place[0], hero_place[1])
                    dir = [0, 1]
                    if -1 <= map_[show_border[1] + hero_place[1] + 1][show_border[0] + hero_place[0]] <= 0:
                        if show_border[1] < field_width - size[1] and hero_place[1] == size[1] // 2:
                            show_border[1] += 1
                        else:
                            hero_place[1] += 1

                if i.key == pygame.K_d:
                    hero_img = heroes_img[qq][0]
                    animation(right_, hero_place[0], hero_place[1])
                    dir = [1, 0]
                    if -1 <= map_[show_border[1] + hero_place[1]][show_border[0] + hero_place[0] + 1] <= 0:
                        if show_border[0] < field_width - size[0] and hero_place[0] == size[0] // 2:
                            show_border[0] += 1
                        else:
                            hero_place[0] += 1

                if i.key == pygame.K_SPACE:
                    target = map_[show_border[1] + hero_place[1] + dir[1]][show_border[0] + hero_place[0] + dir[0]]
                    if target == 1:
                        map_[show_border[1] + hero_place[1] + dir[1]][show_border[0] + hero_place[0] + dir[0]] = 0
                        if dir[0] == 1 or dir[0] == 0:
                            animation(attack_right, hero_place[0], hero_place[1])
                        else:
                            animation(attack_left, hero_place[0], hero_place[1])
                    elif target >= 3:
                        monsters[target - 3]['hp_left'] -= hero['attack']
                        if dir[0] == 1 or dir[0] == 0:
                            animation(attack_right, hero_place[0], hero_place[1])
                        else:
                            animation(attack_left, hero_place[0], hero_place[1])
                        if monsters[target - 3]['hp_left'] <= 0:
                            money += monsters[target - 3]['reward']
                            map_[show_border[1] + hero_place[1] + dir[1]][show_border[0] + hero_place[0] + dir[0]] = -1
                if i.key == pygame.K_q and tower_counter >= 120 and money >= 15 and map_[show_border[1] + hero_place[1] + dir[1]][show_border[0] + hero_place[0] + dir[0]] == 0:
                    tower_counter = 0
                    money -= 15
                    tower = archer_tower
                    tower['x'] = show_border[0] + hero_place[0] + dir[0]
                    tower['y'] = show_border[1] + hero_place[1] + dir[1]
                    towers.append(tower)
                    map_[show_border[1] + hero_place[1] + dir[1]][show_border[0] + hero_place[0] + dir[0]] = -len(towers) - 2

    tower_counter += 1
    monster1counter += 1
    if monster1counter == 15 and len(monsters) < 1000:
        monster1counter = 0
        monster = monster1
        monster['x'] = random.randint(field_width // 3 * 2, field_width - 2)
        monster['y'] = random.randint(field_width // 2 - 1, field_width // 2 + 1)
        monsters.append(monster)
        map_[monster['y']][monster['x']] = len(monsters) + 2
    for tower in towers:
        for c1 in range(tower['x'] - tower['range'], tower['x'] + tower['range'] + 1):
            for c2 in range(tower['y'] - tower['range'], tower['y'] + tower['range'] + 1):
                if map_[c2][c1] > 2:
                    draw_bullet(tower['x'], tower['y'], c1, c2)
                    monsters[map_[c2][c1] - 3]['hp_left'] -= tower['attack']
                    if monsters[map_[c2][c1] - 3]['hp_left'] <= 0:
                        money += monsters[target - 3]['reward'] // 2
                        map_[c2][c1] = -1
                        break
            break

    # monsters
    window.fill((0, 0, 0))
    for t in range(show_border[1], show_border[1] + size[1]):
        for g in range(show_border[0], show_border[0] + size[0]):
            if map_[t][g] == 1.1:
                prob = (map_[t + 1][g] + map_[t][g + 1] + map_[t - 1][g] + map_[t][g - 1])
                a = random.randint(1, 8)
                res = 0
                if prob >= 2 * a:
                    res = 2
                elif prob >= a:
                    res = 1
                map_[t][g] = res
            if t == show_border[1] + hero_place[1] and g == show_border[0] + hero_place[0]:
                window.blit(textures[map_[t][g]], ((g - show_border[0]) * 40, (t - show_border[1]) * 40))
                window.blit(hero_img, (hero_place[0] * 40, hero_place[1] * 40))
            elif map_[t][g] > 2:
                window.blit(textures[-1], ((g - show_border[0]) * 40, (t - show_border[1]) * 40))
                window.blit(monster1_img, ((g - show_border[0]) * 40, (t - show_border[1]) * 40))
            elif map_[t][g] < -2:
                window.blit(textures[0], ((g - show_border[0]) * 40, (t - show_border[1]) * 40))
                window.blit(tower1, ((g - show_border[0]) * 40, (t - show_border[1] - 1) * 40))
            else:
                window.blit(textures[map_[t][g]], ((g - show_border[0]) * 40, (t - show_border[1]) * 40))

    pygame.display.update()
    clock.tick(FPS)
