import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['text.usetex'] = True

def factorial(n):
    i = 1

    for y in range(n):
        i *= (y + 1)

    return i

def euler(n):
    i = 0

    for y in range(n):
        i += 1/factorial(y)

    return i

def calcSourface(x, y, f, t):
    i = 0

    for n in range(f, t):
        i += ((x[n + 1] - x[n]) * y[n])

    return i

x = np.linspace(0.1, 5, 500)
y = 1/x

print(calcSourface(x, y, 92, 267))

plt.plot(x,y)
plt.xlabel(r'$x$', fontsize = 16)
plt.ylabel(r'$\frac{1}{x}$', rotation = 0, fontsize = 16)
plt.title('NME graf', fontsize = 24)
plt.show()

