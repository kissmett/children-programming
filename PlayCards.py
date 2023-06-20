import pygame
import random
import os

from pygame import Rect

from pygame_components.button import Button
from pygame_components import Card
from pygame_components import RED,BLACK,BLUE,GREEN  

from pygame_components.card2 import Card2

pygame.init()
screen = pygame.display.set_mode([800,600])
pygame.display.set_caption("UE")
timer = pygame.time.Clock()

imagefile_list = [ f for f in os.listdir('./assets_en') if f.rfind('.jpg')>0 ]

card_list = pygame.sprite.Group()
for i in range(10):
    sprite = Card2(screen,
                  'assets_en/'+random.choice(imagefile_list),
                (random.randint(100,700),random.randint(100,500)),
                random.random(),
                selected=False
                )  
    card_list.add(sprite)

controll_list = pygame.sprite.Group()
button_test = Button(screen, 'test',button_color=BLUE,text_color=RED,rect=Rect(0,0,100,50))
card_current = Card(screen,
                    'assets_en/back.jpg',
                    (700,100),
                    1,
                    selected=True
                    )
controll_list.add(button_test)
controll_list.add(card_current)

#card2 test
card2 = Card2(screen,
                  'assets_en/back.jpg',
                (random.randint(100,700),random.randint(100,500)),
                1,
                selected=True
                )

keep_going=True        
while keep_going:
    for event in pygame.event.get():
        # 执行各sprite的事件处理方法；
        for s in card_list:
            s._check_events(event)
        card2._check_events(event)
        # 执行game中的事件处理方法；
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
                    button_test.set_msg('card clicked.',True)
                    card_current.setImage(s.filename)
            if button_test.rect.collidepoint(pos): #点击button_test
                for s in card_list:
                    if s.selected:
                        card_list.remove(s)
            if card_current.rect.collidepoint(pos):
                card_current.choose()
                button_test.set_msg('card_current clicked.',True)
    screen.fill(BLACK) 

    card2.blitme()

    card_list.update() # 调用list里每一个精灵的update()
    card_list.draw(screen)

    controll_list.update()
    controll_list.draw(screen)

    # button_test.draw_button()
    # card_current.blitme()
    # # card_current.update() #Not

    pygame.display.update() #flip()与update()有何区别--flip更新整个缓冲区，update可以更新局部rect
    timer.tick(60)

pygame.quit()    