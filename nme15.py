
import numpy as np
import sys

x = [-4, -1, 2]
y = [-28, -16, -40]

m = -0.5

def solve(x, y, m):
    if (len(x) != len(y)):
        sys.exit("Error, lengths of x and y are not same!")

    n = len(x)
    d = np.zeros([n, n], dtype = float)

    for o in reversed(range(n)):
        for p in reversed(range(o + 1)):
            b = (p - o + n - 1)
            a = p

            if (a == b):
                d[a, b] = y[a]
            else:
                d[a, b] = ((m - x[a])*d[a + 1][b] - (m - x[b])*d[a][b - 1])/(x[b] - x[a])

    return d[0, n - 1]

i = solve(x, y, m)

print(i)


