import random
from operator import mul, sub, add

task = 'What is the result of the expression?'

lst = ((add, '+'), (sub, '-'), (mul, '*'))


def gen():
    num1 = random.randint(1,15)
    num2 = random.randint(1,15)
    operation, sym = random.choice(lst)
    escn_qst = '{} {} {}'.format(num1, sym, num2)
    ans = str(operation(num1, num2))
    return escn_qst, ans
    
