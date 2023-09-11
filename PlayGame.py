import pygame
import random
import os
import sys

from pygame import Rect

from pygame_components.button import Button
from pygame_components.card import Card
from pygame_components.color import RED,BLACK,BLUE,GREEN

from pygame_components.card2 import Card2


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode([800,600])
        pygame.display.set_caption("Play Game")
        self.timer = pygame.time.Clock()

        pass

    def _quit_game(self):
        '''退出游戏'''
        pygame.quit()  # 退出pygame。必须加上这句话，否则会因为bug而使得pygame不能退出。
        sys.exit()
    def _proc_events(self,event):
        self._proc_events_common_before(event)
        if event.type == pygame.KEYDOWN:
            self._proc_events_keydown(event)
        elif event.type == pygame.KEYMAPCHANGED:
            self._proc_events_keychanged(event)
        elif event.type == pygame.KEYUP:
            self._proc_events_keyup(event)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            self._proc_events_mousedown(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            self._proc_events_mouseup(event)
        elif event.type == pygame.MOUSEMOTION:
            self._proc_events_mousemove(event)
        elif event.type == pygame.MOUSEWHEEL:  
            self._proc_events_mousewheel(event)                   
        self._proc_events_common_after(event)
        pass 
    
    def _proc_events_keydown(self,event):
        pass
    def _proc_events_keyup(self,event):
        pass
    def _proc_events_keychanged(self,event):
        pass
    def _proc_events_mousedown(self,event):
        print('game.mousedown')
        pass
    def _proc_events_mouseup(self,event):
        pass
    def _proc_events_mousemove(self,event):
        pass
    def _proc_events_mousewheel(self,event):
        pass
    def _proc_events_common_before(self,event):
        pass    
    def _proc_events_common_after(self,event):
        pass

    def run_game(self):
        #事件循环
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._quit_game()
                self._proc_events(event)   
        pass

if __name__ == '__main__':#这句话的意思是，如果该模块作为主程序运行，则为真
    game = Game()
    game.run_game()
    