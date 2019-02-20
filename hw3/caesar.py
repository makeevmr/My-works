from caesar_logic import decrypt, encrypt
print('Введите e если вы хотите зашифровать текст')
print('Введите d если вы хотите расшифровать текст')
a = input()
if a != 'e' and a != 'd':
    print(ValueError('Введено значение, не соответствующее условию'))
else:
    if a == 'e':
        text = input("Введите текст, который нужно зашифровать ")
    else:
        text = input("Введите текст, который нужно расшифровать ")
    print('Введите смещение(целое число)')
    offset = int(input())
    if offset <= -26 or offset >= 26:
        print(ValueError('Введенное смещение больше допустимого'))
    else:
        if a == 'e':
            print(encrypt(offset, text))
        else:
            print(decrypt(offset, text))
