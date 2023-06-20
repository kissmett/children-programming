import pygame

if __name__=='__main__':
    from card import Card
    from color import RED
else:
    from .card import Card   
    from .color import RED

class Card2(Card):
    # def __init(self,screen,imagefile,pos,scale,selected=False):
    #     # Card(self,screen,imagefile,pos,scale,selected)
    #     pass
    
    def _check_events(self, event):
        super()._check_events(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:#如果按下的是键盘右移动键
                self.rect.x += 10
            elif event.key == pygame.K_LEFT:#如果按下的是键盘左移动
                self.rect.x += -10
            elif event.key == pygame.K_UP:#如果按下的是键盘上移动键
                self.rect.y += -10
            elif event.key == pygame.K_DOWN:#如果按下的是键盘下移动键
                self.rect.y += 10
        pass

    def blitme(self):
        super().blitme()
        pygame.draw.circle(self.image,RED,
                               (10*self.scale,10*self.scale),
                               10*self.scale)