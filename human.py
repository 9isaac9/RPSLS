from random import choice
from player import Player
class Human(Player):
    def __init__(self):
        super().__init__()
        

    def rpsls(self,player_choice,player_score):
        print()
        self.random.choice(self.gesture_list)
        print("The player chose" + player_choice)
        player_number = self.name_to_number (player_choice)
        player_score = 0 