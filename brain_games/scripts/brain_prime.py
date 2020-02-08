from brain_games.games.Prime import prm
import prompt


def main():
    print('Welcome to the Brain Games!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    name = prompt.string('\n\nMay I have your name? ')
    print('Hello, ' + name + ' !')
    prm(name)


if __name__ == '__main__':
	main()