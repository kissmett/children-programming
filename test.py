n = int(input("Enter a number: "))
sum_j=0
sum_y=0
sum_t=0
for i in range(n):
    j,y,t = input().split()
    j = int(j)
    y = int(y)
    t = int(t)
    sum_j = sum_j + j
    sum_y = sum_y + y
    sum_t = sum_t + t

sum_all = sum_j + sum_y + sum_t
print(sum_j,sum_y,sum_t,sum_all)
