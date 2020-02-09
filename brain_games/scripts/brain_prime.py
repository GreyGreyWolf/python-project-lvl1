from brain_games.games.Prime import prm_num
import prompt


def main():
    print('Welcome to the Brain Games!')
    print('Answer "YES" if given number is prime. Otherwise answer "NO".')
    name = prompt.string('\n\nMay I have your name? ')
    print('Hello, ' + name + ' !')
    prm_num(name)


if __name__ == '__main__':
	main()