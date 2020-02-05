import random, prompt
from sys import exit

def clc(name): 
    i = 0
    while i < 3:
        num1 = random.randint(1,50)
        num2 = random.randint(1,50)
        dict_opr = {'mul':"*", 'add':"+", 'sub':"-"}
        random_opr = random.choice(['mul', 'add', 'sub'])
        if random_opr == 'mul':
            print('\nQuestion: ', str(num1) + ' * ' + str(num2) )
            ans = prompt._prompt_input ('\nYour answer: ')
            result = num1*num2
            if  ans == result:
                print('Correct!')
                i += 1
            elif (ans != result) or (type(ans) != int):
                print("\n" + str(ans) + " <--- is wrong answer ;(. Correct answer was " + str(result) + "\nLet's try again," + name + "!")
                exit()          
        elif random_opr == 'add':
            print('\nQuestion: ', str(num1) + ' + ' + str(num2))
            result = num1+num2
            ans = prompt._prompt_input('\nYour answer: ')
            if  ans == result:
                print('Correct!')
                i += 1
            elif (ans != result) or (type(ans) != int):
                print("\n" + str(ans) + " <--- is wrong answer ;(. Correct answer was " + str(result) + "\nLet's try again," + name + "!")
                exit()      
        elif random_opr == 'sub':
            print('\nQuestion: ', str(num1) + ' - ' + str(num2))
            result = num1-num2
            ans = prompt._prompt_input('\nYour answer: ')
            if  ans == result:
                print('Correct!')
                i += 1
            elif (ans != result) or (type(ans) != int):
                print("\n" + str(ans) + " <--- is wrong answer ;(. Correct answer was " + str(result) + "\nLet's try again," + name + "!")
                exit() 
    if i == 3:
        print('Congratulations, ' + name + '!')
    else:
        exit()
        