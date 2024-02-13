import pygame, time, random, sys

'''初始化游戏'''
pygame.init()

# 初始化游戏窗口
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('贪吃蛇小游戏')

# 定义速度
fpsclock = pygame.time.Clock()

# 定义字体
font = pygame.font.Font('C:/Windows/Fonts/msyh.ttc', 80)

# 定义颜色
red = pygame.Color(255, 0, 0)
blue = pygame.Color(0, 0, 255)
balck = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
grey = pygame.Color(130, 130, 130)

'''初始化贪吃蛇和食物'''
# 贪吃蛇的位置
snake_head = [100, 100]

# 贪吃蛇的身体
snake_body = [[80, 100], [60, 100], [40, 100]]

# 定义贪吃蛇的开始方向
direction = 'right'

# 食物标记
food_flag = 1

# 第一个食物的位置
food_position = [300, 300]


# 画出贪吃蛇
def snake(Snake_body):
    for i in Snake_body:
        pygame.draw.rect(screen, white, (i[0], i[1], 20, 20))

# 画出食物
def food(food_Position):
    pygame.draw.rect(screen, red, (food_Position[0], food_Position[1], 20, 20))

# 打印分数
def drawscore(score):
    # 设置分数的颜色
    score_surf = font.render('%s' % score, True, grey)

    # 设置分数的位置
    score_rect = score_surf.get_rect()
    score_rect.midtop = (320, 240)

    # 绑定以上句柄
    screen.blit(score_surf, score_rect)

def game_over():
    # 设置文字颜色
    game_over_surf = font.render('Game Over!', True, grey)

    # 设置文字位置
    game_over_rect = game_over_surf.get_rect()
    game_over_rect.midtop = (320, 10)

    # 绑定以上句柄
    screen.blit(game_over_surf, game_over_rect)

    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit()


while True:
    # 屏幕用黑色填充
    screen.fill(0)
    '''检测事件'''
    for event in pygame.event.get():
        # 检测退出
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # 检测按键是否按下
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'down':
                direction = 'up'

            elif event.key == pygame.K_DOWN and direction != 'up':
                direction = 'down'

            elif event.key == pygame.K_RIGHT and direction != 'left':
                direction = 'right'

            elif event.key == pygame.K_LEFT and direction != 'right':
                direction = 'left'
    '''移动贪吃蛇'''
    if direction == 'up':
        snake_head[1] -= 20

    if direction == 'down':
        snake_head[1] += 20

    if direction == 'right':
        snake_head[0] += 20

    if direction == 'left':
        snake_head[0] -= 20
   
   	# 将蛇的头部当前的位置加入到蛇身的列表中
    snake_body.insert(0, list(snake_head))

    # 判定食物是否被吃
    if snake_head[1] == food_position[1] and snake_head[0] == food_position[0]:
        food_flag = 2
    else:
        snake_body.pop()

    # 随机生成食物
    if food_flag == 2:
        x = random.randrange(1, 32)
        y = random.randrange(1, 24)
        food_position = [int(x * 20), int(y * 20)]
        food_flag = 1

    # 画出角色
    snake(snake_body)
    food(food_position)
    drawscore(len(snake_body) - 3)

    '''判定死亡'''
    # 碰到边缘
    if snake_head[0] < 0 or snake_head[0] > 620:
        game_over()

    elif snake_head[1] < 0 or snake_head[1] > 460:
        game_over()

    # 贪吃蛇碰到自己
    for i in snake_body[1:]:
        if snake_head[0] == i[0] and snake_head[1] == i[1]:
            game_over()    

    # 刷新屏幕
    pygame.display.flip()

    fpsclock.tick(10)



