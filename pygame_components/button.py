import pygame.font

class Button:
    '''表示按钮的类'''

    def __init__(self, screen, msg, button_color, text_color,rect):
        '''初始化按钮属性'''
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        #设置按钮的尺寸以及其他属性
        self.width, self.height = 200, 50
        self.button_color = button_color
        self.text_color = text_color
        self.font = pygame.font.SysFont(None, 48)

        #创建按钮的rect对象，并使其居中
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        # self.rect.center = self.screen_rect.center
        self.rect = rect
        
        #按钮的标签只需要创建一次
        self.prep_msg(msg)

    def prep_msg(self, msg):
        '''将标签转渲染成图像，叠放在按钮上'''
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)#把文字渲染成图像，Tue是开启反锯齿
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        '''先绘制一个按钮(由于初始化生成了按钮矩形也确定了坐标所以只要填充按钮颜色即可),再把文字图像盖上去'''
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
        
