word_list = ['rainbow', 'computer', 'science', 'programming',
            'python', 'mathematics', 'player', 'condition',
            'reverse', 'water', 'board', 'geeks']

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']



import random 
word = random.choice(word_list)
print("Computer choose: ", word)

display = ['__' for i in range(len(word))]
print(*display)

lives = 6

is_on =True
while is_on and lives>0:
    print(stages[lives])
    guess = input("Enter a letter: ").lower()
    for i in range(len(word)):
        if guess==word[i]:
            display[i] = str(guess)

    if guess not in word:
        lives -= 1
        
    if "__" not in display:
        print("You won!!")
        is_on = False

    print(*display)

else:
    print(stages[0])
    print("\n\nSorry pal, You were hanged!!")



