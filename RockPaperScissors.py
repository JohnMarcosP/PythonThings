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

#Write your code below this line 👇

input = int(input("What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors."))
if input == 0:

  print(rock)

elif input == 1:
  print(paper)
elif input == 2:
  print(scissors)
else:
  print("Wrong Choice!")

print("Computer choose:")
computer = random.randint(0,2)
if computer == 0:
  print(rock)
  if input == 1:
    print("You win!")
  elif input == 0:
    print("Draws")
  else:
    print("You lose")
elif computer == 1:
  print(paper)
  if input == 2:
    print("You win!")
  elif input == 0:
    print("You lose!")
  else:
    print("Draw")
elif computer == 2:
  print(scissors)
  if input == 0:
    print("You win!")
  elif input == 1:
    print("You lose")
  else:
    print("Draw")