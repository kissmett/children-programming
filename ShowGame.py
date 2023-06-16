# https://nostarch.com/teachkids/

import pygame
pygame.init()
screen = pygame.display.set_mode([800,600])
timer = pygame.time.Clock()

pic = pygame.image.load('assets_en/Clubs2.jpg')
#以下的两行是为了解决一个在某些环境中可能出现的问题:如果图像看起来像有一个黑色的边角的话，可以包含如下两行代码
pic_colorkey = pic.get_at((0,0))
pic.set_colorkey(pic_colorkey)
pic_x = 0
pic_y = 0

keep_going = True
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
radius = 50
while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
    screen.fill(BLUE)
    pygame.draw.circle(screen,GREEN,(100,100),radius)

    pic_x += 1
    pic_y += 1
    screen.blit(pic,(pic_x,pic_y))
    pygame.display.update()
    timer.tick(60)
pygame.quit()            