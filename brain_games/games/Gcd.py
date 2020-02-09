import random
from fractions import gcd

task = 'Find the greatest common divisor of given numbers.'

def nod_num(num1, num2):
    res = gcd(num1, num2)
    return res

def gen():
    num1 = random.randint(1,50)
    num2 = random.randint(1,50)
    escn_qst = '{} AND {}'.format(num1, num2)
    ans = str(nod_num(num1, num2))
    return escn_qst, ans