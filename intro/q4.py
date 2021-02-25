import random

guess = int(input('Guess the number (1 - 10): '))
actualNum = random.randint(0, 10)

while guess != actualNum:
    guess = int(input('Guess the number (1 - 10): '))

    