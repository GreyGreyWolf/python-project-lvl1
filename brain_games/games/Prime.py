import random, prompt
from sys import exit


def prm_num(name):
    i = 0
    while i < 3:
        n = random.randint(1,700) 
        lst = [2, 3, 5, 7, 11 ,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,
                179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,
                379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571,577,587,593,	
                599,601,607,613,617,619,631,641,643,647,653,659,661,673,677,683,691,701]
        print('\nQuestion: ' , n)
        ans = prompt.string('\nYour answer: ')
        if n in lst and ans.lower() == 'yes' or (n not in lst and ans.lower() == 'no') :
            print('Correct!')
            i += 1
        elif n in lst and ans.lower() == 'no':
            print("\n" + ans.upper() + " - is wrong answer ;(. Correct answer was 'YES'. \nLet's try again," + name + "!")
            exit()
        elif not n in lst and ans.lower() == 'yes':
            print("\n" + ans.upper() + " - is wrong answer ;(. Correct answer was 'NO'. \nLet's try again," + name + "!")
            exit()
        elif ans.lower() != 'no' or ans.lower() != 'yes':
            print('\n' + ans.upper() + ' - incorrectly typed response. Let\'s try again, '+ name + '!')
            exit()
    if i == 3:
        print('Congratulations, ' + name + '!')
