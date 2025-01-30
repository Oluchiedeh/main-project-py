import random
print('Welcome to Zihe Games')
print('I am thinking of a number between 1 and 100, guess what the number is?')

number_to_guess = random.randint(1,100)
guess = 0
attempt = 0

while guess != number_to_guess:
    guess = int(input('Enter your guess:'))
    if guess < number_to_guess:
        print('Try again,but higher!')
    elif guess > number_to_guess:
        print('Try again, but lower!')
    else:
       print(f'Congratulations your guessed {number_to_guess} correctly')
        