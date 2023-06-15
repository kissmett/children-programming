class GameStats:
    '''跟踪游戏的统计信息'''

    def __init__(self, ai_game):
        '''初始化统计信息'''
        self.settings = ai_game.settings
        self.reset_stats()#在初始化的时候，开始调用重置方法
        #游戏刚启动处于不活动状态，单击Play后活跃
        self.game_active = False
        #载入历史最高分,任何情况都不重置最高得分
        self._read_high_score()
        #游戏进行标记,进入游戏时，游戏并没有运行
        self.game_running = False
                        

    def reset_stats(self):#这个重置方法包含了初始化，所以在这个类初始化的时候就执行了
        '''初始化游戏在运行起见可能变化的统计信息'''
        self.ships_left = self.settings.ship_limit#剩余飞船数量
        #得分,每次重置时都让得分为0，所以放在重置里而不是初始化里面。
        self.score = 0
        #游戏等级，也是外星人的波数
        self.level = 1
        #游戏进行标记
        self.game_running = True

    def _read_high_score(self):
        '''读取历史最高分'''
        with open(self.settings.high_score_pwd, 'r') as f:
            self.high_score = int(f.readline())

    def write_high_score(self):
        '''写入历史最高分'''
        with open(self.settings.high_score_pwd, 'w') as f:
            f.write(str(self.high_score))
