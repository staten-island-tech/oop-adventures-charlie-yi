import random



class Player:
    def __init__(self,name,ovr,pockets,attributes,fame):
        self.name = name
        self.ovr = int(0)
        self.pockets = int(0)
        self.attributes = attributes
        self.fame = int(0)
name = input ("What would you like to name your player")
my_Player = Player(f"{name}")
