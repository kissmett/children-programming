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
    def __init__(self,imagefile,pos,scale):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(imagefile)
        self.pos = pos
        self.scale = scale
        self.image = pygame.transform.scale(self.image,
                                            (self.image.get_rect().width*self.scale,
                                             self.image.get_rect().height*self.scale)
                                             )
        self.rect = self.image.get_rect()
        self.rect.x = self.pos[0] - self.rect.width/2
        self.rect.y = self.pos[1] - self.rect.height/2
        pass
    def update(self):
        # self.rect.x = self.pos[0] - self.rect.width/2
        # self.rect.y = self.pos[1] - self.rect.height/2
        pass

sprite_list = pygame.sprite.Group()
imagefile_list = [ f for f in os.listdir('./assets_en') if f.rfind('.jpg')>0 ]
keep_going=True        
while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            sprite = Card('assets_en/'+random.choice(imagefile_list),pos,random.random())  
            sprite_list.add(sprite)
    screen.fill(BLACK)        
    sprite_list.update()
    sprite_list.draw(screen)
    pygame.display.update()
    timer.tick(60)

pygame.quit()    