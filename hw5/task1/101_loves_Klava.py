from random import randint
pro_pic_line = 11  # Вероятность вывода пикап-лайна
one_test_time = 17  # Время одного тестирования (в минутах)
working_hours = 1.5  # Время работы Клавы (в часах)
numb_of_sim = 1000  # Количество симуляций


def klava_tests():
        kol_Klava_tests = (working_hours*60)//one_test_time
        kol_Klava_tests = int(kol_Klava_tests)
        for i in range(kol_Klava_tests):
            rnd = randint(1, 100)
            if 0 <= rnd <= pro_pic_line:
                return True
        return False


str_numb = str(numb_of_sim)
length = len(str_numb)
numb_meetings_with_Konst = 0  # Количество встреч с Константином
for p in range(numb_of_sim):
    if klava_tests() is True:
        print('L', end='')
    else:
        rnd_k = randint(1, 100)
        if 0 <= rnd_k <= pro_pic_line:
            print('S', end='')
            numb_meetings_with_Konst = numb_meetings_with_Konst + 1
        else:
            print('F', end='')
print('')
print('Отношение количесвта "S" симуляций к их числу (в процентах): ', end='')
print(f'%.{length-2}f' % ((numb_meetings_with_Konst/numb_of_sim)*100))
