from brain_games.games.Questions import qst
import prompt

def main():
    print('Welcome to the Brain Games!')
    print('Answer "yes" if number even otherwise answer "no"')
    name = prompt.string('\n\nMay I have your name? ')
    print('Hello, ' + name + ' !')
    qst(name)


if __name__ == '__main__':
	main()
        
