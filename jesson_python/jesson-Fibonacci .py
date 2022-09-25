# for i in[1,2,3,4,5]:
#     print(i,'jesson')
#     print(i,'谨谨')
#     print(i,'田飞')
#     print(i,'郑艳')
#     print(i,'田兆明')
#     print(i,'李洁')

# sum = 0
# for i in [2,34,5,9]:
#     sum = sum + i
# print(sum)
# sum=0
# for a in[66,99,33,55]:
#     sum=sum+a
# print(sum)
# sum=253
# for s in[299,300]:
#     sum=sum+s
# print(sum)    

import turtle
sum=1
sum1=0
sum2=1
turtle.pendown()
for i in range(13):
    sum=sum+sum1
    sum1=sum2
    sum2=sum
    print(i ,sum)          
    # draw circle
    turtle.circle(sum,90)

turtle.mainloop()    