import random, prompt
from fractions import gcd
from sys import exit


def nod(name):
    i = 0
    while i < 3:
        num1 = random.randint(1,50)
        num2 = random.randint(1,50)
        print('\nQuestion: ', str(num1) + ' ' + str(num2))
        ans = prompt.integer('\nYour answer: ')
        result = gcd(num1, num2)
        if  (ans == result):
            print('Correct!')
            i += 1
        elif ans != result:
            print("\n" + str(ans) + " <--- is wrong answer ;(. Correct answer was " + str(result) + "\nLet's try again," + name + "!")
            exit()
    if i == 3:
        print('Congratulations, ' + name + '!')
    else:
        exit()

