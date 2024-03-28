import math

global h
h = 0.00000001
eps = 0.00001
x = 0.0

def f(x):
    return (x**2 + math.sin(x/5) - 1/4)

def fp(x, k):
    if k == 0:
        return f(x)
    else:
        return (fp(x + h, k - 1) - fp(x, k - 1)) / h

while True:
    fx = f(x)
    fpx = fp(x, 1)
    xnew = x - (2.0 * fx * fpx) / (2.0 * fpx**2 - fx * fp(x, 2))

    if abs(xnew - x) <= eps:
        print(xnew)
        break

    if (xnew > 100 or xnew < 0):
        print("Out of range")
        break

    x = xnew

