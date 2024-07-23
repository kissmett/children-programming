# -*- coding: utf-8 -*-
import random

def guess_the_number():
    print(u"欢迎参加猜数字游戏！")
    secret_number = random.randint(1, 100)  # 生成1到100之间的随机数

    attempts = 0
    while True:
        user_guess = int(raw_input(u"请猜一个1到100之间的数字："))
        attempts += 1

        if user_guess == secret_number:
            print(u"恭喜你猜对了！你用了%d次尝试。" % attempts)
            break
        elif user_guess < secret_number:
            print(u"太小了，请再试一次。")
        else:
            print(u"太大了，请再试一次。")

if __name__ == "__main__":
    guess_the_number()
