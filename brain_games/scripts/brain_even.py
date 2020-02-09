from brain_games.games.Questions import qst_even
import prompt

def main():
    print('Welcome to the Brain Games!')
    print('Answer "YES" if number even otherwise answer "NO"')
    name = prompt.string('\n\nMay I have your name? ')
    print('Hello, ' + name + ' !')
    qst_even(name)


if __name__ == '__main__':
	main()
        
