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
----'   ____)____
          ______)
          _______)
         _______)
----.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock,paper,scissors]
choice = int(input("Enter the choice here : 0 for rock,1 for paper and 2 for scissor : "))
print(f"your choice is {game_images[choice]}")
computer_choice = random.randint(0,2)
print(f"Computer chose {game_images[computer_choice]}")
if choice ==0 and computer_choice == 2:
    print("You win!")
elif computer_choice==0 and choice == 2:
    print("You lose")
elif computer_choice>choice:
    print("You lose")
elif computer_choice<choice:
    print("You win")
elif computer_choice==choice:
    print("Its a draw")
elif choice>=3 or choice<0:
    print("You typed an invalid number, you lose")