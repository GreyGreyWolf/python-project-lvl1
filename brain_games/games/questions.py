import random, prompt

task = "Answer 'YES' if number even otherwise answer 'NO'."

def qst_even(vrb):
    if vrb % 2 == 0:
        return "YES"
    else:
        return "NO"
    
def gen():
    escn_qst = random.randint(1,50)
    ans = qst_even(escn_qst)
    return escn_qst, ans
    

    
