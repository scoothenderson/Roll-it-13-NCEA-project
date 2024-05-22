import random

#function that simulates rolling a die
def roll_die():
  result = random.randint(1, 6)
  return result
#function that simulates rolling a pair of dice
def first_roll():
    double_opport = 0
    double_score = 0
    
#runs the roll_die function twice
    roll_1 = roll_die()
    roll_2 = roll_die()

#check for doubles
    if roll_1 == roll_2:
      double_opport += 1

#find the sum of both rolls
    double_score = roll_1 + roll_2

#tell user their combined roll
    print(f"Dice 1: {roll_1}, Dice 2: {roll_2}, Total sum: {double_score}")

    return double_opport, double_score

#Main function begins here

input('''
-----------------------------------
Press Enter to continue to the game
-----------------------------------''')

#run first_roll function, seperate two returned values into variables
user_first = first_roll()
user_doubles = user_first[0]
user_score = user_first[1]

#tell user if they have double points opportunity
if user_doubles == 1:
  print('You have rolled doubles! Double points opportunity!\n')

input('Press Enter to continue\n')

#run first roll function for computer
print('The A.I is now rolling...\n')
ai_first = first_roll()
ai_score = ai_first[1]


hold = 0
#will stop looping the code once the user or computer reaches or goes above 13
while user_score < 13 and ai_score < 13:
   print(f'You have a score of {user_score}, the A.I has a score of {ai_score}\n')
   hold_or_roll = ''
   
   #continuely loops input until suitable value is entered 
   if hold != 1:
     while hold_or_roll != 'hold' and hold_or_roll != 'roll':
        hold_or_roll = input('Would you like to hold or roll? (Enter "hold" or "roll")\n').lower()
   
   #rolls dice if user input 'roll' and adds it to score
   if hold_or_roll == 'roll':
      user_roll = roll_die()
      user_score += user_roll
      print('You have chosen to roll\n')
      print(f'You rolled a {user_roll}\n')
      input('Press Enter to end your turn\n')
   #if user entered 'hold', removes ability to roll in future rounds
   else:
      hold += 1
      print('You have chosen to hold, you can no longer roll for the remainder of the round\n')
      input('Press Enter to end your turn\n')
   #will roll dice for a.i if both players scores are still below 13 and add roll to total score
   if user_score < 13 and ai_score < 13:
     print('The A.I is now rolling...\n')
     ai_roll = roll_die()
     ai_score += ai_roll
     print(f'It rolled a {ai_roll}\n')
     input("Press Enter to continue\n")

#prints results once round is finished
print('---------------Round Results----------------')
print('The round is over\n')
print(f'A.I score: {ai_score}, Your score: {user_score}')

#decides who wins the round
if ai_score > user_score and ai_score <= 13:
   print('The A.I wins!\n')
   input('Press Enter to continue\n')
elif ai_score < user_score and ai_score > 13 and user_doubles == 1 and user_score <= 13:
   user_score *= 2
   print('You win the round!\n')
   print(f'Since you rolled doubles, your score is now doubled to: {user_score}')
elif user_score > 13:
   print('The A.I wins!\n')
   input('Press Enter to continue\n')
else:   
   print('You win the round!')
