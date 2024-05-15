import random

def roll_die():
  result = random.randint(1, 6)
  return result

die_roll = roll_die()
print(die_roll)

for i in range(1, 10):
    double_point = 0
    double_roll = 0

    roll_1 = roll_die()
    roll_2 = roll_die()

    if roll_1 == roll_2:
      double_point += 1

    double_roll = roll_1 + roll_2

    print(f"Dice 1: {roll_1}, Dice 2: {roll_2}, Total sum: {double_roll}")

    if double_point == 1:
      print('You have rolled doubles! Double points opportunity!')






