import random, prompt
from sys import exit


def qst_even(name):
    i = 0
    while i < 3:
        num = random.randint(1,50)
        print('\nQuestion: ', num )
        ans = prompt.string('\nYour answer: ')
        if (num % 2 == 0 and ans.lower() == 'yes') or (num % 2 != 0 and ans.lower() == 'no') :
            print('Correct!')
            i += 1
        elif (ans.lower() == 'yes' and num % 2 != 0) :
            print("\n" + ans + " - is wrong answer ;(. Correct answer was 'NO'. \nLet's try again," + name + "!")
            exit()
        elif  (ans.lower() == 'no' and num % 2 == 0):
                print("\n" + ans.upper() + " - is wrong answer ;(. Correct answer was 'YES'. \nLet's try again," + name + "!")
                exit()
        else:
            print("\n" + ans.upper() + ' - is incorrectly typed response. Let\'s try again, '+ name + '!')
            exit()
    if i == 3:
        print('Congratulations, ' + name + '!')
