def smile_logic(line):
    lst_line = list(line)
    if lst_line.count('a') != 0:
        for i in range(lst_line.count('a')):
            lst_line.remove('a')
    f_brace = 0
    f_square_bracket = 0
    f_round_bracket = 0
    f_open_brace = 0
    f_close_brace = 0
    f_open_square = 0
    f_close_square = 0
    f_open_round = 0
    f_close_round = 0
    f = 0
    f1 = 0
    for i in range(len(line)):
        if line[i] == '{':
            f_brace += 1
        if line[i] == '}':
            f_brace += -1
        if line[i] == '[':
            f_square_bracket += 1
        if line[i] == ']':
            f_square_bracket += -1
        if line[i] == '(':
            f_round_bracket += 1
        if line[i] == ')':
            f_round_bracket += -1
        if f_brace < 0 or f_square_bracket < 0 or f_round_bracket < 0:
            return False
    if f_brace != 0 or f_square_bracket != 0 or f_round_bracket != 0:
        return False
    for i in range(len(line)):
        if line[i] == '{':
            f1 += 1
        if line[i] == '}':
            f1 += 1
        if line[i] == '[':
            f1 += 1
        if line[i] == ']':
            f1 += 1
        if line[i] == '(':
            f1 += 1
        if line[i] == ')':
            f1 += 1
    if f1 == 0:
        return True
    for i in range(len(line)):
        if line[i] == '{':
            f_open_brace = i
        if line[i] == '}':
            f_close_brace = i
        if line[i] == '[':
            f_open_square = i
        if line[i] == ']':
            f_close_square = i
        if line[i] == '(':
            f_open_round = i
        if line[i] == ')':
            f_close_round = i
        if f_close_brace != 0:
            for i in range(f_open_brace, f_close_brace+1):
                if line[i] == '[' or line[i] == '(':
                    return False
            lst_line = list(line)
            for i in range(f_open_brace, f_close_brace+1):
                lst_line[i] = 'a'
            for i in range(lst_line.count('a')):
                lst_line.remove('a')
            line = ''
            for i in range(len(lst_line)):
                line += str(lst_line[i])
            for i in range(len(line)):
                if line[i] == '[' or line[i] == '{' or line[i] == '(':
                    f = f+1
            if f == 0:
                return True
            else:
                return smile_logic(line)
        if f_close_square != 0:
            for i in range(f_open_square, f_close_square+1):
                if line[i] == '{' or line[i] == '(':
                    return False
            lst_line = list(line)
            for i in range(f_open_square, f_close_square+1):
                lst_line[i] = 'a'
            for i in range(lst_line.count('a')):
                lst_line.remove('a')
            line = ''
            for i in range(len(lst_line)):
                line += str(lst_line[i])
            for i in range(len(line)):
                if line[i] == '[' or line[i] == '{' or line[i] == '(':
                    f = f+1
            if f == 0:
                return True
            else:
                return smile_logic(line)
        if f_close_round != 0:
            for i in range(f_open_round, f_close_round+1):
                if line[i] == '[' or line[i] == '{':
                    return False
            lst_line = list(line)
            for i in range(f_open_round, f_close_round+1):
                lst_line[i] = 'a'
            for i in range(lst_line.count('a')):
                lst_line.remove('a')
            line = ''
            for i in range(len(lst_line)):
                line += str(lst_line[i])
            for i in range(len(line)):
                if line[i] == '[' or line[i] == '{' or line[i] == '(':
                    f = f+1
            if f == 0:
                return True
            else:
                return smile_logic(line)
