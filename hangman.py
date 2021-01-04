word = input('Enter a word: ')
print('You only have 7 chances if you choose incorrect...')
guessed_word = [None] * (len(word))
already_guessed_word = []
chances = 7
i = 0
while i != chances:
    letter = input()
    if letter in word:
        index_pos = [index for index, value in enumerate(word) if value == letter]
        for positions in index_pos:
            guessed_word[positions] = letter        
        print(guessed_word) 
        # Condition to skip giving chances once all letter are found
        if all(x is not None for x in guessed_word):
            break
    else:
        if letter not in already_guessed_word:
            # Condition to delete chance if incorrect letter is entered
            already_guessed_word.append(letter)
            print('You have {} chances left'.format(chances-i))
            i += 1
        print('Already guessed word which are incorrect are: ', already_guessed_word)
        
if any(x is None for x in guessed_word):
    print('TRY AGAIN !!! ')
    print('The correct word was {}'.format(word) )
else:
    print(''.join(guessed_word))
    print('Congratulations.. You guessed it RIGHT !!! ')