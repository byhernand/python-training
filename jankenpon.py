# Rock, paper and scissors game.

import random

def play():
  rock = 'rock'
  paper = 'paper'
  scissors = 'scissors'
  options = [rock, paper, scissors]

  user_choice = input('Choose a number: \n1: Rock\n2: Paper\n3: Scissors\n‣ ')
  user_choice = options[int(user_choice) - 1]
  pc_choice = options[random.randint(0, 2)]

  print(f'You choose "{user_choice}".')
  print(f'PC choose "{pc_choice}".')

  result = None

  if user_choice == pc_choice:
    print("It's a draw.")
    return
  elif user_choice == rock:
    result = 'win' if pc_choice != paper else 'lose'
  elif user_choice == paper:
    result = 'win' if pc_choice != scissors else 'lose'
  elif user_choice == scissors:
    result = 'win' if pc_choice != rock else 'lose'

  print(f'You {result}!')


play()