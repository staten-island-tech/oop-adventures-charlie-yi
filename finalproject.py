import random



class Player:
    def __init__(self,name,ovr,pockets,attributes,fame,morale,energy,train,game,quit):
        self.name = name
        self.ovr = int(0)
        self.pockets = int(0)
        self.attributes = attributes
        self.fame = int(0)
        self.morale = morale
        self.energy = int(0)
        self.train = train
        self.game = game
        self.quit = quit


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
menu(my_player)
    