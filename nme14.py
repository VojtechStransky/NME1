import numpy as np
import sys

m = np.array([
    [2., 1., -2., -1.],
    [1., -1., -1., 1.],
    [4., 2., 2., 1.],
    [8., 1., 1., 2.]
])

def determinant(a, s):
    r = 1.0

    for i in range(s):
        if a[i][i] == 0.0:
            for g in range(i, s):
                if a[g][i] != 0:
                    a[[g, i]] = a[[i, g]]

            if a[i][i] == 0.0:
                return 0

        for j in range(s):
            if i != j:
                ratio = a[j][i]/a[i][i]

                for k in range(s):
                    a[j][k] = a[j][k] - ratio * a[i][k]

            if i == j:
                r *= a[j][i]

    return r

def detCofac(a, s):
    r = 0
    a1 = np.delete(a, 0, 0)

    if s == 1:
        return a[0][0]

    for i in range(s):
        k = (-1)**(i) * a[0][i]

        if k == 0:
            continue

        a2 = np.delete(a1, i, 1)
        k *= detCofac(a2, s - 1)
        r += k

    return r

det1 = determinant(m, 4)
det2 = detCofac(m, 4)

print("diagonal:")
print(det1)

print("\ncofac:")
print(det2)

print("\nnp:")
print(np.linalg.det(m))

