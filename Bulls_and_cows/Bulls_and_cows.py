import random
from Bulls_and_cows_logic import get_bull_count, get_cow_count, game_over
from Bulls_and_cows_logic import generate_secret_number
f = open('results.bac','r')
lst = []
for line in f:
    lst.append(line)
    if len(lst) > 10:
        lst.pop(0)
for i in range(len(lst)):
    print(lst[i], end = '')
f.seek(0)
f.close()
print('Длина числа равна 4')
f = open('length.bac','r')
length = int(f.read())
secret_number = str(generate_secret_number(length))
chl = input("Введите свое число ")
turns = 1
while game_over(chl, secret_number) == False:
    print('Количество быков:', get_bull_count(chl, secret_number))
    print('Количество коров:', get_cow_count(chl, secret_number))
    chl = input("Введите новое число ")
    turns += 1
name = input("Ваше имя: ")
f.close()
f = open('results.bac', 'r+')
contetns = f.read()
f.write(str(name))
f.write(': ')
f.write(str(turns))
f.write('\n')
f.close()
print('Вы выиграли')
