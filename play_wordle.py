from wordle import Wordle

def main():
    print('Hello Wordle !')
    wordle = Wordle('APPLE')

    while wordle.can_attempt:
        x = input('Type your word: ')

        if len(x) != wordle.WORD_LENGTH:
            print(f'Word must be {wordle.WORD_LENGTH} characters long!')
            continue

        wordle.attempt(x)
        result = wordle.guess(x)
        print(*result, sep='\n')

    if wordle.is_solved:
        print('You have guessed the word. Nice work !')
    else:
        print('You failed, this is wrong words')

if __name__ == '__main__':
    main()