from wordle import Wordle
from colorama import Fore
from letter_state import LetterState
from typing import List

def main():
    print('Hello Wordle !')
    wordle = Wordle('APPLE')

    while wordle.can_attempt:
        x = input('\nType your word: ')

        if len(x) != wordle.WORD_LENGTH:
            print(Fore.RED + f'Word must be {wordle.WORD_LENGTH} characters long!' + Fore.RESET)
            continue

        wordle.attempt(x)
        display_results(wordle)

    if wordle.is_solved:
        print('You have guessed the word. Nice work !')
    else:
        print('You failed, this is wrong words')

def display_results(wordle: Wordle):
    print('Your results so far:')
    print(f'You have {wordle.remaining_attempts} attempts remaining\n')
    for word in wordle.attempts:
        result = wordle.guess(word)
        colored_result_str = convert_result_to_color(result)
        print(colored_result_str)

    for _ in range(wordle.remaining_attempts):
        print(' '.join(['_'] * wordle.WORD_LENGTH))

def convert_result_to_color(result: List[LetterState]):
    result_with_color = []
    for letter in result:
        if letter.is_in_position:
            color = Fore.GREEN
        elif letter.is_in_word:
            color = Fore.YELLOW
        else:
            color = Fore.WHITE
        colored_letter = color + letter.character + Fore.RESET
        result_with_color.append(colored_letter)
    return ' '.join(result_with_color)

if __name__ == '__main__':
    main()