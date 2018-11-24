T1 = int(input("Введите время заполнения шприца "))
T2 = int(input("Введите время передачи шприца "))
T3 = int(input("Введите время инъекции шприца "))
seconds = int(input("Введите время "))
T1_1 = T1
T2_1 = T2
T3_1 = T3
kol_spots = 0
kol_periods = 0
kol_sec = 0
print('1:        ', end='')
print('2:')
a = 0  # a == 0 если нет шприца у 2 наркомана и а == 1 в др случае
d = 0  # d == 0 если первая инъекция еще не введена и 1 в ином случае
for i in range(seconds):
    q = 0
    if T1_1 != 0:  # Набираем шприц
        print('N        ', end='')
        T1_1 -= 1
    else:
        if a == 1:  # Если есть шприц у наркомана 2 - ждем
            print('.        ', end='')
        else:
            if T2_1 != 0:  # Процесс передачи шприца если его нет у наркомана 2
                T2_1 -= 1
                print('p        ', end='')
            if T2_1 == 0:  # Шприц передан
                q = 1
                a = 1
                T1_1 = T1
                T2_1 = T2
                if d == 1:
                    kol_spots += 1
                print('.')
    if a == 0:
        if d == 1:
            kol_spots += 1
        print('.')
    if a == 1 and q == 0:
        if T3_1 != 0:
            T3_1 -= 1
            print('I')
        if T3_1 == 0:
            if d == 1:
                kol_sec = kol_sec + kol_spots + T3
                kol_periods += 1
                kol_spots = 0
            T3_1 = T3
            d = 1
            a = 0
            t = 0
if kol_periods != 0:
    print(kol_sec/kol_periods)
else:
    print('Нет двух концов инъекции')
