import random, prompt
from fractions import gcd
from sys import exit


def nod_num(name):
    i = 0
    while i < 3:
        num1 = random.randint(1,50)
        num2 = random.randint(1,50)
        print('\nQuestion: ', str(num1) + ' AND ' + str(num2))
        ans = prompt.string('\nYour answer: ')
        result = gcd(num1, num2)
        if  (ans == str(result)):
            print('Correct!')
            i += 1
        else:
            print("\n" + ans.upper() + " <--- is wrong answer ;(. Correct answer was " + str(result) + "\nLet's try again," + name + "!")
            exit()
    if i == 3:
        print('Congratulations, ' + name + '!')
