import prompt


def salute_user(module):
    print("Welcome to the Brain Games!")
    print(module.task)
    name = prompt.string('\n\nMay I have your name? ')
    print('Hello, {}! '.format(name))
    return name