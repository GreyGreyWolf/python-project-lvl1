import random
from itertools import islice, count

task = 'What number is missing in the progression?'

SIZE = 10


def new_round():
    seq = list(islice(count(
               start=random.randint(10, 60),
               step=random.randint(1, 10)),
               SIZE))
    answer = random.choice(seq)
    index_num = seq.index(answer)
    seq[index_num] = '...'
    for i, _ in enumerate(seq):
        seq[i] = str(seq[i])
    question = ', '.join(seq)
    return question, str(answer)
