valid_ans = 0
objective_score = 0

while objective_score < 13:
  while valid_ans == 0:
    try:
      if objective_score < 13:
        objective_score = int(input('Please enter a target score greater or equal to (13):\n'))
      else:
        valid_ans += 1
        print(f'You have selected {objective_score}')
        input('Press Enter to continue')
    except ValueError:
      print('This value is not an integer')

