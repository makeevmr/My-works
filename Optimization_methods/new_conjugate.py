from sympy import *
EPC = 0.00001
DELTA = 0.000004
EPC_1 = 0.001
k = 0


def func_1(x):
    return 100 * ((x[1] - x[0] ** 2) ** 2) + 5 * ((1 - x[0]) ** 2)


def func_2(x):
    return (x[0] ** 2 + x[1] - 11) ** 2 + (x[0] + x[1] ** 2 - 7) ** 2


def func_1a(a, start_x, start_y):
    x, y = symbols('x y')
    if k == 0:
        z = [start_x - a * d0[0], start_y - a * d0[1]]
    else:
        z = [start_x - a * dk[0], start_y - a * dk[1]]
    return z


def dichotomy_func(a, b, start_x, start_y, func_number):
    x_k = (a + b) / 2 - DELTA
    y_k = (a + b) / 2 + DELTA
    if func_number == 1:
        if func_1(func_1a(x_k, start_x, start_y)) <= func_1(func_1a(y_k, start_x, start_y)):
            b = (a + b) / 2
        else:
            a = (a + b) / 2
    else:
        if func_number == 2:
            if func_2(func_1a(x_k, start_x, start_y)) <= func_2(func_1a(y_k, start_x, start_y)):
                b = y_k
            else:
                a = x_k
    if b - a < EPC:
        return (a + b) / 2
    return dichotomy_func(a, b, start_x, start_y, func_number)


def conjugate_gradients(start_x, start_y, func_number):
    global k
    global dk
    global d0
    x, y = symbols('x y')
    if func_number == 1:
        df_list = [diff(func_1([x, y]), x), diff(func_1([x, y]), y)]
        print(df_list)
    else:
        if func_number == 2:
            df_list = [diff(func_2([x, y]), x), diff(func_2([x, y]), y)]
        else:
            return "Введен номер функции которой нет  в базе"
    df_xk = [df_list[0].subs({x: start_x, y: start_y}), df_list[1].subs({x: start_x, y: start_y})]
    while sqrt(df_xk[0] ** 2 + df_xk[1] ** 2) >= EPC_1:
        if k == 0:
            d0 = df_xk
            ak = dichotomy_func(0, 10, start_x, start_y, func_number)
            new_x = [start_x - ak * d0[0], start_y - ak * d0[1]]
            df_xk = [df_list[0].subs({x: new_x[0], y: new_x[1]}), df_list[1].subs({x: new_x[0], y: new_x[1]})]
        else:
            new_norm = (df_list[0].subs({x: new_x[0], y: new_x[1]})) ** 2 + \
                       (df_list[1].subs({x: new_x[0], y: new_x[1]})) ** 2
            norm = (df_list[0].subs({x: start_x, y: start_y})) ** 2 + \
                        (df_list[1].subs({x: start_x, y: start_y})) ** 2
            bk = new_norm / norm
            dk = [df_list[0].subs({x: new_x[0], y: new_x[1]}) + bk * df_list[0].subs({x: start_x, y: start_y}),
                  df_list[1].subs({x: new_x[0], y: new_x[1]}) + bk * df_list[1].subs({x: start_x, y: start_y})]
            ak = dichotomy_func(0, 10, new_x[0], new_x[1], func_number)
            start_x = new_x[0]
            start_y = new_x[1]
            new_x = [new_x[0] - ak * dk[0], new_x[1] - ak * dk[1]]
            df_xk = [df_list[0].subs({x: new_x[0], y: new_x[1]}), df_list[1].subs({x: new_x[0], y: new_x[1]})]
        k += 1
        print(new_x[0], new_x[1], func_1(new_x))
    return new_x[0], new_x[1], k, func_2(new_x)


#  print(conjugate_gradients(0, 0, 1))
print(conjugate_gradients(0, 0, 2))
#  print(conjugate_gradients(-141, 124, 2))
