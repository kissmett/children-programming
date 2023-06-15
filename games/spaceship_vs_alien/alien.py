import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    '''表示单个外星人的类'''
    
    def __init__(self, ai_game):
        '''初始化外星人并设置初始位置'''
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #加载外星人图片并设置rect矩形
        self.image = pygame.image.load(self.settings.alien_image).convert_alpha()
        self.rect = self.image.get_rect()#其实这个已经包含了self.position包含width\height\x\y等属性

        #设置外星人初始位置
        self.rect.x = 0#self.rect.width 书上写得是这个代码但实际上这样外星人并不显示在左上角，如果（0，0）才是左上角
        self.rect.y = 0#self.rect.height
        #存储外星人的精确水平位置
        self.x = float(self.rect.x)

    def update(self):
        '''向左或向右移动外星人'''
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        '''检查外星人是不是触碰到边缘'''
        #首先获取屏幕矩形
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= screen_rect.left:
            return True#如果碰到屏幕边界，则返回真
