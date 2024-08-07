'''
{'家具':[,,,],'食物':[]}
key:分类
value:具体的东西
'''
import json


family_things = {}
def save():
    content = json.dumps(family_things)
    f = open('family-things.json','wt+')
    f.write(content)
    f.close()

def load():
    global family_things
    f = open('family-things.json','+rt')
    content = f.read()
    family_things = json.loads(content)
    f.close()
def sum_array(arr):
    s = 0
    for i in arr:
        try:
            i = int(i)
        except:
            i = 0
        s = s + i
    return s    
def sum_all():
    d = {}
    for k in family_things.keys():
        arr = family_things[k]
        s = sum_array(arr)
        d[k] = s
    print('各分类的得分：',d)    

    

while True:
    cmd=input('----------\n请输入如下指令:\na:加入物品\nd:删除物品\nl:列出当前物品\nh:求和\ns:保存\no:加载\nq:退出\n----------\n')
    if cmd == 'q':
        print('bye~')
        break
    if cmd == 'l':
        print('当前物品有：'+ str(family_things))
        continue
    if cmd=='a.v1':
        #列出现有分类
        #问询用户是否添加新分类 y/n
            #若是y则提示用户输入分类名字
                #用户输入名字，系统添加新类别，退出主循环 continue；
            #若是n则让用户选择分类添加物品,
                #提示用户输入分类的名字，
                #提示用户输入具体物品,
                #在该分类下保存物品，并退出主循环continue
        print('现有分类：'+ str(list(family_things.keys())))
        newcls = input('是否添加新分类 y/n')
        if newcls =='y':
            classname = input('输入分类名字')
            if classname not in family_things.keys():
                family_things[classname] = []
                print('{0}新类别已添加')
            else:
                print('{0}已存在，请勿重复添加'.format(classname))
            continue            
        if newcls =='n':
            classname = input('选择分类添加物品')
            if classname in family_things.keys():
                thing = input('输入具体物品')
                if thing == '':
                    print('输入物品名称不能为空，本次添加无效')
                if thing not in family_things[classname]:
                    family_things[classname].append(thing)
                    print('物品添加成功')
                else:
                    print('物品已存在，本次添加无效')                   
            else:
                print('{0}不存在，本次操作无效'.format(classname))
            continue    
        continue
    if cmd=='a':
        print('现有分类：'+ str(list(family_things.keys())))
        classname = input('输入分类名字：')
        classname = classname.strip()
        if classname == '':
            print('分类名称不能为空')
            continue
        if classname not in family_things.keys():
            family_things[classname] = []
            print('[{0}]新类别已添加'.format(classname))
        else:
            print('[{0}]已存在，已切换至该分类'.format(classname))
        thing = input('输入具体物品：') 
        thing = thing.strip() #去掉首尾空格
        if thing == '':
            print('输入物品名称不能为空，本次添加无效')
            continue        
        family_things[classname].append(thing)            
        print('物品添加成功')           
    if cmd=='d':
        print('当前物品有：'+ str(family_things))
        删除类别=input('请选择一个要操作的分类：')
        if 删除类别 not in(family_things.keys()):
            print ('没有当前类别，此次操作无效')
            continue
        操作= int(input('您是要删除该分类（按1）还是该分类下的物品（按2）？'))
        if 操作==1:
            del family_things[删除类别]
            print('已完成')
            continue
        # ------------------------------- #
        删除物品=input('请选择一个要操作的物品：')
        if 删除物品 not in family_things[删除类别]:
            print ('该类别下没有当前物品，此次操作无效')
            continue
        family_things[删除类别].remove(删除物品)
    if cmd=='s':
        save()
        print('保存成功')
        continue
    if cmd=='o':
        load()
        print('加载完成')
        continue
    if cmd=='h':
        sum_all()
        continue
            

