from brain_games.salute import salute_user
import prompt
from sys import exit

def engine(module):
    name = salute_user(module)
    i = 0
    while i < 3:
        escn_qst, result = module.gen()
        print('\nQuestion: {}'.format(escn_qst))
        ans = prompt.string('\nYour answer: ')
        if ans.upper() == result:
            print('Correct!')
            i += 1
        else:
             print("\n'{}' <--- is wrong answer ;(.Correct answer was '{}'. \nLet's try again, {}!".format(ans.upper(), result, name))
             exit()
    if i == 3:
        print('Congratulations, {}!'.format(name))
    