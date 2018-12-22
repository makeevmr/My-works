from random import randint

def random_word():
    lst_words = ['pounds', 'cost', 'main', 'road', 'forever', 'letter', 'company', 'sky']
    secret_word = lst_words[randint(0, len(lst_words) - 1)]
    return secret_word

def get_guessed_word(secret_word, used_letters):
    lst_secret_word = list(secret_word)
    lst_used_letters = list(used_letters)
    lst_guessed_word = []
    guessed_word = ''
    for i in range(len(secret_word)-1):
        lst_guessed_word.append('_')
        lst_guessed_word.append(' ')
    lst_guessed_word.append('_')
    for i in range(len(used_letters)):
        for n in range(len(secret_word)):
            if 65 <= ord(lst_used_letters[i]) <= 90 or 97 <= ord(lst_used_letters[i]) <= 122:
                if ord(lst_used_letters[i]) == ord(lst_secret_word[n]) or ord(lst_used_letters[i]) == ord(lst_secret_word[n]) + 32 or ord(lst_used_letters[i]) == ord(lst_secret_word[n]) - 32:
                    lst_guessed_word[2*n] = lst_secret_word[n]
    for i in range(len(lst_guessed_word)):
        guessed_word += lst_guessed_word[i]
    return guessed_word
                    
def is_word_guessed(secret_word, used_letters):
    for i in range(len(get_guessed_word(secret_word, used_letters))):
        if get_guessed_word(secret_word, used_letters)[i] == '_':
                   return False
    return True

def get_available_letters(used_letters):
    str_a = 'abcdefghijklmnopqrstuvwxyz'
    lst_str_a = list(str_a)
    new_str = ''
    for i in range(len(used_letters)):
        for n in range(len(str_a)):
            if lst_str_a[n] == used_letters[i]:
                lst_str_a[n] = '!'
    for i in range(len(used_letters)):
        lst_str_a.remove('!')
    for i in range(len(lst_str_a)):
        new_str += lst_str_a[i]
    return new_str
        
        
