
import random
# from player import Player

class Game:
    
    def __init__(self):
        self.Ai = "Ai" 
        self.player_one = "player_one"
           
        
    def run_game(self):
        self.greeting()
        self.rules_of_game()
        self.player_choice_rpsl("Rock","Paper""Scissors","Lizard","Spock")
        

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
        print("Choose 0 for Rock.")
        print("Choose 1 for Paper")
        print("Choose 2 for Scissors")
        print("Choose 3 for Lizard")
        print("choose 4 for Spock")
        print()
        print(input("Choose your gesture "))

    def name_to_number(self,name):
        if name == "Rock":
            return 0
        elif name == "Paper":
            return 1
        elif name == "Scissors":
            return 2
        elif name == "Lizard":
            return 3
        elif name == "Spock":
            return 4

    def number_to_name (self,number):
        if number == 0:
            return "Rock"
        elif number == 1:
            return "Paper"
        elif number == 2:
            return "Scissors"
        elif number == 3:
            return "Lizard"
        elif number == 4:
            return "Spock"
   

    def player_choice_rpsls(self,player_choice):
        self.player_choice = player_choice
        self.random.choice(self.gesture_list)
        print("The player chose" + player_choice)
        player_number = "name_to_number" (player_choice)
        print()  

    
        ai_number = random.randrange(0,5)
        player_number = (0,5)
        if ai_number - player_number % 5 == 0:
            outcome = "ai and human Tie!"
        elif ai_number - player_number % 5 > 2:
            outcome = "Player_one Wins!"
        else:
            outcome = "Ai Wins!"
        
        print(input("Would you like to play again? "))

    