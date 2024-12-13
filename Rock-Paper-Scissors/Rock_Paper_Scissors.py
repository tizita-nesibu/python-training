# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 16:58:09 2024

Rock Paper Scissors game

@author: tizit
"""

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# 3 Rules of the game:
# Rock wins against scissors,
# scissors win against paper
# and paper wins against rock

rock_paper_scissors_img = [rock, paper, scissors]

player_choice = int(input("What do you choose? Type 0 for Rock, "
                         "1 for Paper or 2 for Scissors.\n"))
if player_choice >= 0 and player_choice <=2:
    print(rock_paper_scissors_img[player_choice])

computer_choice = random.randint(0,2)
print("Computer Chose:\n", rock_paper_scissors_img[computer_choice])

if player_choice >= 3 or player_choice < 0:
    print("You typed an invalid number, you Lose!")
elif player_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and player_choice == 2:
    print("You lose!")
elif computer_choice > player_choice:
    print("You lose!")
elif player_choice > computer_choice:
    print("You win!")
elif computer_choice == player_choice:
    print("It's a draw!")

