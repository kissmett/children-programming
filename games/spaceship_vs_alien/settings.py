class Settings:
    '''存储游戏外星人入侵中所有设置的类'''

    def __init__(self):
        '''初始化游戏设置'''
        #游戏资源
        self.screen_init_width = 1200#因为要实现全屏切换引入的常量
        self.screen_init_height = 800#因为要实现全屏切换引入的常量
        self.screen_width = self.screen_init_width
        self.screen_height = self.screen_init_height
        self.caption = '外星人入侵'
        self.bg_color = (230, 230, 230)
        self.white = (255, 255, 255)
        self.full_screen = False#设置是否是全屏

        #游戏暂停时间
        self.ship_hit_sleep_time = 0.5
        self.game_over_sleep_time = 5
        
        #飞船设置
        self.ship_image = 'games\\spaceship_vs_alien\\picture\\飞船\\飞船平时状态.png'
        self.ship_limit = 3 

        #子弹设置
        self.bullets_num_allowed = 3
        #以下是绘制子弹，但是可以加载图片代替self.bullet_image = 'picture\\飞船\\飞船平时状态.jpg'
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)

        #外星人设置
        self.alien_image = 'games\\spaceship_vs_alien\\picture\\怪物\\怪物平时状态.png'
        self.speedup_scale = 1.1#每次外星人速度的增长倍数
        self.score_scale = 1.5#外星人分数的提高

        self.initialize_dynamic_settings()

        #最高分的存储文件
        self.high_score_pwd = 'games\\spaceship_vs_alien\\game_stats\\high_score.txt'

        #按钮设置
        self.play_button_text_color = (255, 255, 255)
        self.pausing_button_text_color = (255, 255, 255)
        self.game_over_button_text_color = (255, 0, 0)
        self.button_color = (0, 255, 0)

    def initialize_dynamic_settings(self):
        '''初始化随游戏进行而变化的设置'''
        #飞船移速
        self.ship_right_speed = 1
        self.ship_left_speed = 1
        self.ship_up_speed = 1
        self.ship_down_speed = 1

        #子弹速度
        self.bullet_speed = 1.0

        #外星人速度
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10#当有外星人撞到屏幕外星人群向下移动
        self.fleet_direction = 1#为1时，向右移动；为-1时，向左移动

        #消灭外星人得到的分数
        self.alien_points = 50

    def increase_speed(self):
        '''提高速度设置和得分设置'''
        #飞船速度提升
        self.ship_right_speed *= self.speedup_scale
        self.ship_left_speed *= self.speedup_scale
        self.ship_up_speed *= self.speedup_scale
        self.ship_down_speed *= self.speedup_scale

        #子弹速度提升
        self.bullet_speed *= self.speedup_scale

        #外星人速度提升
        self.alien_speed *= self.speedup_scale

        #击杀外星人得分设置
        self.alien_points = int(self.alien_points * self.score_scale)
