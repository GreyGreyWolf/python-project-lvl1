from brain_games.games.Gcd import nod
import prompt


def main():
    print('Welcome to the Brain Games!')
    print('Find the greatest common divisor of given numbers')
    name = prompt.string('\n\nMay I have your name? ')
    print('Hello, ' + name + ' !')
    nod(name)


if __name__ == '__main__':
	main()