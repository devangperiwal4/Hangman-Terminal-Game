import random
from words import words
from hangman_visual import lives_visual_dict
import string


def get_valid_word(words):
    word = random.choice(words)  # randomly chooses something from the list
    # while '-' in word or ' ' in word:
    #     word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word.upper())  # letters in the word
    if '-' in word_letters:
        word_letters.remove('-')
    if ' ' in word_letters:
        word_letters.remove(' ')
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

    lives = 7

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        s = ''
        for i in range(lives):
            s = s + '\U0001F90D'
        print('You have', s, 'lives left and you have used these letters: ',
              ' '.join(used_letters))
        word_list = []
        # what current word is (ie W - R D)
        for letter in word:
            if letter in used_letters:
                word_list.append(letter)
            elif letter == '-' or letter == ' ':
                word_list.append(letter)
            else:
                word_list.append('_')

        print(lives_visual_dict[lives])
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1  # takes away a life if wrong
                print('\nYour letter,', user_letter, 'is not in the word.')

        elif user_letter in used_letters:
            print('\nYou have already used that letter. Guess another letter.')

        else:
            print('\nThat is not a valid letter.')

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print(lives_visual_dict[lives])
        print('You died, sorry. The word was', word)
    else:
        print('YAY! You guessed the word', word, '!!')


if __name__ == '__main__':
    hangman()
