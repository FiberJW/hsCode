# 15/20
# Nice job. I like the personality of the program.
# Computer guessed a number above a previous guess that I said was too high.
# Give option to play again.


# CPU guesses number
from random import randint
import time

print("\tEnter a number from 1 - 100. I'll try to guess it. Bring it on!")

num = 0 # Init Sentry Variable

# Checks if number is in proper range
while num < 1 or num >100:
    try:
        num = int(input("\n\t\tInput your number (I'm not looking):\n\t=>"))
    except ValueError:
        print('\n\t\t\tYou didn\'t input an integer')
        continue
    if num > 100:
        print("Number is too high!")
    if num < 1:
        print("Number is too low!")

cpu_guess = randint(1, 100)

print('I think that your number is: ', cpu_guess)
sentry = 0
while cpu_guess != num:
    res = input('\nType (1) if my guess is too high, or (2) if my guess is too low:\n\t=>')
    if res == '1':
        high_guess = cpu_guess
        cpu_guess = randint(1, high_guess)
    elif res == '2':
        low_guess = cpu_guess
        cpu_guess = randint(low_guess, 100)
    else:
        print('\nInvalid input.')
        res = input('\nType (1) if my guess is too high; or (2) if my guess s too low:\n\t=>')
    print("I'll try again...", cpu_guess)
    time.sleep(0.1)
    sentry += 1
    if sentry > 4:
        print('FINE. I\'LL DO IT BY MYSELF')
        time.sleep(0.2)
        while cpu_guess != num:
            if cpu_guess > num:
                high_guess = cpu_guess - 10
                cpu_guess = randint(1, high_guess)
                print("\nI'll try again...", cpu_guess)
            elif cpu_guess < num:
                low_guess = cpu_guess + 10
                cpu_guess = randint(low_guess, 100)
                print("\nI'll try again...", cpu_guess)
            else:
                break

print("FINALLY! I got it!\n")
print('Your number is: ', cpu_guess)
print('\n\tI was actually looking after all...')

