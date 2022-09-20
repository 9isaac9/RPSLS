from random import choice
from player import Player

class Ai(Player):
    def __init__(self):
        super().__init__()
        self.gesture_list = {'Rock','Paper','Scissors','Lizard','Spock'}
    def select_gesture(self):
        self.random.choice(self.gesture_list)
        print(self.gesture_list)
