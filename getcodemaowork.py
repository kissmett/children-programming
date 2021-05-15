import easygui

import tkinter

# answer = easygui.ynbox('是否继续？')
# print(answer)
# easygui.msgbox('Hello,%s'%answer)
import requests, webbrowser

json = requests.get('https://api-creation.codemao.cn/kitten/work/player/load/' + input('你要获取bcm文件的ID')).json()
print(json['source_urls'][0])

webbrowser.open(json['source_urls'][0])