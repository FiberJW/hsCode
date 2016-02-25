def guess_user_num():
  import random, time

  print('\t\t\tGuess My Number!\nI will think of a number between 1 and 100 (Inclusive)\n\nTell me what you think the number is. I\'ll give you hints\n\n')

  def main(): #define main instructions as function for calling later
      num = random.randint(0, 100)
      print('\nI\'m thinking of a number...')
      def con():
          response = str(input("Do you want to try again? Type 'yes' to continue or press the enter key to exit\n\t=>")).lower()
          if response == 'yes' or response == 'y':
              main()
          elif response == '':
              print('\nThanks for playing!')
              time.sleep(2)
              raise SystemExit
          else:
              print('Invalid Response', end='\n')
              con()
      def dec(): # Gets input and decides upon it what to do
          nonlocal num
          try:
              guess = int(input('What am I thinking of?\n\t=>'))
          except ValueError:
              print('I don\'t think you entered a number-- try again.\n')
              guessNum()
          if guess == num:
              con()
          elif guess > num:
              print('Too high')
              guessNum()
          elif guess < num:
              print('Too low')
              guessNum()

      def guessNum():
          time.sleep(1)
          dec()

      guessNum()

  main()


def guess_cpu_num():
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


def menu():
    res = input('Do you want to [1] Have the computer guess your number, ' \
    '[2] Guess the computer\'s number, or [3] Exit the program?\n\t=>')
    if res == '1':
        guess_user_num()
    elif res == '2':
        guess_cpu_num()
    elif res == '3':
        raise SystemExit
    else:
        print('\nBad choice.\n')
        menu()


def main():
    print('Welcome to the Guess My Number program!\n')
    menu()
main()
