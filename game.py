
import random
from player import Player
from human import Human
from ai import Ai

class Game:
    
    def __init__(self):
        self.player_one = Human()
        self.player_two = Ai()
        
           
        
    def run_game(self):
        self.greeting()
        self.rules_of_game()
       
        
    def greeting(self):
        print("Welcome to RPSLS")

    def rules_of_game(self):
        print("Each match will be best of three games.Use the number key to enter your selection")
        print ("Scissor cut Paper")
        print("Paper covers Rock")
        print("Rock crushes Lizard")
        print("Lizard poisons Spock")
        print("Spock smashes Scissors")
        print("Scissors decapitate Lizard")
        print("Lizard eats Paper")
        print("Paper disproves Spock")
        print("Spock vaporizes Rock")
        print("Rock crushes Scissors")
        print()
        print(input("How many players 1,2,or 3 for a surprise? "))
        print()
    
   
player_score = 0
ai_score = 0


print("Rock","Paper","Scissors","Lizard","Spock")
while player_score < 3 and ai_score < 3:
    player_choice = input("\nChoose 'Rock','Paper','Scissors','Lizard','Spock' \n").upper()

    while player_choice not in ["Rock","Paper","Scissors","Lizard","Spock"]:
        player_choice = input("\nChoose 'Rock','Paper','Scissors','Lizard','Spock' \n")       
    ai_choice = random.choice(['Rock','Paper','Scissors','Lizard','Spock'])
    print("Player Choice:", player_choice)
    print("AI Choice:", ai_choice)

    if player_choice == "Rock" and ai_choice == "Paper":
        ai_score += 1
    elif player_choice == "Rock" and ai_choice== "Scissors":
        player_score += 1
    elif player_choice == "Rock" and ai_choice == "Lizard":
        ai_score += 1
    elif player_choice == "Rock" and ai_choice == "Spock":
        player_score += 1
    elif player_choice == "Paper" and ai_choice == "Rock":
        ai_score += 1
    elif player_choice == "Paper" and ai_choice == "Scissors":
        player_score += 1
    elif player_choice == "Paper" and ai_choice == "Lizard":
        ai_score += 1
    elif player_choice == "Paper" and ai_choice == "Spock":
        player_score += 1
    elif player_choice == "Sissors" and ai_choice == "Rock":
        ai_score += 1
    elif player_choice == "Scissors" and ai_choice == "Paper":
        player_score += 1
    elif player_choice == "Scissors" and ai_choice == "Lizard":
        ai_score += 1
    elif player_choice == "Scissor" and ai_choice == "Spock":
        player_score += 1
    elif player_choice == "Lizard" and ai_choice == "Rock":
        ai_score += 1
    elif player_choice == "Lizard"  and ai_choice == "Paper":
        player_score += 1
    elif player_choice == "Lizard" and ai_choice == "Scissors":
        ai_score += 1
    elif player_choice == "Lizard" and ai_choice == "Spock":
        player_score += 1
    elif player_choice == "Spock" and ai_choice == "Rock":
        ai_score += 1
    elif player_choice == "Spock" and ai_choice == "Paper":
        player_score += 1
    elif player_choice == "Spock" and ai_choice == "Scissors":
        ai_score += 1
    elif player_choice == "Spock" and ai_choice == "Lizard":
        player_score += 1
    else:
        print("Tie")
    print("Player_Score:",player_score)
    print("AI Score:",ai_score)

if player_score > ai_score:
    print("\nYou win!")
else:
    print("\nYou lose")
        
    print(input("Would you like to play again? "))


    