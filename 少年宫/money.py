
feedict = {}
feelist = []
while True:
    print('''
        press l to show 
        press a to add
        
    ''')
    p=input( )
    try:
        if p=='a':
            date=input('日期：')
            money=float(input('金额：'))
            notes=input('物品：')
            # feedict={'2024 03 01':20.0,}
            # feedict = {'datetime':'20l24-3-1 13:00:00' , 'fee':32.0, 'notes':'买了葡萄，香蕉'}
            feedict = {'datetime':date , 'fee':money, 'notes':notes}    
            feelist.append(feedict)        
        if p=='l':
            print('购物：',feelist)
    except ValueError:
        print('数据类型错误')






















