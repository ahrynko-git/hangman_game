from random import choice
from os import system

tries = 7

with open('words.txt', 'r') as file:
    words = file.read().splitlines()
file.close()


def draw_header():
    print('\n\33[34m\u2554' + '\u2550' * 30 + '\u2557\n' + '\u2551\33[0m' + ' ' * 7 + '\33[91mH A N G M A N\33[0m' +
          ' ' * 10 + '\33[34m\u2551\n' + '\u255A' + '\u2550' * 30 + '\u255D\n\33[0m')


def draw_hangman(tries_left):
    head, l_hand, r_hand, body, low_body, l_foot, r_foot = '', '', '', '', '', '', ''
    print('\n')
    if tries_left == 8:
        head, l_hand, r_hand, body, low_body, l_foot, r_foot = '😃', '/', '\\', '|', '|', '/', '\\'
    if tries_left == 7:
        head = '😀'
    if tries_left == 6:
        head, body = '☺️', ' |'
    if tries_left == 5:
        head, body, l_hand = '😉', '|', '/'
    if tries_left == 4:
        head, body, l_hand, r_hand, low_body = '🙂', '|', '/', '\\', '|'
    if tries_left == 3:
        head, body, l_hand, r_hand, low_body, l_foot = '🤨', '|', '/', '\\', '|', '/'
    if tries_left == 2:
        head, body, l_hand, r_hand, low_body, l_foot, r_foot = '😒', '|', '/', '\\', '|', '/', '\\'
    if tries_left == 1:
        head, body, l_hand, r_hand, low_body, l_foot, r_foot = '😱', '|', '/', '\\', '|', '/', '\\'
    if tries_left == 0:
        head, body, l_hand, r_hand, low_body, l_foot, r_foot = '😭', '|', '/', '\\', '|', '/', '\\'

    hangman = (' ' * 20 + '\u250F' + '\u2501' * 4 + '\u2513\n' + ' ' * 20 + '\u2503' + ' ' * 4 + '\33[5m' + head +
               '\33[0m' + '\n' + ' ' * 20 + '\u2503' + ' ' * 3 + l_hand + body + r_hand + '\n' + ' ' * 20 + '\u2503' +
               ' ' * 4 + low_body + '\n' + ' ' * 20 + '\u2503' + ' ' * 3 + l_foot + ' ' + r_foot + '\n' + ' ' * 19 +
               '\u2501' + '\u253B' + '\u2501')
    print(hangman)


def play_game(tries_left):
    letters = "`- "
    difficulty_level = input('Please choose difficulty level \33[102m\33[5m1\33[0m or \33[101m\33[5m2\33[0m: ')
    random_word = choice(words)
    if difficulty_level == '1':
        while len(random_word) > 5:
            random_word = choice(words)
    if difficulty_level == '2':
        while len(random_word) < 8:
            random_word = choice(words)
    while tries_left:
        system('clear'), draw_header()
        print('Tries left: %s/7' % tries_left,  (tries_left - 1) * '❤️ ' + '\33[5m❤️\33[0m')
        draw_hangman(tries_left)
        hidden_words_check = 0
        for letter in random_word:
            if letter in letters:
                print(letter, end='')
            else:
                print('?', end='')
                hidden_words_check = 1
        if hidden_words_check != 1:
            system('clear'), draw_header(), draw_hangman(8)
            print('\n\33[102m\33[5mYou win!\33[0m The answer was:', '\33[102m' + random_word +
                  '\33[0m\nYou score: \33[102m\33[5m%i\33[0m' % (len(random_word)/(1/tries_left)))
            break
        current_letter = input('\n\33[102m\33[5mGuess a letter: \33[0m\33[0m')[:1]
        print('current_letter: ', current_letter)
        letters += current_letter
        if current_letter in random_word:
            print('')
        else:
            tries_left -= 1
    if tries_left == 0:
        system('clear'), draw_header(), draw_hangman(0)
        print('\33[101m\33[5mYou lost!\33[0m The answer was:', '\33[102m' + random_word +
              '\33[0m\nYou score: \33[102m\33[5m%i\33[0m' % (len(random_word)/(1/(tries_left + 1))))


play_game(tries)

while True:
    new_game = input('Would you like a play again? \33[102m\33[5my\33[0m/\33[101m\33[5mn\33[0m: ')[:1]
    if new_game == 'y':
        play_game(tries)
    else:
        break
