import random
# from player import Player

class Game:
    
    def __init__(self):
        self.player_one = "player_one"
        self.Ai = "Ai"   
        
    def run_game(self):
        self.greeting()
        self.rules_of_game = "rules"
        self.display_winner = "winner"

    def greeting(self):
        print("Welcome to RPSLS")

    def rules_of_game(self):
        print("Each match will be best of three games.  Use the number key to enter your selection")
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

        print(input("How many players 1,2,or 3 for a surprise?  "))

        print("Choose 0 for Rock.")
        print("Choose 1 for Paper")
        print("Choose 2 for Scissors")
        print("Choose 3 for Lizard")
        print("choose 4 for Spock")

        print(input("Choose your gesture"))

    def winner(self):
        self.ai_number()
        self.player_number()
        ai_number = random.randrange(0,5)
        player_number = "gesture_name; gesture_number"
        if ai_number - player_number % 5 == 0:
            outcome = "ai and human Tie!"
        elif ai_number - player_number % 5 > 2:
            outcome = "Player_one Wins!"
        else:
            outcome = "Ai Wins!"
        
        print(input("Would you like to play again? "))
