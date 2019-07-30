import numpy as np

def h(x):
    return x*x*x + 2*x*x +3*x + 4

def h1(x):
    return 3*x*x + 4*x + 3

def h2(x):
    return 6*x + 4



def hh(x):
    return np.exp(x) + 2*x*x + 3*x

def hh1(x):
    return np.exp(x) + 4*x + 3

def hh2(x):
    return np.exp(x) + 4

xk = -30
k = 1
y = 0
e = 0.0001
times = 10

while k < times:
    y = hh(xk)
    print(str(xk) + "\t" + str(y))
    a = hh1(xk)
    b = hh2(xk)
    # xk -= y/a   # 用于求h(x) = 0的方程根的任务中更新xk
    xk -= a/b   # 用于求h(x)极值的任务中更新xk
    k += 1
print("====================")
print("k = ", k)
print("x = ", xk)
print("y = ", hh(xk))
