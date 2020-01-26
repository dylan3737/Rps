#random integer for computer choice
import random

#Function to play Rock, Paper, Scissors
def rock_paper_scissors():
    print("Let's play Rock, Paper, Scissors!")

#Player Choice
    player_choice = input("Would you like to pick Rock, Paper, or Scissors? : ").capitalize()
    print("Player picks " + player_choice)

#Computer Choice
    computer_choices = ["Rock", "Paper", "Scissors"]
    computer_choice = (random.randint(0,2))
    print("Computer picks " + computer_choices[computer_choice])


#if statements to determine winner
    if(player_choice == "Rock" and computer_choice == 0):
        print("The game is a tie")
    if (player_choice == "Paper" and computer_choice == 1):
        print("The game is a tie")
    if (player_choice == "Scissors" and computer_choice == 2):
        print("The game is a tie")

    if (player_choice == "Rock" and computer_choice == 1):
        print("Computer wins.")
    if (player_choice == "Paper" and computer_choice == 2):
        print("Computer wins.")
    if (player_choice == "Scissors" and computer_choice == 0):
        print("Computer wins.")

    if (player_choice == "Rock" and computer_choice == 2):
        print("Player wins.")
    if (player_choice == "Paper" and computer_choice == 0):
        print("Player wins.")
    if (player_choice == "Scissors" and computer_choice == 1):
        print("Player wins.")
#--------------------------------------------------------------

rock_paper_scissors()


