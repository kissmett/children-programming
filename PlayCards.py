import pygame
import random
import os

from pygame import Rect

from pygame_components.button import Button
from pygame_components.card import Card
from pygame_components.color import RED,BLACK,BLUE,GREEN



pygame.init()
screen = pygame.display.set_mode([800,600])
pygame.display.set_caption("UE")
timer = pygame.time.Clock()

imagefile_list = [ f for f in os.listdir('./assets_en') if f.rfind('.jpg')>0 ]

card_list = pygame.sprite.Group()
for i in range(10):
    sprite = Card(screen,
                  'assets_en/'+random.choice(imagefile_list),
                (random.randint(100,700),random.randint(100,500)),
                random.random(),
                selected=False
                )  
    card_list.add(sprite)

button_test = Button(screen, 'test',BLUE,RED,Rect(0,0,100,50))
card_current = Card(screen,
                    'assets_en/back.jpg',
                    (700,100),
                    1,
                    selected=True
                    )
# card_list.add(card_current)


keep_going=True        
while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            # sprite = Card('assets_en/'+random.choice(imagefile_list),
            #               pos,
            #               random.random(),
            #               True
            #               )  
            # card_list.add(sprite)
            for s in card_list:
                if s.rect.collidepoint(pos):
                    s.choose()
                    card_current.image = s.image.copy()
            if button_test.rect.collidepoint(pos): #点击button_test
                for s in card_list:
                    if s.selected:
                        card_list.remove(s)

    screen.fill(BLACK) 
    card_list.update() # 调用list里每一个精灵的update()
    card_list.draw(screen)

    button_test.draw_button()
    card_current.blitme()

    # card_current.update()

    pygame.display.update() #flip()与update()有何区别--flip更新整个缓冲区，update可以更新局部rect
    timer.tick(60)

pygame.quit()    