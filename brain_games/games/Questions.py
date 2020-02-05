import random, prompt
from sys import exit


def qst(name):
    i = 0
    while i < 3:
        num =  random.randint(1,50)
        print('\nQuestion: ', num)
        ans = prompt.string('\nYour answer: ')
        if  (ans.lower() == 'yes' and num % 2 == 0) or (ans.lower() == 'no' and num % 2 != 0):
            print('Correct!')
            i += 1
        elif ans.lower() == 'yes' and num % 2 != 0:
            print("\n'yes' is wrong answer ;(. Correct answer was 'no'. \nLet's try again," + name + "!")
            exit()
        elif ans.lower() == 'no' and num % 2 == 0:
            print("\n'no' is wrong answer ;(. Correct answer was 'yes'. \nLet's try again," + name + "!")
            exit()
        elif ans.lower() != 'no' or ans.lower() != 'yes':
            print('incorrectly typed response. Let\'s try again, '+ name + '!')
            exit()
    if i == 3:
        print('Congratulations, ' + name + '!')
    else:
        exit()
