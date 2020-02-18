import random

task = "Answer 'YES' if number even otherwise answer 'NO'."


def question_even(a):
    if a % 2 == 0:
        return "YES"
    else:
        return "NO"


def new_round():
    question = random.randint(1, 50)
    answer = question_even(question)
    return question, answer
