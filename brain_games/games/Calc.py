import random, prompt
from sys import exit

def clc_expr(name): 
    i = 0
    while i < 3:
        num1 = random.randint(1,50)
        num2 = random.randint(1,50)
        random_opr = random.choice(['mul', 'add', 'sub'])
        if random_opr == 'mul':
            print('\nQuestion: ', str(num1) + ' * ' + str(num2) )
            result = num1*num2
        elif random_opr == 'add':
            print('\nQuestion: ', str(num1) + ' + ' + str(num2))
            result = num1+num2
        elif random_opr == 'sub':
            print('\nQuestion: ', str(num1) + ' - ' + str(num2))
            result = num1-num2
        ans = prompt.string('\nYour answer: ')
        if  ans == str(result):
            print('Correct!')
            i += 1
        else:
            print("\n" + ans.upper() + " <--- is wrong answer ;(. Correct answer was " + str(result) + "\nLet's try again," + name + "!")
            exit()
    if i == 3:
        print('Congratulations, ' + name + '!')
