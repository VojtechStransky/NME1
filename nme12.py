import numpy as np
import matplotlib.pyplot as plt

def function(x) :
    return 16*x**2

def derivative(x) :
    return 16*2*x

def numDerivative(x, h) :
    return (function(x + h) - function(x))/h

def findH(base) :
    error = 1.0
    h = 1.0

    while (error >= 0.1) :
        h = h * 0.99
        error = abs(((numDerivative(base, h) - derivative(base))/derivative(base)))

    return h

def findI() :
    y = np.log(11) - np.log(10)
    i = 0

    x = [i]
    v = [y]

    while (y > 0) :
        i += 1
        y = 1/i - 10 * y

        x.append(i)
        v.append(y)

    plt.yscale("log")
    plt.plot(x,v)
    plt.show()

    return i

print(findH(1))
print(findI())


