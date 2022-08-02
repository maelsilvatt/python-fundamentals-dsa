# My solution to 'Lab 03 - Jogo da Forca' from 'Python Fundamentos para Análise de Dados 3.0'
# from Data Science Academy
#
# This game has been created exclusively for learning purposes
# All words and tips are from W3schools. Copyright 1999-2022 by Refsnes Data. All Rights Reserved.
#

# Import choice to choose a random word from our 'words.txt'
from random import choice

# Imports 'literal_eval' to convert str to dict
from ast import literal_eval

# Imports clear to keep the terminal clean
from os import system

# Imports sleep to make transtitions smoother
from time import sleep

# ANSI color codes for outputs
ANSI_CYAN = '\033[1;36m'
ANSI_RED = '\033[1;31m'
ANSI_YELLOW = '\033[1;33m'
ANSI_RESET = '\033[0m'


# Cleans terminal screen
def clear(timer=1.5):

    # Simple timer to make smoother transitions
    sleep(timer)
    _ = system('clear')


# Hangman game class
class Hangman:
    def __init__(self):

        # Selects a random word from 'words.txt' to
        # initialize 'self.word'
        with open('words.txt', 'r') as file:
            self.word = choice(file.read().split('\n'))

        # Selects a random word from 'words.txt' to
        # initialize 'self.word' and 'self.tip'
        with open('words.txt', 'r') as file:

            # Prints file content into 'file_content'
            file_content = file.read().split('\n')

            # Choose a random word tip pair from 'file_content',
            # and evaluate it to convert from str to dict
            # finally get a key valur pair of the selected dictionary
            random_word_tip_pair = literal_eval(choice(file_content)).items()

            # converts 'random_word_tip_pair' into a list and pops its key value par
            self.word, self.tip = list(random_word_tip_pair).pop()

        # Creates a ghost version of the original word that will be displayed in game
        self.guessing_word = '_ ' * len(self.word)

        # Creates a set of all missing letters
        self.missing_letters = set()

        # Imports all stages of our game
        with open('board.txt', 'r') as file:
            self.board = file.read().split(',')

        # Initializes 'stage', that is the actual number of body parts
        self.stage = 0

    # Validates an input letter based on the chosen word
    def guess(self, letter):

        # Checks if the letter is not present in the word
        if letter not in self.word:

            # Adds the actual letter to a set of all missing letters
            self.missing_letters.add(letter)

            # Updates the number of body parts
            self.stage += 1

            return False

        else:
            # Checks if the actual letter has actually been chosen before
            if letter in self.guessing_word:
                return False

            # Creates a boolean to identify if there was any match
            match = False

            # Creates a copy of 'guessing_word'
            _temp = self.guessing_word.split()

            # Runs the word to check if there is a match
            # if true, it updates '_temp' with the matched letter
            # if false, it concatenates _temp[i] with blank space
            # because we are using split
            for i in range(len(_temp)):
                if letter == self.word[i]:
                    _temp[i] = f'{letter} '
                    match = True
                else:
                    _temp[i] += ' '
            if match:
                # Updates 'guessing_word' with matched letters
                self.guessing_word = ''.join(_temp)

                return True
            else:
                return False

    # Checks if the player has won
    def won(self):
        if self.guessing_word.replace(' ', '') == self.word:
            return True


# Game's main function
def main():

    # to start a new game, we instantiate 'Hangman'
    game = Hangman()

    # Main menu loop
    while not game.won():
        # Clears terminal outputs
        clear()

        # Prints hangman board
        print(f'{ANSI_YELLOW}'
              f'{game.board[game.stage]}'
              f'{ANSI_CYAN}' 
              f'\nWord: {game.guessing_word}'
              f'\nTip: {game.tip}'
              # Using join to output 'x, c, k' instead of '('x', 'c', 'k')'
              f'\nMissing letters: {", ".join(game.missing_letters)}')

        # Gets input letter
        letter = input('Enter a letter: ')

        # Checks if the letter is there or not
        if game.guess(letter):
            print('Right answer!')
        else:
            print(f'{ANSI_RED}Wrong answer. Try again!')

            # Checks if game is over
            if game.stage == 6:
                print(f'\n{ANSI_RED}You lost :('
                      f'\nThe answer is: {game.word}')

                # Ends the game
                return

    # Prints a victory message
    print('\nCongrats! You won!'
          f'\nThe answer is: {game.word}')


# Calls main function
main()
