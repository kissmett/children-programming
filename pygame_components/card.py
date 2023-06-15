import pygame
from .color import RED,BLACK,BLUE,GREEN

class Card(pygame.sprite.Sprite): 
    # 属性image/rect不可少
    def __init__(self,screen,imagefile,pos,scale,selected=False):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.filename = imagefile
        # self.pos = pos
        self.scale = scale
        self.selected = selected
        self.setImage(self.filename)
        self.setPos(pos)
        pass
    def blitme(self):
        self.screen.blit(self.image,self.rect)
        pass
    def setImage(self,filename):
        self.image = pygame.image.load(filename)
        self.image = pygame.transform.scale(self.image,
                                            (self.image.get_rect().width*self.scale,
                                             self.image.get_rect().height*self.scale)
                                             )
        self.image0 = self.image.copy()
              
    def setPos(self,pos):
        self.pos = pos
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
