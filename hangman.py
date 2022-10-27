import os
# os.system('clear')

hangman_steps = ['''
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

# create secret word dictionary 
word_dict = {}
word = 'prova'
for i in range(len(word)):
    word_dict[i] = ['_', word[i]]
'''
result:
0 ['_', 'p']
1 ['_', 'r']
2 ['_', 'o']
3 ['_', 'v']
4 ['_', 'a']
'''

# show the hidden word
for i in word_dict:
    print(word_dict[0][0], end='')

# vars setting
step_num = 0
print(hangman_steps[step_num])

# core game
while step_num < 7:
    guess = input('what letter? > ')
    # os.system('clear')
    if not guess in word:
        step_num += 1
    print(hangman_steps[step_num])
    print(step_num)
