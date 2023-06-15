import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):#继承pygame精灵
    '''管理子弹的类'''
    def __init__(self, ai_game):#和飞船一样，在屏幕上绘制所以要有属性ai_game
        super().__init__()#super可以调用父类方法，super().__init__()意思是调用父类__init__()初始化方法，此时子弹拥有了父类精灵的一切属性。因为初始化是赋值属性的
        self.screen = ai_game.screen
        #self.settings = Settings()这里说一下为什么不用这个语句，因为ai_game里有settings属性，它已经实例化了所有设置参数，所以没必要再实例画一个Settings()
        self.settings = ai_game.settings
        #其实可以不用写self.speed因为settings里面已经有了，但是写出来比较好因为这样打开本文件是可以知道子弹有什么属性的！而且类似之前屏幕长宽那种情况
        self.speed = self.settings.bullet_speed
        #以下的内容是因为我们没有子弹图片需要自己绘制才写的
        self.width = self.settings.bullet_width
        self.height = self.settings.bullet_height
        self.color = self.settings.bullet_color
        #在(0,0)处创建一个表示子弹的矩形，再设置正确位置
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        #设置子弹正确位置
        self.rect.midtop = ai_game.ship.rect.midtop

        #存储用小数表示的子弹位置
        self.y = float(self.rect.y)

    def update(self):
        '''向上移动子弹'''
        #更新子弹的位置的小数值
        self.y -= self.speed
        #更新子弹的实际位置
        self.rect.y = self.y
    

    def draw_bullet(self):#这里实际上就是biltme和飞船一样，因为子弹没有图片所以是draw画
        '''在屏幕上绘制子弹'''
        pygame.draw.rect(self.screen, self.color, self.rect)
        
