###This program is a dice based game against an A.I opponent similar to blackjack - Created by Boston Setefano - Started 09/05/2024 - Finished __________###
import random
#Function that prints the game instructions
def instructions():
    print('''
----------------------------------------------------------------------------------------------------------------          
Roll-13 is a dice game similar to popular card game 'Blackjack' 

Before begining, you must decide on an overall score to reach (e.g. 50 or more)
The game will begin with both players rolling a pair of six-sided die
The sum of both die is added to your total score for that turn
Every subsequent roll for that round only uses one dice
The aim is to reach the target score of 13, or be closer than the A.I
          
At the start of your turn, you have the option to 'hold' or 'roll'
If you select 'hold', you will not roll that turn, and will not have the option to roll for the rest of the round
If you select 'roll', you will roll the dice and the score is added to your total
          
If you select to 'roll', and the number shown makes your score higher than 13, you lose the round
In the event of a loss, no points are added to your overall score
In the event of a win, the points you have for that round are added to the overall score.
On your first roll, if doubles are rolled, your winning score is doubled.
----------------------------------------------------------------------------------------------------------------
          ''')

print('-----------------------')
print('🎲Welcome to Roll-13🎲')
print('-----------------------\n')

read_instruct = input('Would you like to read the instructions? Y|N \n').lower()

#Repeats input until user enters a suitable responde
while read_instruct != 'y' and read_instruct != 'yes' and read_instruct != 'n' and read_instruct != 'no':
     print(f"You have entered '{read_instruct}'")
     read_instruct = input('This is an incorrect value, please respond with either Y|N \n').lower()

#Either shows the instructions or not depending on user input
if read_instruct == 'y' or read_instruct == 'yes':
    instructions()
elif read_instruct == 'n' or read_instruct == 'no':
    print('-------------------------------------------')
    print('You have opted not to read the instructions')
    input('Press enter to continue\n')

valid_ans = 0
objective_score = 0

while objective_score < 13:
  while valid_ans == 0:
    try:
      if objective_score < 13:
        objective_score = int(input('Please enter a target score greater or equal to (13):\n'))
      else:
        valid_ans += 1
        print(f'You have selected {objective_score}\n')
        input('Press Enter to continue\n')
    except ValueError:
      print('This value is not an integer\n')