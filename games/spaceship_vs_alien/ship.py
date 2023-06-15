import pygame

from pygame.sprite import Sprite


class Ship(Sprite):
    '''管理飞船的类，注意这显然会是玩家、敌方飞船的父类(但是最初，可以不把它当成父类，最后再对代码进行重构变成父类即可)'''

    def __init__(self, ai_game):#这里解释一下为什么会有ai_game因为pygame机制问题,pygame所有的子surface都会在主surface，也就是游戏资源屏幕上绘制，所以飞船必须有管理游戏资源类这个属性
        '''初始化飞船并设置其位置'''
        super().__init__()
        self.settings = ai_game.settings
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()#获得屏幕的外接矩形，这有好处，因为可以调用一些屏幕外接矩形的属性，好用

        #加载飞船图像并获得其外接矩形
        self.image = pygame.image.load(self.settings.ship_image).convert_alpha()
        self.rect = self.image.get_rect()#其实这个已经包含了self.position

        #注意实际上可以设置一个属性self.position = self.settings.ship_init_pos的但是由于飞船是矩形，可以用边长的位置确定飞船位置，所以先不用这种方法，因为rect对象自带确定位置的方法！！！！
        #用rect对象自带属性，确定飞船位置
        self.rect.midbottom = self.screen_rect.midbottom

        #f飞船移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def reset_pos(self):
        '''重新设置飞船位置，让飞船回到初始位置'''
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    #飞船会出现在屏幕上，所以绘制飞船是飞船自己的方法，而不是管理游戏初始化和资源类的方法
    def blitme(self):
        '''在指定位置绘制飞船'''
        self.screen.blit(self.image, self.rect)#self.rect就是指定位置！

    #首先，飞船移动是飞船自己的方法。怎么实现移动，其实是改变位置，在blitme。我们要编写改变位置的方法
    def update(self):#其实我觉得更应该叫move，但是书上是update也行，更新位置嘛
        '''调整飞船的位置'''
        
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.ship_right_speed#这条语句就是改变位置，别忘了外接矩形
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.rect.x -= self.settings.ship_left_speed#这条语句就是改变位置，别忘了外接矩形
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.rect.y -= self.settings.ship_up_speed#这条语句就是改变位置，别忘了外接矩形
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += self.settings.ship_down_speed#这条语句就是改变位置，别忘了外接矩形
        
