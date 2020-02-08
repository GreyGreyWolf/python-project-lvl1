from brain_games.games.Progression import prg
import prompt


def main():
    print('Welcome to the Brain Games!')
    print('What number is missing in the progression?')
    name = prompt.string('\n\nMay I have your name? ')
    print('Hello, ' + name + ' !')
    prg(name)


if __name__ == '__main__':
	main()