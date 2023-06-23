a = 3
b = 6
if a > b:
    print("前者大") 
else:
    print("后者大")       

gender = input("please input your gender(male/female):")
age = int(input("please input your age(integer):"))
print(gender,age)   
print(type(age))
if gender == 'male':
    print("男性")
    if age >=18:
        print("你是成年男性")
    else:
        print("你是未成年男性")    
else:
    print("女性")  
    if age >=60:
        print("你是老年女性")
    elif age >=18:
        print("你是成年女性")
    else:
        print("你是未成年女性") 