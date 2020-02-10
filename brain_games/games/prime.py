import random

task = 'Answer "YES" if given number is prime. Otherwise answer "NO".'


def prm_check(num):
    lst = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
           47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103,
           107, 109, 113]
    if num in lst:
        return "YES"
    else:
        return "NO"


def gen():
    escn_qst = random.randint(1, 120)
    ans = prm_check(escn_qst)
    return escn_qst, ans
