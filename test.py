import random

class Item:
    def __init__(self, name, cost, effect, value, morale=0):
        self.name = name
        self.cost = cost
        self.effect = effect
        self.value = value
        self.morale = morale

class Player:
    def __init__(self, name):
        self.name = name
        self.ovr = 0
        self.energy = 100
        self.morale = 50
        self.fame = 0
        self.money = 10
        self.rank = 1
        self.inventory = []

    def location(self):
        return ["Slums","Local League","NCAA","G League","NBA","Hall of Fame"][self.rank-1]

    def can_rank_up(self):
        return self.rank<6 and self.fame>=self.rank*20 and self.ovr>=self.rank*20

    def rank_up(self):
        if self.can_rank_up():
            self.rank += 1
            print("\n--- Rank Up! ---")
            print("You advanced to:", self.location())
            dialogues = {
                2:"Georgie: Congrats kid, welcome to the Local League! Keep grinding.",
                3:"Johnathan: Proud of you! NCAA awaits.\nGeorgie: Couldn't have done it without your dedication!",
                4:"Father: We're so proud!\nMother: Keep pushing, you've got this!",
                5:"Georgie: NBA! You made it!\nFather & Mother: Our boy!\nJayce: Let's celebrate!",
                6:"Hall of Fame! Your journey ends here. Congratulations!"
            }
            print(dialogues.get(self.rank,""))
        else:
            print("Requirements not met for rank up (OVR or Fame too low)")

    def show_stats(self):
        print(f"\n--- Stats ---")
        print(f"Name: {self.name} | OVR: {self.ovr} | Energy: {self.energy} | Morale: {self.morale} | Fame: {self.fame} | Money: {self.money} | Location: {self.location()}")

    def show_inventory(self):
        if not self.inventory:
            print("Inventory empty")
        for i,item in enumerate(self.inventory):
            print(i,"-",item.name)

    def use_item(self, idx):
        if 0<=idx<len(self.inventory):
            item = self.inventory.pop(idx)
            if item.effect=="energy": self.energy = min(100,self.energy+item.value)
            if item.effect=="morale": self.morale = min(100,self.morale+item.value)
            if item.morale>0: self.morale = min(100,self.morale+item.morale)
            print(f"Used {item.name}")

    def train_physical(self):
        if self.energy<10: print("Not enough energy"); return
        gain=random.randint(1,3)
        self.ovr += gain
        self.energy -= 10
        print("Physical training. OVR +", gain)
        self.random_event()

    def train_skills(self):
        if self.morale<10: print("Too demotivated"); return
        gain=random.randint(1,3)
        self.ovr += gain
        self.morale -= 10
        print("Skills training. OVR +", gain, "Morale -10")
        self.random_event()

    def pickup_game(self):
        if self.energy<10: print("Too tired"); return
        opp = self.ovr + random.randint(-5,5)
        print("\nPickup game vs OVR",opp)
        print("1) Drive  2) Shoot  3) Pass")
        input("> ")
        chance = 50+(self.ovr-opp)
        if random.randint(1,100)<=chance:
            perf = max(1,(self.ovr-opp)//5+1)
            self.money += perf*3
            self.fame += 5
            self.morale = min(100,self.morale+2)
            print("Score! Money +",perf*3,"Fame +5 Morale +2")
        else:
            self.morale -= 2
            print("Missed. Morale -2")
        self.energy -= 10
        self.random_event()

    def recreation(self, cost):
        if self.money<cost: print("No money"); return
        self.money -= cost
        self.morale = min(100,self.morale+random.randint(4,8))
        self.energy = min(100,self.energy+random.randint(2,5))
        print("Recreation complete")
        self.random_event()

    def random_event(self):
        r=random.randint(1,10)
        if r==1: self.ovr+=1; print("Random event: Breakthrough! OVR +1")
        if r==2: self.morale-=2; print("Random event: Bad day. Morale -2")
        if r==3: found=random.randint(1,5); self.money+=found; print("Random event: Found $",found)
        if r==4: self.fame+=3; print("Random event: Spotted in park! Fame +3")

class Store:
    def __init__(self):
        self.items = [
            Item("Energy Drink",3,"energy",10),
            Item("Hot Dog",5,"energy",15,1),
            Item("Protein Bar",7,"energy",20),
            Item("Soda",2,"morale",3)
        ]

    def open(self, player):
        print("\n--- Store ---")
        for i,item in enumerate(self.items):
            print(f"{i}) {item.name} - ${item.cost}")
        choice=input("Type item number to buy or 'back': ")
        if choice.isdigit():
            idx=int(choice)
            if 0<=idx<len(self.items):
                item=self.items[idx]
                if player.money>=item.cost:
                    player.money-=item.cost
                    player.inventory.append(item)
                    print(f"Bought {item.name}!")
                else:
                    print("Not enough money")
                    
    #enumurate is for the numbered list. Append sends the item to Inventory list. Got my cousins help.

def main():
    name=input("Enter your player name: ")
    p=Player(name)
    store=Store()
    print("You are a kid in the Slums with hoop dreams.Can you make it out?")

    while True:
        print("Main Menu")
        print("1) Stats  2) Train Physical  3) Train Skills  4) Pickup Game")
        print("5) Store  6) Recreation  7) Inventory  8) Rank Up  9) Quit")
        choice=input("> ")

        if choice=="1": p.show_stats()
        elif choice=="2": p.train_physical()
        elif choice=="3": p.train_skills()
        elif choice=="4": p.pickup_game()
        elif choice=="5": store.open(p)
        elif choice=="6": p.recreation(5)
        elif choice=="7":
            p.show_inventory()
            if p.inventory:
                u=input("Use item index or 'back': ")
                if u.isdigit(): p.use_item(int(u))
        elif choice=="8": p.rank_up()
        elif choice=="9": break
#menu ui took a long time haha.
main()

#p is to reference the class apparently, so it grabs the function from the class and has it in the main.