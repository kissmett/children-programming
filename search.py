'''
{'家具':[,,,],'食物':[]}
key:分类
value：具体的东西
'''

family_things = {}
while True:
    cmd=input('请输入如下指令:\na:加入物品\nd:删除物品\nl:列出当前物品\nq:退出\n')
    if cmd == 'q':
        print('bye~')
        break
    if cmd == 'l':
        print('当前物品有：'+ str(family_things))
        continue
    if cmd=='a':
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
            

