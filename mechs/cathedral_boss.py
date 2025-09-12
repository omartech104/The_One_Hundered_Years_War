import random
from mechs import fighting, shopping, inventory
from .puzzles import cipher

boss_hp = 1500
boss_attack = (50, 250)  # random attack range
equipped_weapon = None
equipped_damage = 50  # fists by default
defeated = False  # ✅ boss state is tracked


def equip_weapon():
    global equipped_weapon, equipped_damage

    if not shopping.inventory:
        print("You have no items in your inventory!")
        return

    # Filter inventory for weapons (items found in any Armory)
    weapon_list = []
    for item in shopping.inventory:
        for city in shopping.shops.values():
            if "Armory" in city and item in city["Armory"]:
                weapon_list.append((item, city["Armory"][item]["damage"]))

    if not weapon_list:
        print("You have no usable weapons. Fighting with fists (50 dmg).")
        equipped_weapon = None
        equipped_damage = 50
        return

    print("\nChoose a weapon to equip:")
    for idx, (weapon, dmg) in enumerate(weapon_list, 1):
        print(f"{idx}. {weapon} ({dmg} dmg)")

    choice = input("> ").strip()
    if choice.isdigit():
        choice = int(choice) - 1
        if 0 <= choice < len(weapon_list):
            equipped_weapon, equipped_damage = weapon_list[choice]
            print(f"You equipped {equipped_weapon}! Damage set to {equipped_damage}")
            return

    print("Invalid choice. Fighting with fists (50 dmg).")
    equipped_weapon = None
    equipped_damage = 50


def fight_cathedral_boss():
    global boss_hp, defeated

    if defeated:  # ✅ prevents multiple fights
        print("\nThe Cathedral Guardian has already been defeated.")
        return

    print("\nYou enter the dark Cathedral. A towering knight, the Guardian of Shifts, blocks your way!")

    # Let player pick weapon
    equip_weapon()

    while boss_hp > 0 and fighting.player_hp > 0:
        print(f"\nYour HP: {fighting.player_hp} | Boss HP: {boss_hp}")
        print("1. Attack")
        print("2. Use Item")
        print("3. Run")

        choice = input("> ").strip()

        if choice == "1":
            damage = equipped_damage
            boss_hp -= damage
            print(f"You strike the Cathedral Guardian with {equipped_weapon or 'fists'} for {damage} damage!")

        elif choice == "2":
            if not shopping.inventory:
                print("Your inventory is empty!")
            else:
                print("\nChoose an item to use:")
                for idx, item in enumerate(shopping.inventory, 1):
                    print(f"{idx}. {item}")
                item_choice = input("> ").strip()
                if item_choice.isdigit():
                    item_choice = int(item_choice) - 1
                    if 0 <= item_choice < len(shopping.inventory):
                        inventory.use_item(shopping.inventory[item_choice])  # ✅ fixed import
                    else:
                        print("Invalid choice.")
                else:
                    print("Invalid input.")

        elif choice == "3":
            print("You flee from the Cathedral... but the boss awaits still.")
            defeated = False
            return

        else:
            print("Invalid choice.")
            continue

        # Boss counterattacks if still alive
        if boss_hp > 0:
            boss_damage = random.randint(*boss_attack)
            fighting.player_hp -= boss_damage
            print(f"The Guardian smashes you for {boss_damage} damage!")

    if fighting.player_hp <= 0:
        print("\nYou were slain by the Cathedral Guardian...")
        defeated = False
    else:
        print("\nYou defeated the Cathedral Guardian!")
        post_boss_event()
        defeated = True  # ✅ boss stays defeated


def post_boss_event():
    print("\nAs the Guardian falls, his voice echoes in the cathedral halls...")
    print('"The amount of shifts... is 3..."')
    print("\nA chest appears before you. It seems to need a number to open.")

    attempt = input("Enter the number: ").strip()
    if attempt == "3":
        print("\nThe chest clicks open...")
        inventory.content = cipher.message
        print(f"You obtained the real message")
        shopping.player_gold += 355
    else:
        print("\nThe chest remains sealed... Maybe try again later.")

