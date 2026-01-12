import random

class Item:
    def __init__(self,name,cost,value,morale,energy,train,game):
        self.name = name
        self.ovr = cost
        self.value = value
        self.morale = morale
        self.energy = int(100)




class Player:
    def __init__(self,name):
        self.name = name
        self.ovr = 0
        self.fame = 0
        self.energy = 100
        self.morale = 50 
        self.money = 10
        self.attributes = []
        self.inventory = []


def show_stats():
    print("stats")
    print("Name:",self.name)
    print("Ovr:",self.ovr)
    print("Energy:",self.energy)
    print("Money:",self.money)
    print("Fame:",self.fame)
    print("Morale", self.morale)


def main():
    name = input ("Enter player name")
    player = Player(name)
    store = store()
    while True:
        print("Main menu")
        print("1)stats")
        print("2)Train physical")
        print("3)Train skills")
        print("4)Pickup Game")
        print("5)Store")
        print("6)Recreation")
        print("7)inventory")
        print("8)quit")

        if choice == "1":
            player.show
        elif choice == "2":
        elif choice == "3":
        elif choice == "4":
        elif choice == "5":