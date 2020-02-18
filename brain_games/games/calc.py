import random
from operator import mul, sub, add

task = 'What is the result of the expression?'

OPERATORS = ((add, '+'), (sub, '-'), (mul, '*'))


def new_round():
    num1 = random.randint(1, 15)
    num2 = random.randint(1, 15)
    operation, sym = random.choice(OPERATORS)
    question = '{} {} {}'.format(num1, sym, num2)
    answer = str(operation(num1, num2))
    return question, answer
