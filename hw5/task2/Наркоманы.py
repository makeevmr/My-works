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
a = False  # a False если нет шприца у 2 наркомана и а True в др случае
d = False  # d False если первая инъекция еще не введена и True в ином случае
for i in range(seconds):
    flag = False
    if T1_1 != 0:  # Набираем шприц
        print('N        ', end='')
        T1_1 -= 1
    else:
        if a is True:  # Если есть шприц у наркомана 2 - ждем
            print('.        ', end='')
        else:
            if T2_1 != 0:  # Процесс передачи шприца если его нет у наркомана 2
                T2_1 -= 1
                print('p        ', end='')
            if T2_1 == 0:  # Шприц передан
                flag = True
                a = True
                T1_1 = T1
                T2_1 = T2
                if d is True:
                    kol_spots += 1
                print('.')
    if a is False:
        if d is True:
            kol_spots += 1
        print('.')
    if a is True and flag is False:
        if T3_1 != 0:
            T3_1 -= 1
            print('I')
        if T3_1 == 0:
            if d is True:
                kol_sec = kol_sec + kol_spots + T3
                kol_periods += 1
                kol_spots = 0
            T3_1 = T3
            d = True
            a = False
if kol_periods != 0:
    print(kol_sec/kol_periods)
else:
    print('Нет двух концов инъекции')
