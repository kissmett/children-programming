v = "a.v"

import b
# from b import v 
from b import v as bv
def func1():
    v = "a.func1.v"
    print(v)

def func2():
    print(v)

def func3():
    print(b.v)

func1()
func2()
func3()