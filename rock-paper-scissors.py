import random
rock='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper='''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images=[rock,paper,scissors]
user_choice=int(input("What do you choose?\nType 0 for ROCK, 1 for PAPER or 2 for SCISSORS\n"))
print(game_images[user_choice])

computer_choice=random.randint(0,2)
print("Computer choice:\n")
print(game_images[computer_choice])

if user_choice>=3 or user_choice<0:
    print("You chose and INVALID number")
elif user_choice==0 and computer_choice==2:
    print("You WIN!")
elif computer_choice==0 and user_choice==2:
    print("You LOSE!")
elif user_choice > computer_choice:
    print("You WIN!")
elif user_choice < computer_choice:
    print("You LOSE!")
elif user_choice==computer_choice:
    print("It's a DRAW")
elif user_choice>=3 or user_choice<0:
    print("You chose and INVALID number")
