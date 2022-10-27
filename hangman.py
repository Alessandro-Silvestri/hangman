import os
# os.system('clear')


class Hangman:
    def __init__(self):
        # create secret word dictionary 
        self.word_dict = {}
        self.step_num = 0
        self.word = 'prova' 
        for i in range(len(self.word)):
            self.word_dict[i] = ['_', self.word[i]]
 
    def get_hidden_word(self):
        '''show the hiddemn word like this: ______'''
        # show the hidden word
        for i in self.word_dict:
            print(self.word_dict[0][0], end='')

    def core_game(self):
        '''user interaction'''
        print(self.death()[self.step_num])

        # core game
        while self.step_num < 7:
            self.guess = input('what letter? > ')
            # os.system('clear')
            if not self.guess in self.word:
                self.step_num += 1
            print(self.death()[self.step_num])
            print(self.step_num)
        quit()

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


'''
self.word_dict (result example)
0 ['_', 'p']
1 ['_', 'r']
2 ['_', 'o']
3 ['_', 'v']
4 ['_', 'a']
'''

play = Hangman()
print(play.core_game())