import random
print("Welcome to Rock Paper Scissor")
print("Let's begin the game")
user_choice = int(input("Enter your choice: \n0 for Rock \n1 for Paper \n2 for Scissor \n")) 
computer_choice = random.randint(0, 2)
print (f"Your choice: {user_choice} \nComputer choice: {computer_choice}")
if user_choice < 0 or user_choice > 2:
     print("Invalid choice, You lost! \nPlay Again")
elif user_choice == 1 and computer_choice == 2:
    print("You Won! \nPlay Again")
elif user_choice == 2 and computer_choice == 0: 
    print("You Lost! \nComputer Won\nPlay Again")
elif user_choice < computer_choice:
    print("You Lost! \nComputer Won\nPlay Again") 
elif user_choice> computer_choice:
   print("You Won! \nPlay Again")
elif user_choice == computer_choice:
   print("The game is draw \nPlay Again!")
