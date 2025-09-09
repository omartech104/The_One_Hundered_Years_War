from mechs import shopping

inv = shopping.inventory
import random

player_hp = 3000
player_dp = 0




class Enemy:
    def __init__(self,kind, dp, hp):
        self.kind = random.choice(["templar", "theif", "bandit"])
        self.dp = dp
        self.hp = hp

    def cutsence():
        # placeholder names, change them to be more aggressive
        if not msg:
            msg = random.choice([
                "Greetings, traveler.",
                "The roads are dangerous, beware.",
                "Have you heard the latest news?",
                "Supplies are scarce these days.",
                "May fortune smile upon you."
            ])
    
    # add the logic form the distribution of enemies
    # then feel free to add additional functions


weapon = input("Select a weapon:")


# i will do this part 
for item in inv:
    if weapon == item:
        pass

        


def player_attack():
    enemy_hp -= player_dp
    print("You attacked the enemy, you dealt some damage")
    if enemy_hp <= 0:
        print("Good Job, You killed the enemy")

def player_heal():
    player_hp += 200 

def enemy_attack():
    pass

def enemy_heal():
    player_hp += 20

def player_dodge():
    pass

def contact():
    des = input("An enemy is approaching, what should you do\n 1. -Attack \n 2. -Heal \n 3. -Dodge")

    if des == "1":
        player_attack()
        random.choice(enemy_attack(), enemy_heal())
    if des == "2":
        player_heal()
    if des == "3":
        player_dodge()






    
