import os
os.system('clear')


class Hangman:
    def __init__(self):
        # create secret word dictionary 
        self.word = 'prova'                                 # word you have to guess
        self.len_word = len(self.word)                      # word characters numbers
        self.word_dict = {}
        self.step_num = 0
        for i in range(self.len_word):
            self.word_dict[i] = ['_', self.word[i]]
        '''
        self.word_dict (result example)
        0 ['_', 'p']
        1 ['_', 'r']
        2 ['_', 'o']
        3 ['_', 'v']
        4 ['_', 'a']
        '''

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
        self.check = 0                              
        # core game
        while self.step_num < 7:                            # 7 are the Hangman steps

            print(self.death()[self.step_num])              # shows the Hangman
            self.guess = input('what letter? > ')



            if not self.guess in self.word:
                self.step_num += 1
                print(self.get_hidden_word(self.guess))     # prints hidden word
            else:
                self.check += 1
                print(self.get_hidden_word(self.guess))     # prints hidden word
                if self.check == self.len_word:
                    break



            #### just for debugging
            print(self.step_num)
            print(self.check)
            #### just for debugging
        
        
        if self.check == self.len_word:
            print('You WIN!')
        else:
            print(self.death()[self.step_num])              # shows the Hangman
            print('You LOST')


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



# IT WORKS! shows hidden word:
# while True:
#     letter = input('what letter? > ')
#     print(play.get_hidden_word(letter))