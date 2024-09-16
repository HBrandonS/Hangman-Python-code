import random

bank_words = ['??', '??', '??']
random_word = random.choice(bank_words)
placeholder = ''
word_lenght = len(random_word)
game_over = False
correct_letters = []
lives = 6
for position in range(word_lenght):
    placeholder += "_"

print(placeholder)

while not game_over:
    display = ''
    guess_letter = input('Guess the letter: ').lower()

    for letter in random_word:
        if letter == guess_letter:
            display += letter
            correct_letters.append(guess_letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += '_'

    print(display)

    if "_" not in display:
        game_over = True
        print('You win!')

    if guess_letter not in random_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lose!")
