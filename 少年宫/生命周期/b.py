v='b.v'

def to_upper(s):
    return s.upper()
def positive(x):
    return x>0

if __name__ == '__main__':
    a = ['aaa','bbb','c']
    b = list(map(to_upper, a))
    print(b)

    c=[-3,4,5,-6]
    d=list(filter(positive,c)) # positive for non-negative numbers, negative for negative numbers, and zero for zero-length lists/arrays.
    print(d)