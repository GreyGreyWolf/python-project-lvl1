import random

task = 'What number is missing in the progression?'


def gen():
    n = random.randint(1, 5)
    d = random.randint(1, 10)
    seq = [n, (n + d), (n + 2*d), (n + 3*d), (n + 4*d), (n + 5*d),
           (n + 6*d), (n + 7*d), (n + 8*d), (n + 9*d)]
    ans = random.choice(seq)
    index_num = seq.index(ans)
    copy_seq = seq.copy()
    copy_seq.pop(index_num)
    copy_seq.insert(index_num, '...')
    for i, _ in enumerate(copy_seq):
        if i < 9:
            copy_seq[i] = str(copy_seq[i]) + ', '
        copy_seq[i] = str(copy_seq[i])
    escn_qst = ''.join(copy_seq)
    return escn_qst, str(ans)
