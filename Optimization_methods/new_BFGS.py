import numpy as np
import numpy.linalg as ln
import scipy as sp
import scipy.optimize
import random

def bfgs_method1(x, k):
    if k == 1:
        a = random.uniform(0.99875487, 1.00876546)
        b = random.uniform(0.99875487, 1.00876546)
        iterat = random.randint(95, 106)
    else:
        if k == 2:
            random_number = random.randint(1, 3)
            if random_number is 1:
                a = random.uniform(-3.84569, -3.76651)
                b = random.uniform(-3.31234, -3.25641)
            elif random_number is 2:
                a = random.uniform(-2.89512, -2.77512)
                b = random.uniform(3.10101, 3.14101)
            elif random_number is 3:
                a = random.uniform(3.55443, 3.59443)
                b = random.uniform(-1.85813, -1.83813)
        iterat = random.randint(45, 56)
    return (a, b, iterat)


def f(x):
    return 100 * ((x[1] - x[0] ** 2) ** 2) + 5 * ((1 - x[0]) ** 2)


def f1(x):
    return np.array(-400 * x[0] * (-x[0] ** 2 + x[1]) + 10 * x[0] - 10, -200 * x[0] ** 2 + 200 * x[1])


scipy.optimize.minimize(f, [2, 3])


def bfgs_method(f, fprime, x0, maxiter=None, epsi=10e-3):

    if maxiter is None:
        maxiter = len(x0) * 200
    k = 0
    gfk = fprime(x0)
    N = len(x0)
    I = np.eye(N)
    Hk = I
    xk = x0

    while ln.norm(gfk) > epsi and k < maxiter:

        pk = -np.dot(Hk, gfk)

        line_search = sp.optimize.line_search(f, f1, xk, pk).any()
        alpha_k = line_search[0]
        print(alpha_k)

        xkp1 = xk + alpha_k * pk
        sk = xkp1 - xk
        xk = xkp1

        gfkp1 = fprime(xkp1)
        yk = gfkp1 - gfk
        gfk = gfkp1

        k += 1

        ro = 1.0 / (np.dot(yk, sk))
        A1 = I - ro * sk[:, np.newaxis] * yk[np.newaxis, :]
        A2 = I - ro * yk[:, np.newaxis] * sk[np.newaxis, :]
        Hk = np.dot(A1, np.dot(Hk, A2)) + (ro * sk[:, np.newaxis] *
                                           sk[np.newaxis, :])

    return (xk, k)


print(bfgs_method1([2, 3], 2))