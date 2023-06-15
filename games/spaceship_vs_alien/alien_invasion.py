import sys

import pygame

from pygame.locals import *

from settings import Settings#从settings.py中导入Settings类

from ship import Ship

from bullet import Bullet

from alien import Alien

from game_stats import GameStats

from button import Button

from scoreboard import Scoreboard

from time import sleep

class AlienInvasion:
    '''管理游戏资源和行为的类'''

    def __init__(self):
        '''初始化游戏并创建游戏资源'''
        pygame.init()#pygame初始化

        self.settings = Settings()#实例化游戏参数
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))#游戏资源：屏幕。并创建一个显示窗口，返回一个surface对象，游戏中的一切绘制在这个surface上。
        pygame.display.set_caption(self.settings.caption)#游戏标题

        #实例化飞船 这里要注意一定要加上self因为飞船有输入属性ai_game这个ai_game就是AlienInvasion自己
        self.ship = Ship(self)

        #创建一个用于存储游戏统计信息的实例
        self.stats = GameStats(self)

        #创建记分牌
        self.sb = Scoreboard(self)

        #创建一个按钮实例,Play按钮
        self.play_button = Button(self, 'Play', self.settings.button_color, self.settings.play_button_text_color)

        #创建一个按钮实例，Pausing。这个按钮只是用来显示，并不会响应
        self.pausing_button = Button(self, 'pausing', self.settings.button_color, self.settings.pausing_button_text_color)

        #创建一个按钮实例，Game over。这个按钮只是用来显示，并不会响应
        self.game_over_button = Button(self, 'Game Over', self.settings.button_color, self.settings.game_over_button_text_color)
        
        #子弹在屏幕上会有很多很多，所以编组来管理，同理敌军飞机也会编组来管理
        self.bullets = pygame.sprite.Group()
        
        #外星人在屏幕上会有很多很多，所以编组来管理
        self.aliens = pygame.sprite.Group()

        #初始化创建外星人舰队
        self._create_fleet()


    def run_game(self):
        '''开始游戏的主循环'''
        while True:

            #监视键盘和鼠标事件
            self._check_events()

            if self.stats.game_active:

                #更新飞船位置#绘制飞船在更新屏幕里
                self.ship.update()

                #更新子弹
                self._update_bullets()

                #更新外星人
                self._update_aliens()
            
            #更新屏幕
            self._update_screen()

            #如果game_over则暂停游戏一段时间
            self._game_over_sleep()
            
            

    def _quit_game(self):
        '''退出游戏'''
        self.stats.write_high_score()#保存游戏历史最高分
        pygame.quit()  # 退出pygame。必须加上这句话，否则会因为bug而使得pygame不能退出。
        sys.exit()
            
    def _check_events(self):
        '''响应按键和鼠标事件'''
        for event in pygame.event.get():#事件循环
            if event.type == pygame.QUIT:
                self._quit_game()
            elif event.type == pygame.KEYDOWN:#如果事件是按下键盘
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:#如果事件是松开键盘
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:#如果事件是按下鼠标
                #首先确定鼠标的位置
                mouse_pos = pygame.mouse.get_pos()
                #判断鼠标是不是在Play按钮上
                self._check_play_button(mouse_pos)
                
    def _check_keydown_events(self, event):#注意这个有传参了，其实很容易想到要有传参
        '''响应按下'''
        if event.key == pygame.K_RIGHT:#如果按下的是键盘右移动键
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:#如果按下的是键盘左移动
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:#如果按下的是键盘上移动键
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:#如果按下的是键盘下移动键
            self.ship.moving_down = True
        elif event.key == pygame.K_ESCAPE:#如果按下的是Esc退出游戏
            self._quit_game()
        elif event.key == pygame.K_o:#如果按下的是o,切换成全屏
            self._change_full_screen()
        elif event.key == pygame.K_SPACE:#如果按下的是空格,发射一颗子弹
            self._fire_bullet()
        elif event.key == pygame.K_p:#如果按下的是P键,暂停/恢复游戏
            self._pause_begin()
            
         

    def _check_keyup_events(self, event):#注意这个有传参了，其实很容易想到要有传参
        '''响应松开'''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:#如果松开的是键盘左移动键
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:#如果松开的是键盘上移动键
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:#如果松开的是键盘下移动键
            self.ship.moving_down = False
            

    def _check_play_button(self, mouse_pos):
        '''检查是否按下Play按钮并作出响应,开始游戏'''
        if self.play_button.rect.collidepoint(mouse_pos) and not self.stats.game_active and not self.stats.game_running:
            #重置游戏统计信息
            self.stats.reset_stats()
            self.stats.game_active = True#游戏进入活跃状态

            #删除子弹和外星人
            self.bullets.empty()
            self.aliens.empty()

            #创建一群新的外星人并让飞船回到起始位置
            self._create_fleet()
            self.ship.reset_pos()

            #游戏开始隐藏鼠标
            pygame.mouse.set_visible(False)

            #重置游戏速度，分数
            self.settings.initialize_dynamic_settings()

            #重新渲染游戏记分牌
            self.sb.prep_score()

            #重新渲染游戏等级记分牌
            self.sb.prep_level()

            #重新准备剩余飞船记分牌
            self.sb.prep_ships_left()
        
    def _change_full_screen(self):
        '''切换全屏/小窗口'''
        #这同样是一个开关类操作，所以方式和移动一样，引入一个全屏标志
        if self.settings.full_screen:
            self.settings.screen_width, self.settings.screen_height = self.settings.screen_init_width, self.settings.screen_init_height
            self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
            self.settings.full_screen = False#开关切换
        else:
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            self.settings.screen_width, self.settings.screen_height = self.screen.get_rect().width, self.screen.get_rect().height
            self.settings.full_screen = True#开关切换

    def _fire_bullet(self):
        '''开火：创建一颗子弹'''
        #注意这里并不应该包含子弹位置更新和子弹绘制，子弹绘制和更新是连续的，但开火创建子弹是不连续的
        if len(self.bullets) < self.settings.bullets_num_allowed:#判断时，不用引入新的设置参数，直接用子弹组长度表示当前屏幕的子弹数目
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _pause_begin(self):
        '''暂停/开始游戏'''
        if self.stats.game_running:#如果游戏在进行，P键才有效
            if self.stats.game_active:
                self.stats.game_active = False
            else:
                self.stats.game_active = True
    
    def _delete_death_bullet(self):
        '''删除已经消失超过屏幕死亡的子弹'''
        for bullet in self.bullets.copy():#这里的.copy()是因为python特性
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
                    
    def _update_bullets(self):
        '''更新子弹的位置并删除消失子弹'''
        #更新子弹组里所有子弹的位置#绘制子弹在更新屏幕里
        self.bullets.update()
        #删除消失的子弹
        self._delete_death_bullet()
        #检测是否有子弹击中外星人,同时删除所有被击中的外星人还有子弹，在有外星人死掉后，判断如果外星人舰队为空，则生成一队新的外星人
        self._check_bullet_alien_collisions()

    def _update_aliens(self):
        '''更新外星人'''
        self._check_fleet_edges()#检测外星人群里是否有外星人碰到边缘
        self.aliens.update()
        #判断有没有外星人和飞船相撞
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        #判断有没有外星人触碰底部
        self._check_aliens_bottom()

    def _ship_hit(self):
        '''飞船被撞击后发生的事'''
        if self.stats.ships_left > 1:
            #统计信息里，飞船剩余数量减1
            self.stats.ships_left -= 1
            #重新准备剩余飞船记分牌
            self.sb.prep_ships_left()

            #清空剩下的子弹和外星人
            self.bullets.empty()
            self.aliens.empty()

            #创建一批新的外星人
            self._create_fleet()
        
            #将飞船放回初始位置。这显然不是一个事件，而是一个飞船自己的方法！
            self.ship.reset_pos()

            #暂停，让玩家察觉飞船被撞
            sleep(self.settings.ship_hit_sleep_time)

        else:
            #统计信息里，飞船剩余数量减1
            self.stats.ships_left -= 1
            #重新准备剩余飞船记分牌
            self.sb.prep_ships_left()
            self.stats.game_active = False
            self.stats.game_running = False#剩余飞船用完，游戏不运行
            pygame.mouse.set_visible(True)#显示鼠标
            

    def _game_over_sleep(self):
        '''当game over时游戏暂停一段时间'''
        if self.stats.ships_left == 0:
            self.stats.ships_left -= 1#必须让它不在是0否则程序将无法运行，因为你没有机会点击Play
            sleep(self.settings.game_over_sleep_time)
        
        
    def _create_fleet(self):
        '''创建外星人群'''
        alien = Alien(self)#创建一个外星人,这个外星人实例化只是为了让下2行代码可用，所以这个外星人不进入组
        #计算每行可容纳多少个外星人
        available_space_x = self.settings.screen_width - (2 * alien.rect.width)
        number_aliens_x = available_space_x // (2 * alien.rect.width)
        #计算每列可容纳多少个外星人
        available_space_y = self.settings.screen_height - 3 * alien.rect.height - self.ship.rect.height 
        number_aliens_y = available_space_y // (2 * alien.rect.height)

        #创建外星人
        for alien_number_x in range(number_aliens_x):
            for alien_number_y in range(number_aliens_y):
                self._create_alien(alien_number_x, alien_number_y)
            

    def _create_alien(self, alien_number_x, alien_number_y):
        '''实例化一个外星人，并且修改其初始坐标,放在当前行'''
        #因为要确定坐标，所以需要一个传参alien_number
        alien = Alien(self)
        #要对每一个外星人都设置初始坐标，不然所有外星人会叠在一起
        alien.x = alien.rect.width + 2 * alien.rect.width * alien_number_x#含小数的坐标
        alien.rect.x = alien.x#矩形坐标自动四舍五入
        alien.y = alien.rect.height + 2 * alien.rect.height * alien_number_y#含小数的坐标
        alien.rect.y = alien.y#矩形坐标自动四舍五入
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        '''有外星人到达边缘时改变外星人移动方向'''
        for alien in self.aliens.sprites():
            if alien.check_edges():
                #改变整个舰队的方向反转标志
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        '''先让每个外星人向下，在反转方向'''
        for alien in self.aliens.sprites():#每个外星人向下移动
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1#妙啊！这种切换方式好！

    def _check_bullet_alien_collisions(self):
        '''响应外星人和子弹碰撞同时删除发生碰撞的2者，如果舰队没了，则生成一组新的舰队'''
        #检测是否有子弹击中外星人,同时删除所有被击中的外星人还有子弹
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        #如果有子弹撞到外星人，并杀死了外星人，则得分增加分数
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
                self.sb.prep_score()#更新计分牌
                self.sb.check_high_score()#当有外星人被消灭，检查当前得分，以确定是否更新最高得分
        #在有外星人死掉后，判断如果外星人舰队为空，则生成一队新的外星人
        if not self.aliens:
            self.bullets.empty()#因为所有外星人意思所以清空所有子弹
            self._create_fleet()#生成外星人舰队
            self.settings.increase_speed()#提高外星人飞船子弹速度

            #提高游戏等级（显示）
            self.stats.level += 1
            self.sb.prep_level()#重新渲染等级牌
            
    def _check_aliens_bottom(self):
        '''检查是否有外星人到达了屏幕底端'''
        #先获取屏幕矩形
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                #像飞船被撞到一样处理
                self._ship_hit()
                break

    
            
    def _update_screen(self):
        '''更新屏幕上的图像，并切换到屏幕'''
        #每次循环时都重新绘制
        self.screen.fill(self.settings.bg_color)#颜色填充整个屏幕

        #绘制飞船
        self.ship.blitme()

        #绘制子弹
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        #绘制外星人
        self.aliens.draw(self.screen)

        #绘制Play按钮，如果游戏处于非活跃状态且游戏还未运行过则绘制按钮
        if not self.stats.game_active and not self.stats.game_running:
            self.play_button.draw_button()

        #绘制Pausing按钮，如果游戏处于非活跃状态且游戏正在运行则绘制按钮
        if not self.stats.game_active and  self.stats.game_running:
            self.pausing_button.draw_button()

        #绘制记分牌，显示得分
        self.sb.show_score()

        #绘制game_over按钮
        if self.stats.ships_left == 0:
            self.game_over_button.draw_button()


        #让最近绘制的屏幕可见
        pygame.display.flip()

        
        
        

if __name__ == '__main__':#这句话的意思是，如果该模块作为主程序运行，则为真
    #创建游戏实例并运行
    ai = AlienInvasion()
    ai.run_game()
    
