import pygame
import random
import os

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)

pygame.init()
screen = pygame.display.set_mode([800,600])
pygame.display.set_caption("UE")
timer = pygame.time.Clock()

class Card(pygame.sprite.Sprite): 
    # 属性image/rect不可少
    def __init__(self,imagefile,pos,scale,selected=False):
        pygame.sprite.Sprite.__init__(self)
        self.filename = imagefile
        self.pos = pos
        self.scale = scale
        self.selected = selected
        self.image = pygame.image.load(self.filename)
        self.image = pygame.transform.scale(self.image,
                                            (self.image.get_rect().width*self.scale,
                                             self.image.get_rect().height*self.scale)
                                             )
        self.image0 = self.image.copy()
        self.rect = self.image.get_rect()
        self.rect.x = self.pos[0] - self.rect.width/2
        self.rect.y = self.pos[1] - self.rect.height/2
        pass
    def update(self):
        # print(self.filename,'.update()')
        # self.rect.x = self.pos[0] - self.rect.width/2
        # self.rect.y = self.pos[1] - self.rect.height/2
        if self.selected:
            # pygame.draw.rect(self.image,RED,self.rect)
            # pygame.draw.rect(self.image,RED,(),20)
            pygame.draw.circle(self.image,RED,
                               (self.rect.width-10*self.scale,10*self.scale),
                               10*self.scale) #OK, draw a circle on the image from topright
            # pygame.draw.circle(screen,RED,
            #                    (self.rect.x+self.rect.width-10*self.scale,
            #                     self.rect.y+10*self.scale),
            #                    10*self.scale) #Not
        
        pass
    def choose(self):
        if self.selected:
            self.selected = False
            self.image = self.image0.copy()
        else:
            self.selected = True

imagefile_list = [ f for f in os.listdir('./assets_en') if f.rfind('.jpg')>0 ]

sprite_list = pygame.sprite.Group()
for i in range(10):
    sprite = Card('assets_en/'+random.choice(imagefile_list),
                          (random.randint(100,700),random.randint(100,500)),
                          random.random(),
                          selected=False
                          )  
    sprite_list.add(sprite)

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
            # sprite_list.add(sprite)
            for s in sprite_list:
                if s.rect.collidepoint(pos):
                    s.choose()

    screen.fill(BLACK)        
    sprite_list.update() # 调用list里每一个精灵的update()
    sprite_list.draw(screen)
    pygame.display.update()
    timer.tick(60)

pygame.quit()    