import random


def get_bull_count(chl, secret_number):
    lst2 = list(secret_number)
    lst1 = list(chl)
    k = 0
    b = len(chl)
    for f in range(b):
        if lst1[f] == lst2[f]:
            k = k+1
    return k


def get_cow_count(chl, secret_number):
    lst2 = list(secret_number)
    lst1 = list(chl)
    k = 0
    b = len(chl)
    for f in range(b):
        for n in range(b):
            if lst1[f] == lst2[n]:
                k = k+1
    return k


def generate_secret_number(length):
    secret_number_lst = random.sample([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], length)
    secret_numb = ''
    for i in range(len(secret_number_lst)):
        secret_numb += str(secret_number_lst[i])
    return secret_numb


def game_over(chl, secret_number):
    if chl == secret_number:
        return True
    else:
        return False
