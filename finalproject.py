import random
from typing import Self



class Player:
    def __init__(self,name,ovr,pockets,attributes,fame,morale,energy,train,game,quit):
        self.name = name
        self.ovr = int(0)
        self.pockets = int(50)
        self.attributes = []
        self.fame = int(0)
        self.morale = morale
        self.energy = int(100)
        self.train = train
        self.game = game
        self.quit = quit
       
    def train(player):
        valid = True
    training = input("1)Train in the gym by yourself 2)Lift weights 3)Work on conditioning""Choose what would you like to do")
    if training == "1":
        Player.ovr += 1 
        Player.energy -= 10
        print(f"after working in the gym {Player.name} gained 1 ovr but loses 10 energy")
    elif training == "2":
        Player.ovr += 1
        Player.energy -= 10
        print(f"after lifting weights {Player.name} gained 1 ovr but loses 10 energy")
    elif training == "3":
        Player.ovr += 1
        player.energy -= 10
        print(f"after working on conditioning {Player.name} gained 1 ovr but loses 10 energy")
    else:
        print("You must choose 1,2,or 3")
    print (f"Happiness: {self.ovr}  Tiredness: {self.energy}")






        








name = input ("Welcome to the Career what would you like to name your player" )
my_player = Player(f"{name}")
print("Slums, you are just a kid in the Slums that had hoop dreams, until Georgie came to you and asked if you really wanted to get out and pursue the high life.")
def menu(my_player):
    play=True
    while play == True:
        print("1)Train with geogie")
        print("2)earn enegry")
        print("3)Play basketball game")
        print("4)quit")
        y = input("what would you like to do")
        if y == "1":
            Player.train(my_train)
        elif y == "2":
            Player.energy(my_energy)
        elif y == "3":
            Player.game(my_game)
        elif y == "4":
            break
        else:
            print("You have to choose 1,2,3, or 4")
        self.random_value = random.randint(1,2)
        if random == 1:
            print("A event has spawned")
        elif random == 2:
            print
menu(my_player)
    
