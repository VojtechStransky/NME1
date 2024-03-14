import numpy as np
import sys

m = np.array([
    [0.,-1.,3.],
    [0.,0.,2.],
    [-2.,-2.,1.]
])

def inverse(a):
    x = np.identity(3)

    for i in range(3):
        if a[i][i] == 0.0:
            for g in range(i, 3):
                if a[g][i] != 0:
                    a[[g, i]] = a[[i, g]]
                    x[[g, i]] = x[[i, g]]

            if a[i][i] == 0.0:
                sys.exit('Singular!')
                return

        for j in range(3):
            if i != j:
                ratio = a[j][i]/a[i][i]

                for k in range(3):
                    a[j][k] = a[j][k] - ratio * a[i][k]
                    x[j][k] = x[j][k] - ratio * x[i][k]

            if i == j:
                q = a[i][i]

                for k in range(3):
                    a[j][k] = a[j][k]/q
                    x[j][k] = x[j][k]/q

    return x

i = inverse(m)

print(i)

