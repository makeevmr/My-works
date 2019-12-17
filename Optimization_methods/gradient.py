from sympy import *
EPC = 0.00001
DELTA = 0.000004
EPC_1 = 0.01
iterations = 0


def func_1(x):
    return 100 * ((x[1] - x[0] ** 2) ** 2) + 5 * ((1 - x[0]) ** 2)


def func_2(x):
    return (x[0] ** 2 + x[1] - 11) ** 2 + (x[0] + x[1] ** 2 - 7) ** 2


def func_1a(a, start_x, start_y):
    x = [start_x - a * (diff(func_1(x0), x0[0]).subs({x0[0]: start_x, x0[1]: start_y})),
         start_y - a * (diff(func_1(x0), x0[1]).subs({x0[0]: start_x, x0[1]: start_y}))]
    return x


def func_2a(a, start_x, start_y):
    x = [start_x - a * (diff(func_2(x0), x0[0]).subs({x0[0]: start_x, x0[1]: start_y})),
         start_y - a * (diff(func_2(x0), x0[1]).subs({x0[0]: start_x, x0[1]: start_y}))]
    return x


def dichotomy_func(a, b, start_x, start_y, func_number):
    x_k = (a + b) / 2 - DELTA
    y_k = (a + b) / 2 + DELTA
    if func_number == 1:
        if func_1(func_1a(x_k, start_x, start_y)) <= func_1(func_1a(y_k, start_x, start_y)):
            b = y_k
        else:
            a = x_k
    if func_number == 2:
        if func_2(func_2a(x_k, start_x, start_y)) <= func_2(func_2a(y_k, start_x, start_y)):
            b = y_k
        else:
            a = x_k
    if b - a < EPC:
        return (a + b) / 2
    return dichotomy_func(a, b, start_x, start_y, func_number)


def gradient_method(start_x, start_y, func_number):
    global x0
    global iterations
    iterations += 1
    x0 = [start_x, start_y]
    x0[0], x0[1] = symbols('x0[0] x0[1]')
    if func_number == 1:
        dfx0 = diff(func_1(x0), x0[0]) + diff(func_1(x0), x0[1])
    else:
        if func_number == 2:
            dfx0 = diff(func_1(x0), x0[0]) + diff(func_1(x0), x0[1])
        else:
            return "Введён номер функции, которой нет в базе"
    if abs(dfx0.subs({x0[0]: start_x, x0[1]: start_y})) < 0.001:
        return start_x, start_y
    a = dichotomy_func(0, 10, start_x, start_y, func_number)
    if func_number == 1:
        new_x0 = [start_x - a * (diff(func_1(x0), x0[0]).subs({x0[0]: start_x, x0[1]: start_y})),
                  start_y - a * (diff(func_1(x0), x0[1]).subs({x0[0]: start_x, x0[1]: start_y}))]
        max_lst = [sqrt((new_x0[0] - start_x) ** 2 + (new_x0[1] - start_y) ** 2), abs(func_1(new_x0) - func_1([start_x, start_y])),
                   sqrt((diff(func_1(x0), x0[0]).subs({x0[0]: new_x0[0], x0[1]: new_x0[1]})) ** 2
                        + (diff(func_1(x0), x0[1]).subs({x0[0]: new_x0[0], x0[1]: new_x0[1]})) ** 2)]
    else:
        new_x0 = [start_x - a * (diff(func_2(x0), x0[0]).subs({x0[0]: start_x, x0[1]: start_y})),
                  start_y - a * (diff(func_2(x0), x0[1]).subs({x0[0]: start_x, x0[1]: start_y}))]
        max_lst = [sqrt((new_x0[0] - start_x) ** 2 + (new_x0[1] - start_y) ** 2),
                   abs(func_2(new_x0) - func_2([start_x, start_y])),
                   sqrt((diff(func_2(x0), x0[0]).subs({x0[0]: new_x0[0], x0[1]: new_x0[1]})) ** 2
                        + (diff(func_2(x0), x0[1]).subs({x0[0]: new_x0[0], x0[1]: new_x0[1]})) ** 2)]
    if max(max_lst) < EPC_1:
        return new_x0[0], new_x0[1], iterations
    else:
        return gradient_method(new_x0[0], new_x0[1], func_number)


#  print(gradient_method(21, 45, 1))
print(gradient_method(0, 0, 2))