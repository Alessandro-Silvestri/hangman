import os
os.system('clear')

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




word_dict = {}
word = 'prova'
for i in range(len(word)):
    word_dict[i] = ['_', word[i]]

for i, j in word_dict.items():
  print(i, j)
quit()







step_num = 0
print(hangman_steps[step_num])
word_hidden = '*' * len(word)
print(word_hidden)

while step_num < 7:
    guess = input('what letter? > ')
    os.system('clear')
    if not guess in word:
        step_num += 1

    print(hangman_steps[step_num])
    print(word_hidden)
    print(step_num)
