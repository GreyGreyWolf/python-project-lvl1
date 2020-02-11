import prompt


def salute_user(module):
    print("Welcome to the Brain Games!")
    print(module.task)
    name = prompt.string('\n\nMay I have your name? ')
    print('Hello, {}! '.format(name))
    return name


def engine(module):
    name = salute_user(module)
    i = 0
    while i < 3:
        question, result = module.generation()
        print('\nQuestion: {}'.format(question))
        answer = prompt.string('\nYour answer: ')
        if answer.upper() != result:
            print()
            print("'{}' <--- is wrong answer ;(.Correct answer was '{}'."
                  "Let's try again, {}!".format(answer.upper(), result, name))
            break
        print('Correct!')
        i += 1
    else:
        print('Congratulations, {}!'.format(name))
