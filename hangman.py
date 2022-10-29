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

        # it modifies word_dict, reveals the letter guessed
        for i, j in self.word_dict.items():
            if j[1] == letter:
                self.word_dict[i][0] = letter

        # put all the characters: '_' and <letter> inside hidden_word
        for i, j in self.word_dict.items():
            hidden_word += j[0]

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

            #### just for debugging
            print(self.step_num)
            print(self.check)
            #######################
        
        if self.check == self.len_word:
            print('You WIN!')
        else:
            print('You LOST')
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




play = Hangman()

while True:
    letter = input('what letter? > ')
    print(play.get_hidden_word(letter))



# IT WORKS! shows hidden word:
# while True:
#     letter = input('what letter? > ')
#     print(play.get_hidden_word(letter))