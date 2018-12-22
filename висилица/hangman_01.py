from hangman_new import random_word, get_guessed_word, is_word_guessed, get_available_letters
secret_word = random_word()
attempts = 10
used_letters = ''
while attempts > 0:
    print('Попыток осталось:', attempts)
    print(get_guessed_word(secret_word, used_letters))
    start_word = get_guessed_word(secret_word, used_letters)
    print('Доступные буквы:', get_available_letters(used_letters))
    if is_word_guessed(secret_word, used_letters) == True:
        print("Загаданное слово было:", secret_word)
        print('Вы выиграли')
        break
    else:
        letter = input("Буква ")
        used_letters += letter
    if is_word_guessed(secret_word, used_letters) == True:
        print("Загаданное слово было:", secret_word)
        print('Вы выиграли')
        break
    else:
        if start_word == get_guessed_word(secret_word, used_letters):
            attempts -= 1
if attempts == 0:
    print("Загаданное слово было:", secret_word)
    print('Вы проиграли')
    
        
