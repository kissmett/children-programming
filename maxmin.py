list = [23,3,4,5,9,54,45,29,84]

max = list[0]
min = list[0]

for i in list:
    if i > max:
        max = i
    if i < min:
        min = i
        
print("max:",max)
print("min:",min)