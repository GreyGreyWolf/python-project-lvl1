import random

task = 'Find the greatest common divisor of given numbers.'


def check_gcd(x, y):
    w = [x, y]
    w.sort()
    a, b = w
    if b % a == 0:
        return a
    i = a
    while i >= 1:
        if b % i == 0 and a % i == 0:
            return i
        i -= 1


def generation():
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    question = '{} AND {}'.format(num1, num2)
    answer = str(check_gcd(num1, num2))
    return question, answer
