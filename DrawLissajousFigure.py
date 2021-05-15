import matplotlib.pyplot as plt
import numpy as np

def Lissajous_Figure():
    X=np.linspace(-np.pi,np.pi,256,endpoint=True) #-π to+π的256个值
    # print(X)
    C,S=np.cos(7*X),np.sin(5*X)
    # plt.plot(X,C)
    # plt.plot(X,S)
    plt.plot(C,S)
    #在ipython的交互环境中需要这句话才能显示出来
    plt.show()

def Lissajous_Figure_dyn():
    i = 0
    while True:
        plt.cla()
        i = i + 0.1
        X=np.linspace(-np.pi,np.pi,256,endpoint=True) #-π to+π的256个值
        C,S=np.cos(7*X+i),np.sin(5*X)
        plt.plot(C,S)
        plt.pause(0.1)

if __name__ == '__main__':
    Lissajous_Figure_dyn()
    # Lissajous_Figure()