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

while keep_going:
    # screen.fill(BLACK) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            pygame.draw.circle(screen,RED,pos,50)  


   
    pygame.display.update()


pygame.quit()            