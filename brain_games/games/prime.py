import random
from math import gcd

task = 'Answer "YES" if given number is prime. Otherwise answer "NO".'


def prime_check(num):
    i = num
    divisor = 0
    while i >= 1:
        divisor = gcd(num, i)
        if 1 < divisor < num:
            return False
        i -= 1
    return True


def generation():
    question = random.randint(1, 1000)
    answer = prime_check(question)
    if answer is True:
        answer = 'YES'
    else:
        answer = 'NO'
    return question, answer
