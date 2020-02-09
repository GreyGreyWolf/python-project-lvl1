import random, prompt
from sys import exit


def prg_num(name):
    i = 0
    while i < 3:
        n = random.randint(1,5)
        d = random.randint(1,10)
        seq = [n, (n + d), (n + 2*d), (n + 3*d), (n + 4*d), (n + 5*d), (n + 6*d), (n + 7*d), (n + 8*d), (n + 9*d)]
        result_num = random.choice(seq)
        index_num = seq.index(result_num)
        seq.pop(index_num)
        seq.insert(index_num, '...')
        print('\nQuestion: ' , *seq)
        ans = prompt.string('\nYour answer: ')
        if  (ans == str(result_num)):
            print('Correct!')
            i += 1
        elif ans != result_num:
            print("\n" + ans.upper() + " <--- is wrong answer ;(. Correct answer was " + str(result_num) + "\nLet's try again," + name + "!")
            exit()
    if i == 3:
        print('Congratulations, ' + name + '!')
