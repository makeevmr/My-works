def poly_logic(line):
    line_number = '0123456789'
    lst_numb = list(line_number)
    lst = []
    new_line = ''
    for i in range(len(line)):
        if lst_numb.count(line[i]) != 0:
            new_line += line[i]
        if lst_numb.count(line[i]) == 0 and len(new_line) != 0:
            lst.append(new_line)
            new_line = ''
        if lst_numb.count(line[i]) == 0 and len(new_line) == 0:
            lst.append(line[i])
        if i == len(line)-1 and new_line != '':
            lst.append(new_line)
    for i in range(len(lst)):
        if lst[i] == ' ':
            lst[i] = 'a'
    for i in range(lst.count('a')):
        lst.remove('a')

    def zero_degree_of(lst):  # избавление от x^0
        for i in range(len(lst)):
            if lst[i] == '0' and i != 0:
                if lst[i-1] == '^':
                    if i-2 == 0:
                        lst[i-2] = '1'
                        lst[i-1] = 'a'
                        lst[i] = 'a'
                    else:
                        if lst[i-3] == '+' or lst[i-3] == '-':
                            lst[i-2] = '1'
                            lst[i-1] = 'a'
                            lst[i] = 'a'
                        else:
                            lst[i-2] = 'a'
                            lst[i-1] = 'a'
                            lst[i] = 'a'
        for i in range(lst.count('a')):
            lst.remove('a')
        return lst
    lst = zero_degree_of(lst)
    for i in range(len(lst)):
        if lst[i] == '0':
            if i+1 <= len(lst)-1:
                if lst[i+1] == 'x':
                    if i+2 <= len(lst) - 1:
                        if lst[i+2] != '^':
                            lst[i] = 'a'
                            lst[i+1] = 'a'
                            if i != 0:
                                lst[i-1] = 'a'
    for i in range(lst.count('a')):
            lst.remove('a')
    for i in range(len(lst)):  # избавление от свободых коэфицентов
        if i == 0 and i == len(lst)-1:
            if lst[i] != 'x':
                lst[i] = 'a'
        else:
            lst_1 = list(lst[i])
            if i == 0:
                if lst_numb.count(lst_1[0]) != 0:
                    if lst[i+1] != 'x':
                        lst[i] = 'a'
            else:
                if i == len(lst)-1:
                    lst_1 = list(lst[i])
                    if lst_numb.count(lst_1[0]) != 0:
                        if lst[i-1] != '^':
                            lst[i] = 'a'
                            lst[i-1] = 'a'
                else:
                    if lst_numb.count(lst_1[0]) != 0 and lst[i+1] != 'x':
                        if lst[i-1] != '^':
                            lst[i] = 'a'
                            lst[i-1] = 'a'
    for i in range(lst.count('a')):
        lst.remove('a')
    if len(lst) > 0:
        if lst[0] == '+':
            lst[0] = 'a'
            lst.remove('a')
    for i in range(len(lst)):  # преобразуем x в первой степени
        if i == 0 and i == len(lst)-1:
            if lst[i] == 'x':
                lst[i] = '1'
        else:
            if i == 0:
                if lst[i] == 'x':
                    if lst[i+1] != '^':
                        lst[i] = '1'
            else:
                if i == len(lst)-1:
                    if lst[i] == 'x':
                        if lst[i-1] == '+' or lst[i-1] == '-':
                            lst[i] = '1'
                        else:
                            lst[i] = 'a'
                else:
                    if lst[i] == 'x':
                        if lst[i+1] != '^':
                            if lst[i-1] == '+' or lst[i-1] == '-':
                                lst[i] = '1'
                            else:
                                lst[i] = 'a'
    for i in range(lst.count('a')):
        lst.remove('a')
    lst_degree_of = []
    for i in range(len(lst)):  # проверка коэфицента 0
        if lst[i] == '0':
            if i+1 < len(lst)-1:
                if lst[i+1] == 'x':
                    if i+2 < len(lst)-1:
                        if lst[i+2] == '^':
                            if i == 0:
                                lst[i] = 'a'
                                lst[i+1] = 'a'
                                lst[i+2] = 'a'
                                lst[i+3] = 'a'
                            else:
                                lst[i] = 'a'
                                lst[i+1] = 'a'
                                lst[i+2] = 'a'
                                lst[i+3] = 'a'
                                lst[i-1] = 'a'
                        else:
                            if i == 0:
                                lst[i] = 'a'
                                lst[i+1] = 'a'
                            else:
                                lst[i] = 'a'
                                lst[i+1] = 'a'
                                lst[i-1] = 'a'
                    else:
                        if i == 0:
                            lst[i] = 'a'
                            lst[i+1] = 'a'
                        else:
                            lst[i] = 'a'
                            lst[i+1] = 'a'
                            lst[i-1] = 'a'
    for i in range(lst.count('a')):
        lst.remove('a')
    if len(lst) > 0:
        if lst[0] == '+':
            del lst[0]
    for i in range(len(lst)):  # уменьшаем степеь
        if lst[i] == '^':
            if int(lst[i+1]) > 1:
                lst_degree_of.append(lst[i+1])
            lst[i+1] = str(int(lst[i+1])-1)
    lst = zero_degree_of(lst)
    c = len(lst)
    for i in range(c):  # вставляем число степени в коэфицент
        if lst[i] == 'x':
            if i == 0:
                lst[i] = 'b'
                lst.insert(0, lst_degree_of[0])
                del lst_degree_of[0]
                c = c+1
            else:
                if lst[i-1] == '+' or lst[i-1] == '-':
                    lst[i] = 'b'
                    lst.insert(i, lst_degree_of[0])
                    del lst_degree_of[0]
                    c = c+1
                else:
                    lst[i] = 'b'
                    k = ((int(lst[i-1]))*int(lst_degree_of[0]))
                    lst[i-1] = str(k)
                    del lst_degree_of[0]
    for i in range(len(lst)):
        if lst[i] == 'b':
            lst[i] = 'x'
    for i in range(len(lst)):
        if lst[i] == '^':
            if lst[i+1] == '1':
                lst[i] = 'a'
                lst[i+1] = 'a'
    for i in range(lst.count('a')):
        lst.remove('a')
    string = ''
    for i in range(len(lst)):
        string = string + str(lst[i])
    return string
