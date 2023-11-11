import random
print("Welcome to Rock-paper-scissors game\n".upper)

print("Basic Rules:\n1. Paper covers rock- Paper choice wins over a rock choice\n2. Scissors cuts paper- Scissors choice wins over paper choice\n3. Rock smashes scissors- Rock choice wins over scissors choice\n")
print("Let the Game begin...\n")

#To repeat the operations
while True:

  #Receiving inputs from users
  user_choice = input("Make a choice: Paper or Scissors or Rock:__ ").upper()
  possible_choices = ["PAPER", "SCISSORS", "ROCK"]
  computer_choice = random.choice(possible_choices)

  if user_choice == computer_choice:
    print("\nYour choice is same with your player; the Computer,\nHence, No winner, It's a tie! ")

  elif user_choice == "rock".upper():
    if computer_choice =="scissors".upper():
      print("\nYour choice is ",user_choice, ", Computer choice is ",computer_choice, "\nHence, You win")
    else:
      print("\nYour player's choice is ",computer_choice, ":\nPaper covers rock, You lose! ")

  elif user_choice == "paper".upper():
    if computer_choice =="rock".upper():
      print("\nYour choice is ",user_choice, ", Computer choice is ",computer_choice, "\nHence, You win")
    else:
      print("\nYour player's choice is ",computer_choice, ":\nScissors cut paper, You lose! ")   

  elif user_choice == "scissors".upper():
    if computer_choice =="paper".upper():
      print("\nYour choice is ",user_choice, ", Computer choice is ",computer_choice, "\nHence, You win")
    else:
      print("\nYour player's choice is ",computer_choice, ":\nRock smashes scissors, You lose! ")  
  
  
  user_play_again = input("\nDo you want to play again? Select 1 or 2:\n1. Yes\n2. No:__")
  if user_play_again != "1":
      print("Thank you for using the App!")
      break
  
 



