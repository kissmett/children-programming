print("my name is:{}, i'm {} years old.".format('Jesson',9))
print("my name is:{name}, i'm {age} years old.".format(name='Jesson',age=9))
print("my name is:{name}, i'm {age} years old.".format(age=9,name='Jesson'))
#  字面量
print('---------------1')
data = {
    'tableName':'person information',
    'data':[
        {'name':'Jesson','age':9},
        {'name':'George','age':6},
        {'name':'Field Tian','age':44},
        {'name':'Amy','age':44},
    ]
}
print(data['data'][2]['name'][6:])
print(data['data'][2]['name'][6:-1])
# print(data['data'][2]['name'][6:0:-1])
print('---------------2')
s = '0123456789'
print(s[1:3])
print(s[1:7:2])
print(s[-1])
print(s[::-1])
'''ooooooooooooooooooooooooooooooohhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
aaaaaaaaaaaaaaaaaaaaaaaaaaaahhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
gggggggggggggggggggggggggggggggggggggeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee'''

s = '0 1 2 3 4 5'
s1 = s.split()
print(s1)
s = '0,1,2,3,4,5'
s1 = s.split(',')
print(s1)
s2 = s.replace(',',',,')
print(s2)
try:
    print(s2.index('2-'))
except Exception as e:
    print('------------[{}]------------'.format(e))
