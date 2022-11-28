'''
https://www.jb51.net/article/206578.htm
'''
from functools import partial

import colorama; # pip install colorama
colorama.init(autoreset=True)

class Style:
 DEFAULT = 0
 BOLD= 1
 ITALIC = 3
 UNDERLINE = 4
 ANTIWHITE = 7


class Color:
 DEFAULT = 39
 BLACK = 30
 RED = 31
 GREEN = 32
 YELLOW = 33
 BLUE = 34
 PURPLE = 35
 CYAN = 36
 WHITE = 37
 LIGHTBLACK_EX = 90
 LIGHTRED_EX = 91
 LIGHTGREEN_EX = 92
 LIGHTYELLOW_EX = 93
 LIGHTBLUE_EX = 94
 LIGHTMAGENTA_EX = 95
 LIGHTCYAN_EX = 96
 LIGHTWHITE_EX = 97


class BGColor:
 DEFAULT = 49
 BLACK = 40
 RED = 41
 GREEN = 42
 YELLOW = 43
 BLUE = 44
 PURPLE = 45
 CYAN = 46
 WHITE = 47
 LIGHTBLACK_EX = 100
 LIGHTRED_EX = 101
 LIGHTGREEN_EX = 102
 LIGHTYELLOW_EX = 103
 LIGHTBLUE_EX = 104
 LIGHTMAGENTA_EX = 105
 LIGHTCYAN_EX = 106
 LIGHTWHITE_EX = 107


def out(content, color=Color.DEFAULT, bgcolor=BGColor.DEFAULT, style=Style.DEFAULT):
 print("\033[{};{};{}m{}\033[0m".format(style, color, bgcolor, content))


red = partial(out, color=Color.RED)
green = partial(out, color=Color.GREEN)
blue = partial(out, color=Color.BLUE)
yellow = partial(out, color=Color.YELLOW)
bold = partial(out, style=Style.BOLD)
underline = partial(out, style=Style.UNDERLINE)
italic = partial(out, style=Style.ITALIC)