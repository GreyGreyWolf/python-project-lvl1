from brain_games.games.Calc import clc_expr
import prompt


def main():
    print('Welcome to the Brain Games!')
    print('What is the result of the expression?')
    name = prompt.string('\n\nMay I have your name? ')
    print('Hello, ' + name + ' !')
    clc_expr(name)


if __name__ == '__main__':
	main()