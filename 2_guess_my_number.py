# Great. 20/20. Get rid of the warning when exiting the program.
# Guess My Number
'''
Pseudocode:
1. Welcome user to program
2. Give user instructions
3. Program generates a random number from 1 to 100
4. User enters a guess for the number
5. Program says whether guess is too high or too low
6. User keeps guessing, with high/low feedback, until getting correct answer
7. Ask if user wants to play again. If so, start over. If not, exit with 'enter'
'''
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
