import os
# os.system('clear')


class Hangman:
    def __init__(self):
        # create secret word dictionary 
        self.word_dict = {}
        self.step_num = 0
        self.word = 'prova'
        self.len_word = len(self.word)
        for i in range(self.len_word):
            self.word_dict[i] = ['_', self.word[i]]
 
    def get_hidden_word(self, letter):
        '''at the moment not used'''
        '''show the hidden word like this: ______'''
        hidden_word = ''
        # show the hidden word
        for i in self.word_dict:
            hidden_word += self.word_dict[0][0]
        return hidden_word

    def core_game(self):
        '''user interaction'''
        self.check = 0
        print(self.death()[self.step_num])
        # core game
        while self.step_num < 7:
            self.guess = input('what letter? > ')
            # os.system('clear')
            if not self.guess in self.word:
                self.step_num += 1
            else:
                self.check += 1
                if self.check == self.len_word:
                    break
            
            print(self.death()[self.step_num])
            print(self.step_num)
            print(self.check)
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