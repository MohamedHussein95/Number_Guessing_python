import random

total_guesses = 3
score = 0

print('-' * 15, 'Challenge yourself can you make it with a score of 50+', '-' * 15, end='\n')
print('-' * 15, 'Everytime a hint is given you lose 10 points', '-' * 15, end='\n')

while True:
    computer = random.randint(1, 10)
    guesses = 0

    while guesses < total_guesses:
        try:
            user_guess = int(input('Guess a number (1 to 10): '))
        except ValueError:
            print('Please choose a number from 1 to 10.')
            continue

        if user_guess < computer or user_guess > computer:
            print('Hint: Greater' if user_guess < computer else 'Hint: Lower')
            if score > 0:
                score -= 10
                print('Lost 10 points')

        elif user_guess == computer:
            score += 10
            break

        if computer % 2 == 0 and user_guess % 2 != 0:
            print('Hint: Even')
        elif computer % 2 != 0 and user_guess % 2 == 0:
            print('Hint: Odd')

        guesses += 1

    if guesses < total_guesses:
        print('You won!')
    else:
        print('You lost! The correct number was:', computer)

    print(f"Score: {score}")
    print('-------------------------------------------')

    if input('Play again? (yes or no): ').lower() != 'yes':
        break
