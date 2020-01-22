import prompt


def welcome_user():
    name = prompt.string('\n\nMay I have your name?')
    print('Hello, ' + name + ' !')