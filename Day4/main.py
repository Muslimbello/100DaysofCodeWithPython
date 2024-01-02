import random

user_input = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n")
)

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
if user_input > 2:
    if user_input > 2:
        raise ValueError("Please input a valid number (0, 1, or 2)")

rand_int = random.randint(0, 2)
map = [rock, paper, scissors]
users_choice = map[user_input]
computers_choice = map[rand_int]

if (
    (user_input == 2 and rand_int == 1)
    or (user_input == 1 and rand_int == 0)
    or (user_input == 0 and rand_int == 2)
):
    result = "You Win!"
elif user_input == rand_int:
    result = "Draw Try Again"
else:
    result = "You Lose Try Again"

print(users_choice)
print("computer choose:")
print(computers_choice)
print(result)
