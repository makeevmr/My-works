from math import exp


def f_func(x):
    a_f = 27
    b_f = 211
    return a_f * x + b_f / exp(x)


EPC = 0.00001
DELTA = 0.000004
k = 0


def dichotomy_func(a, b):
    global k
    x_k = (a + b) / 2 - DELTA
    y_k = (a + b) / 2 + DELTA
    if f_func(x_k) <= f_func(y_k):
        b = y_k
    else:
        a = x_k
    k += 1
    if b - a < EPC:
        return (a + b) / 2, k
    return dichotomy_func(a, b)


print(dichotomy_func(-5, 5))
