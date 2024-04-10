"""
Rock, Paper, Scissors game played in terminal.
Made by Kamil Seternus
https://github.com/kseternus
"""
import random


class RockPaperScissors:
    """
    Main class to handle an instance of Rock, Paper, Scissors game
    """

    def __init__(self):
        """
        Initialize the variables.
        """
        self.wins = self.loses = self.ties = 0
        self.my_choice = None
        self.choices = ['Rock', 'Paper', 'Scissors']

    def random_choice(self):
        """
        Random choice from the list
        :return: String containing computer choice
        """
        return random.choice(self.choices)

    def check_win(self, my_choice, computer_choice):
        """
        If statement checking who wins according to rules: rock wins against scissors, paper wins against rock
        and scissors wins against paper. [0] is added to print the choices without the square brackets and quotes.
        Everytime you win/lose/tie the corresponding variable values are incremented by 1.
        :param my_choice: String of chosen Rock, Paper or Scissors by player from run_game()
        :param computer_choice: String of chosen randomly Rock, Paper or Scissors by computer from random_choice()
        :return: None
        """
        if computer_choice == my_choice:
            print(f'You picked {my_choice[0]} and Computer also picked {computer_choice[0]}')
            print('That is a tie!')
            self.ties += 1
        else:
            if ((my_choice[0] == 'Paper' and computer_choice[0] == 'Rock') or
                    (my_choice[0] == 'Scissors' and computer_choice[0] == 'Paper') or
                    (my_choice[0] == 'Rock' and computer_choice[0] == 'Scissors')):
                print(f'You picked {my_choice[0]} and Computer picked {computer_choice[0]}')
                print('You win!')
                self.wins += 1
            else:
                print(f'You picked {my_choice[0]} and Computer picked {computer_choice[0]}')
                print('You lose!')
                self.loses += 1

    def score(self):
        """
        Prints score containing player wins, computer wins and ties
        :return: None
        """
        print(f'\nYour wins: {self.wins}, computer wins: {self.loses}, ties: {self.ties}\n')

    def run_game(self):
        """
        Here we play with computer while player choice != Q with will break from the loop and print score.
        We call check_win and pass player choice and computer (random) choice to check who won round.
        :return: None
        """
        while self.my_choice != 'Q':
            my_choice = input('Pick rock, paper or scissors: ').capitalize()
            if my_choice == 'Q':
                print(f'Game ended with score:\nYour wins: {self.wins}, Computer wins: {self.loses}, ties: {self.ties}')
                print('Bye! See you soon :)')
                exit()
            elif my_choice not in self.choices:
                print('Wrong choice!')
            else:
                break
        computer_choice = self.random_choice()
        self.check_win([my_choice], [computer_choice])

"""
if __name__== '__main__' is a conditional statement that tells the Python interpreter under what conditions the main
method should be executed. There we call class and run game
"""
if __name__ == '__main__':
    print('Welcome to Rock, Paper, Scissors game!\n'
          'Rules are simple: rock wins against scissors, paper wins against rock and scissors wins against paper.\n'
          'Type "Q" to end game. Good Luck!\n')
    game = RockPaperScissors()
    while True:
        game.run_game()
        game.score()
