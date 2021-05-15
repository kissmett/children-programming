import random

for i in range(1,50):
    for j in range(1,50):
        r = random.random()
        if (r>=0.5):
            print('\u2571',end='')
        else:
            print('\u2572',end='')
    #print()

