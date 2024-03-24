# -*- coding: utf-8 -*- 
import pygame
if __name__ =='__main__':
    from color import RED,BLACK,BLUE,GREEN
else:
    from .color import RED,BLACK,BLUE,GREEN
# from .color import RED,BLACK,BLUE,GREEN

class Card(pygame.sprite.Sprite): 
    # 属性image/rect不可少
    def __init__(self,screen,imagefile,pos,scale,selected=False):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.filename = imagefile        
        self.scale = scale
        self.selected = selected
        self.mousedown = False

        self._setImage(self.filename)
        self.setPos(pos) #需要基于image scale来设置position，所以此行要放setImage后面；
        self._makeChooseFlag()
        self._setChooseFlag()

        pass
    def blitme(self):
        self._setChooseFlag()
        self.screen.blit(self.image,self.rect)
        pass
    def _makeChooseFlag(self):
        self.font = pygame.font.SysFont(None, 20)
        self.msg_image = self.font.render("X", True, BLACK, RED)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = (self.rect.width-10*self.scale,10*self.scale)
        pass
    def _setChooseFlag(self):
        if self.selected:
            pygame.draw.circle(self.image,RED,
                               (self.rect.width-10*self.scale,10*self.scale),
                               10*self.scale) #OK, draw a circle on the image from topright
            
            self.image.blit(self.msg_image,self.msg_image_rect)
        pass
    def setImage(self,filename):
        self._setImage(filename)
        self._setChooseFlag()
        pass
    def _setImage(self,filename):
        print('card.setImage()',self.filename,self.selected)
        self.image = pygame.image.load(filename)
        self.image = pygame.transform.scale(self.image,
                                            (self.image.get_rect().width*self.scale,
                                             self.image.get_rect().height*self.scale)
                                             )
        self.image0 = self.image.copy() #存放原始图像

        pass      
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
        # if self.selected:
        #     # pygame.draw.rect(self.image,RED,self.rect)
        #     # pygame.draw.rect(self.image,RED,(),20)
        #     pygame.draw.circle(self.image,RED,
        #                        (self.rect.width-10*self.scale,10*self.scale),
        #                        10*self.scale) #OK, draw a circle on the image from topright
            
        #     self.image.blit(self.msg_image,self.msg_image_rect)
        #     # pygame.draw.circle(screen,RED,
        #     #                    (self.rect.x+self.rect.width-10*self.scale,
        #     #                     self.rect.y+10*self.scale),
        #     #                    10*self.scale) #Not
        
        pass
    def choose(self):
        print('card.choose()',self.filename,self.selected)
        if self.selected:
            self.selected = False
            self.image = self.image0.copy()
        else:
            self.selected = True
            # 在self.image上画圆和文字
            self._setChooseFlag()
    
    #支持拖动
    def _check_events(self, event):        
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            if self.rect.collidepoint(pos):
                self.mousedown = True
        if event.type == pygame.MOUSEBUTTONUP:
            self.mousedown = False
        if event.type == pygame.MOUSEMOTION:
            pos = event.pos
            if self.mousedown:
                self.setPos(pos)          
        pass

if __name__ == '__main__':
    print('card.main.')
