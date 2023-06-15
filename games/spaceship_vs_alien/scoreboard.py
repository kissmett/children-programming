import pygame.font
from pygame.sprite import Group

from ship import Ship

class Scoreboard:
    '''显示游戏中分数的类'''

    def __init__(self, ai_game):
        '''初始化显示得分涉及的属性'''
        self.ai_game = ai_game#这是因为创建剩余飞船数显示图像时，要实例化飞船，因此要实例化游戏管理类
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        #显示得分信息时使用的字体设置
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        #准备渲染初始得分图像
        self.prep_score()
        #准备渲染最高得分图像
        self.prep_high_score()
        #准备渲染游戏等级图像
        self.prep_level()
        #准备显示剩余飞船数的图像
        self.prep_ships_left()

    def prep_score(self):
        '''将得分转换为一幅渲染的图像'''
        #将得分以,分隔千位数,并舍入得分舍个位数。
        rounded_score = round(self.stats.score, -1)
        score_str = 'current score:{:,}'.format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        #设置得分矩形位置，把得分矩形的坐标设置在右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        '''将最高得分转换为一幅渲染的图像'''
        #将最高分以,分隔千位数,并舍入得分舍个位数。
        high_score = round(self.stats.high_score, -1)
        high_score_str = 'highest score:{:,}'.format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)

        #设置最高分矩形位置，把最高分矩形的坐标设置在屏幕顶部中央
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.score_rect.top = self.score_rect.top

    def prep_level(self):
        '''将游戏等级渲染成图像'''
        level_str = f'level:{str(self.stats.level)}'
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)

        #设置等级矩形位置，把等级放在得分下面
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships_left(self):
        '''显示还剩余多少飞船'''
        ships_left_str = 'left ships:'
        self.ships_left_word = self.font.render(ships_left_str, True, self.text_color, self.settings.bg_color)#剩余飞船数的文字提示
        #设置描述矩形位置，把描述放在剩余飞船图像上面
        self.ships_left_word_rect = self.ships_left_word.get_rect()
        self.ships_left_word_rect.left = self.screen_rect.left
        self.ships_left_word_rect.top = 20
        
        self.ships = Group()#新建一个空组，来存储剩余飞船，我们只要图像
        for ship_number in range(self.stats.ships_left):
            print(self.stats.ships_left)
            ship = Ship(self.ai_game)
            #设置这些飞船绘制的位置
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 70
            self.ships.add(ship)

    def check_high_score(self):
        '''检查是否诞生了新的最高分'''
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def show_score(self):
        '''在屏幕上显示得分、最高分、游戏等级、剩余飞船数'''
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.ships_left_word, self.ships_left_word_rect)
        self.ships.draw(self.screen)
        
        
