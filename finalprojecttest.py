import random

class player:
    def __init__(self,name,ovr,pockets,attributes,fame,morale,energy,train,game,quit):
        self.name = name
        self.ovr = int(0)
        self.pockets = int(0)
        self.attributes = []
        self.fame = int(0)
        self.morale = morale
        self.energy = int(0)
        self.train = train
        self.game = game
        self.quit = quit

class Npc:
    def __init__(self,name):
        self.name = name
        
def menu():
     print("Slums, you are just a kid in the Slums that had hoop dreams, until Georgie came to you and asked if you really wanted to get out and pursue the high life.")
     while True:
        print("What would you like to do next? (1) View Player Stats (2) Train Player (3) Talk to NPCs (4) Play a game (5) Quit")
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            display_stats(player)
        elif choice == '2':
            train(player)
        elif choice == '3':
            interact(player)
        elif choice == '4':
            game(player)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
   

def game(player):
    print("Scrim in progress...")
    if player.ovr >= 85:
        print(f"{player.name} performed excellently in the scrim!")
        print(f"Reward: +{random.randint(50,100)}$ to Pockets")
    elif player.ovr <= 75:
        print(f"{player.name} got whooped.")
        train_player(player)
    else:
        print(f"Scrim did not go so well...")
        train_player(player)
        

if __name__ == "__main__":
    menu()

