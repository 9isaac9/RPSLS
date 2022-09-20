from random import choice
from player import Player
class Human(Player):
    def __init__(self):
        super().__init__()
        self.gesture_list =  ['Rock','Paper','Scissors','Lizard','Spock']

    def rpsls(self,player_choice):
        print()
        self.random.choice(self.gesture_list)
        print("The player chose" + player_choice)
        player_number = "name_to_number" (player_choice)