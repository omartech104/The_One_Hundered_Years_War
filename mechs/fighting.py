import random
from mechs import traveling, shopping, inventory

# player stats
player_hp = 1500
player_hp = min(player_hp, 1500)
player_dp = 50
equipped_weapon = None

# enemy spawn points (city -> tile -> enemy types)
enemy_spawns = {
    "London": {
        "Crossroad": ["Bandit", "Thief"],
        "Docks": ["Thief", "Bandit"],
        "Castle": ["Templar"]
    },
    "Paris": {
        "Tavern": ["Bandit"],
        "Gatehouse": ["Thief"],
        "Cathedral": ["Templar"]
    },
    "Cairo": {
        "Oasis": ["Bandit"],
        "Citadel": ["Templar"],
        "Bazaar": ["Thief"]
    }
}


# enemy class
class Enemy:
    def __init__(self, kind):
        self.kind = kind
        self.dp = random.randint(80, 150)
        self.hp = random.randint(500, 1200)

    def cutscene(self):
        print(f"A {self.kind} appears at this location!")


# equip weapon system
def equip_weapon():
    global player_dp, equipped_weapon
    from mechs import shopping

    inv = shopping.inventory
    shops = shopping.shops

    if not inv:
        print("You have no weapons in your inventory!")
        return

    print("\nYour Weapons:")
    weapon_list = []
    for item in inv:
        for city in shops.values():
            if "Armory" in city and item in city["Armory"].keys():
                weapon_list.append(item)
                print(f"{len(weapon_list)}. {item} ({city['Armory'][item]['damage']} dmg)")

    if not weapon_list:
        print("You have no usable weapons (only items).")
        return

    choice = input("\nChoose a weapon to equip: ")

    if choice.isdigit() and 1 <= int(choice) <= len(weapon_list):
        weapon = weapon_list[int(choice) - 1]
        for city in shops.values():
            if "Armory" in city and weapon in city["Armory"]:
                equipped_weapon = weapon
                player_dp = city["Armory"][weapon]["damage"]
                print(f"\nYou equipped the {weapon}! Damage set to {player_dp}")
                return
    else:
        print("Invalid choice, you fight with fists.")
        equipped_weapon = None
        player_dp = 50


# player attacks enemy
def player_attack(enemy):
    damage = player_dp
    enemy.hp -= damage
    print(f"You hit the {enemy.kind} with {equipped_weapon or 'fists'} for {damage} damage!")
    if enemy.hp <= 0:
        print(f"The {enemy.kind} has been slain!")
        return True
    return False

def player_heal():
    global player_hp
    inventory.view_inventory()
    player_hp = min(player_hp, 1500)


# enemy attacks player
def enemy_attack(enemy):
    global player_hp
    damage = enemy.dp
    player_hp -= damage
    print(f"The {enemy.kind} attacked you for {damage} damage! Current HP: {player_hp}")
    if player_hp <= 0:
        print("You were slain... Game Over.")
        return True
    return False


# combat loop (returns whether enemy was killed, and loot)
def combat(enemy):
    global player_hp
    enemy.cutscene()
    equip_weapon()

    while player_hp > 0 and enemy.hp > 0:
        print(f"\nYour HP: {player_hp} | Enemy HP: {enemy.hp}")
        des = input("What do you do?\n1. Attack\n2. Heal\n3. Dodge\n> ")

        if des == "1":
            killed = player_attack(enemy)
            if killed:
                # ✅ Enemy drops loot
                loot = [f"{enemy.kind} Loot"]
                shopping.inventory.extend(loot)
                return enemy.kind, loot
            if random.random() < 0.8:
                if enemy_attack(enemy):
                    return None, []
        elif des == "2":
            pass
        elif des == "3":
            if random.random() > 0.5:
                print("You dodged the attack successfully!")
            else:
                print("Dodge failed!")
                if enemy_attack(enemy):
                    return None, []
        else:
            print("Invalid choice! The enemy takes the chance to strike...")
            if enemy_attack(enemy):
                return None, []

    return None, []


# check if enemy spawns on current tile
def check_for_enemy():
    city = traveling.current_city
    row, col = traveling.player_pos
    tile = traveling.current_map[row][col]

    if city in enemy_spawns and tile in enemy_spawns[city]:
        possible_enemies = enemy_spawns[city][tile]
        enemy_kind = random.choice(possible_enemies)
        enemy = Enemy(enemy_kind)
        return combat(enemy)  # ✅ returns (defeated_enemy, looted_items)

    else:
        print("The area is quiet. No enemies here.")
        return None, []
