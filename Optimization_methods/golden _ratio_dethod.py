from math import exp, sqrt


def f_func(x):
    a_f = 27
    b_f = 211
    return a_f * x + b_f / exp(x)


EPC = 0.00001
k = 0
PHI = (1 + sqrt(5))/2


def golden_ratio_func(a, b):
    global PHI
    global k
    x = b - (b - a)/PHI
    y = a + (b - a)/PHI
    if f_func(x) >= f_func(y):
        a = x
    else:
        b = y
    k += 1
    if b - a < EPC:
        return (a + b)/2, k
    return golden_ratio_func(a, b)


print(golden_ratio_func(-5, 5))
