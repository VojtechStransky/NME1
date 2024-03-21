import numpy as np

x = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
y = [60.2, 45.3, 30.5, 11.6, 5.2, 3.1, 6.8, 13.2, 32.8, 44.7, 61.5]

degree = 3

def sum(x, exp, y = None):
    r = 0

    for (z, i) in enumerate(x):
        if y == None:
            c = 1
        else:
            c = y[z]

        r += i**exp * c

    return r

def solve(x, y, degree):
    m = np.zeros((degree + 1, degree + 1))
    r = np.zeros(degree + 1)

    for i in range(degree + 1):
        z = degree

        r[i] = sum(x, i, y)

        for q in range(i + 1):
            m[z - i + q][z - q] = sum(x, (2 * z - i))
            m[i - q][q] = sum(x, i)

    return np.linalg.solve(m, r)

c = solve(x, y, degree)

print(c)

