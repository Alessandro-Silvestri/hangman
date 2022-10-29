import os
os.system('clear')


class Hangman:
    def __init__(self):
        self.word_dict = {}
        self.step_num = 0

    def get_hidden_word(self, letter: str):
        '''show the hidden word like this: ______'''
        hidden_word = ''
        # it generates the hidden_word adding the input letters
        for i, j in self.word_dict.items():
            if j[1] == letter:
                self.word_dict[i][0] = letter
                hidden_word += j[0]
            else:
                hidden_word += j[0]
        return hidden_word

    def core_game(self):
        self.word = input('Insert the secret word: > ').upper()
        os.system('clear')

        self.len_word = len(self.word)                      # word characters numbers
        for i in range(self.len_word):                      # create secret word dictionary 
            self.word_dict[i] = ['_', self.word[i]]
        
        print(self.death()[self.step_num])                  # shows the Hangman
        self.hidden_word = self.get_hidden_word('.')
        print(self.hidden_word)                             # prints hidden word
        
        # core game
        while self.step_num < 7:                             # 7 are the Hangman steps
            self.guess = input('what letter? > ').upper()
            if not self.guess in self.word:
                os.system('clear')
                self.step_num += 1
                print(self.death()[self.step_num])           # shows the Hangman
                self.hidden_word = self.get_hidden_word(self.guess)
                print(self.hidden_word)                      # prints hidden word
        
            else:
                os.system('clear')
                print(self.death()[self.step_num])           # shows the Hangman
                self.hidden_word = self.get_hidden_word(self.guess)
                print(self.hidden_word)                      # prints hidden word   
                if not '_' in self.hidden_word:
                    break

        if not '_' in self.hidden_word:
            print('You WIN!')
        else:
            print('You LOST')
            print('The word was:', self.word)

    def death(self):
        '''steps to death'''
        self.hangman_steps = ['''
            +---+
                |
                |
                |
                |
                |
            =========''','''
            +---+
            |   |
                |
                |
                |
                |
            =========''', '''
            +---+
            |   |
            O   |
                |
                |
                |
            =========''', '''
            +---+
            |   |
            O   |
            |   |
                |
                |
            =========''', '''
            +---+
            |   |
            O   |
           /|   |
                |
                |
            =========''', '''
            +---+
            |   |
            O   |
           /|\  |
                |
                |
            =========''', '''
            +---+
            |   |
            O   |
           /|\  |
           /    |
                |
            =========''', '''
            +---+
            |   |
            O   |
           /|\  |
           / \  |
                |
            =========''']
        return self.hangman_steps


play = Hangman()
play.core_game()

