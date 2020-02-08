import random, prompt
from sys import exit


def prg(name):
    i = 0
    while i < 3:
        n = random.randint(1,5) # Первый элемент последовательности
        d = random.randint(1,10) # Шаг последовательности
        # Арифметическая последовательность
        seq = [n, (n + d), (n + 2*d), (n + 3*d), (n + 4*d), (n + 5*d), (n + 6*d), (n + 7*d), (n + 8*d), (n + 9*d)]
        result = random.choice(seq) # Тот самый искомый элемент
        format_seq = seq.copy() # Копирование последовательности
        index = seq.index(result) # Нахождение индекса заменямого элемента
        format_seq.pop(index) 
        format_seq.insert(index, '...')
        print('\nQuestion: ' , *format_seq)
        ans = prompt.integer('\nYour answer: ')
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