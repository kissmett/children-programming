# https://nostarch.com/teachkids/

import pygame
import random

pygame.init()
screen = pygame.display.set_mode([800,600])
pygame.display.set_caption("UE")
timer = pygame.time.Clock()

pic = pygame.image.load('assets_en/Clubs2.jpg')
#以下的两行是为了解决一个在某些环境中可能出现的问题:如果图像看起来像有一个黑色的边角的话，可以包含如下两行代码
pic_colorkey = pic.get_at((0,0))
pic.set_colorkey(pic_colorkey)
pic_x = 0
pic_y = 0
speed_x = 5
speed_y = 5

keep_going = True
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
radius = 50

colors = [0]*100
locations = [0]*100
sizes = [0]*100
for i in range(100):
    colors[i] = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    locations[i]=(random.randint(0,800),random.randint(0,600))
    sizes[i]=random.randint(10,100)

def DrawRandomCircles():
    for i in range(100):
        pygame.draw.circle(screen,colors[i],locations[i],sizes[i])
        new_x = locations[i][0]+1
        new_y = locations[i][1]+1
        if new_x>800:
            new_x -= 800
        if new_y>600:
            new_y -= 600
        locations[i] = (new_x,new_y)
        
while keep_going:
    screen.fill(BLACK) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            pygame.draw.circle(screen,RED,pos,50)    
    

    # pygame.draw.circle(screen,GREEN,(100,100),radius)
    DrawRandomCircles()


    pic_x += speed_x
    pic_y += speed_y
    if pic_x<=0 or pic_x>=800-pic.get_width():
        speed_x = -speed_x
    if pic_y<=0 or pic_y>=600-pic.get_height():
        speed_y = -speed_y
    screen.blit(pic,(pic_x,pic_y))
    pygame.display.update()
    timer.tick(60)

pygame.quit()            