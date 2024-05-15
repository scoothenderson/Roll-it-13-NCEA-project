import random

#function that simulates rolling a die
def roll_die():
  result = random.randint(1, 6)
  return result

#testing roll_die
die_roll = roll_die()
print(die_roll)

#loops code for testing purposes
for i in range(1, 10):
    double_point = 0
    double_roll = 0
    
#runs the roll_die function twice
    roll_1 = roll_die()
    roll_2 = roll_die()

#check for doubles
    if roll_1 == roll_2:
      double_point += 1

#find the sum of both rolls
    double_roll = roll_1 + roll_2

#tell user their combined roll
    print(f"Dice 1: {roll_1}, Dice 2: {roll_2}, Total sum: {double_roll}")

#tell user if they have doubles
    if double_point == 1:
      print('You have rolled doubles! Double points opportunity!')






