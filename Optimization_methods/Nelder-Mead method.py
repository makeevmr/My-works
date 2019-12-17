def func_1(x):
    return 100 * ((x[1] - x[0] ** 2) ** 2) + 5 * ((1 - x[0]) ** 2)


def func_2(x):
    return (x[0] ** 2 + x[1] - 11) ** 2 + (x[0] + x[1] ** 2 - 7) ** 2


def nelder_mead(x_1, x_2, x_3, func_number):
    iterations = 0
    while iterations < 100:
        if func_number == 1:
            dct_func = {func_1(x_1): x_1, func_1(x_2): x_2, func_1(x_3): x_3}
            lst = [func_1(x_1), func_1(x_2), func_1(x_3)]
        else:
            if func_number == 2:
                dct_func = {func_2(x_1): x_1, func_2(x_2): x_2, func_2(x_3): x_3}
                lst = [func_2(x_1), func_2(x_2), func_2(x_3)]
            else:
                return "Введён номер функции, которой нет в базе"
        lst.sort()
        b = dct_func.get(lst[0])
        g = dct_func.get(lst[1])
        w = dct_func.get(lst[2])
        # print(func_1(b), func_1(g), func_1(w))
        mid = [(b[0] + g[0]) / 2, (b[1] + g[1]) / 2]
        x_r = [2 * mid[0] - w[0], 2 * mid[1] - w[1]]
        if func_number == 1:
            if func_1(x_r) < func_1(g):
                w = x_r
            else:
                if func_1(x_r) < func_1(w):
                    w = x_r
                c = [0.5 * mid[0] + 0.5 * w[0], 0.5 * mid[1] + 0.5 * w[1]]
                if func_1(c) < func_1(w):
                    w = c
            if func_1(x_r) < func_1(b):
                x_e = [2 * x_r[0] - mid[0], 2 * x_r[1] - mid[1]]
                if func_1(x_e) < func_1(x_r):
                    w = x_e
                else:
                    w = x_r
            if func_1(x_r) > func_1(g):
                x_c = [0.5 * mid[0] + 0.5 * w[0], 0.5 * mid[1] + 0.5 * w[1]]
                if func_1(x_c) < func_1(w):
                    w = x_c
        if func_number == 2:
            if func_2(x_r) < func_2(g):
                w = x_r
            else:
                if func_2(x_r) < func_2(w):
                    w = x_r
                c = [0.5 * mid[0] + 0.5 * w[0], 0.5 * mid[1] + 0.5 * w[1]]
                if func_2(c) < func_2(w):
                    w = c
            if func_2(x_r) < func_2(b):
                x_e = [2 * x_r[0] - mid[0], 2 * x_r[1] - mid[1]]
                if func_2(x_e) < func_2(x_r):
                    w = x_e
                else:
                    w = x_r
            if func_2(x_r) > func_2(g):
                x_c = [0.5 * mid[0] + 0.5 * w[0], 0.5 * mid[1] + 0.5 * w[1]]
                if func_2(x_c) < func_2(w):
                    w = x_c
        x_1 = b
        x_2 = g
        x_3 = w
        iterations += 1
    return b

print(nelder_mead([14, 3], [5, 2], [11, 8], 1))
print(nelder_mead([0, 0], [1, 0], [0, 1], 1))
print(nelder_mead([1, 0], [-1, 2], [2, 1], 1))
print(nelder_mead([3, 3], [1, 2], [1, 0], 2))
print(nelder_mead([2, 2], [0, 1], [0, -1], 2))
print(nelder_mead([-5, -5], [-7, -6], [-7, -8], 2))
