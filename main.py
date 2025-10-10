import os
import sys

from mechs import NPC, ascii_art, badges, fighting, inventory, quest, shopping, traveling
from mechs.quest import start_quest

pltform = sys.platform


# Clear screen based on OS
def clear_screen():
    if pltform in ("linux", "darwin"):
        os.system("clear")
    elif pltform == "win32":
        os.system("cls")


run = True
menu = True
play = False
rules = False


def draw():
    print("xX--------------------xX")


while run:
    while menu:
        clear_screen()
        ascii_art.welcome_screen()
        draw()
        print("1. NEW GAME")
        print("2. LOAD GAME")
        print("3. RULES")
        print("4. QUIT GAME")
        draw()

        if rules:
            print("Play the game cleanfully")
            rules = False
            input("> ")
            choice = ""
        else:
            choice = input("# ")

        if choice == "1":
            menu = False
            play = True
        elif choice == "2":
            print("Load feature not implemented yet.")
            input("> Press Enter...")
        elif choice == "3":
            clear_screen()
            rules = True
        elif choice == "4":
            clear_screen()
            print("Farewell, Hero")
            quit()
        else:
            print("Insert a valid command")

    while play:
        clear_screen()
        draw()
        print(traveling.get_tile_description())

        NPC.check_for_npcs(traveling.current_city, traveling.get_current_tile())
        if (traveling.current_city, traveling.get_current_tile()) == ("Paris", "Cathedral"):
            start_quest("Lost Relic")

        if (traveling.current_city, traveling.get_current_tile()) == ("Cairo", "Bazaar"):
            start_quest("Missing Ring")

        if (traveling.current_city, traveling.get_current_tile()) == ("London", "Docks"):
            start_quest("Smuggled Goods")

        if (traveling.current_city, traveling.get_current_tile()) == ("London", "Crossroad"):
            start_quest("Crossroad Ambush")

        if (traveling.current_city, traveling.get_current_tile()) == ("London", "Castle"):
            start_quest("Castle Intruder")

        if (traveling.current_city, traveling.get_current_tile()) == ("Paris", "Tavern"):
            start_quest("Tavern Brawl")

        if (traveling.current_city, traveling.get_current_tile()) == ("Paris", "Gatehouse"):
            start_quest("Gatehouse Thief")

        if (traveling.current_city, traveling.get_current_tile()) == ("Paris", "Cathedral"):
            start_quest("Defender of the Faith")

        if (traveling.current_city, traveling.get_current_tile()) == ("Cairo", "Oasis"):
            start_quest("Oasis Raid")

        if (traveling.current_city, traveling.get_current_tile()) == ("Cairo", "Citadel"):
            start_quest("Citadel Intrigue")

        if (traveling.current_city, traveling.get_current_tile()) == ("Cairo", "Bazaar"):
            start_quest("Bazaar Pickpocket")

        if (traveling.current_city, traveling.get_current_tile()) == ("London", "Crossroad"):
            start_quest("Highway Robbery")

        if (traveling.current_city, traveling.get_current_tile()) == ("London", "Docks"):
            start_quest("Stolen Cargo")

        if (traveling.current_city, traveling.get_current_tile()) == ("London", "Castle"):
            start_quest("Knight’s Oath")

        if (traveling.current_city, traveling.get_current_tile()) == ("Paris", "Tavern"):
            start_quest("Drunken Raiders")

        if (traveling.current_city, traveling.get_current_tile()) == ("Paris", "Gatehouse"):
            start_quest("City Gate Break-in")

        if (traveling.current_city, traveling.get_current_tile()) == ("Cairo", "Oasis"):
            start_quest("Desert Justice")


        draw()
        print()
        draw()
        print("1. Travel to another city")
        print("2. Go to the Center of city")
        print("3. Visit the shop")
        print("4. Move inside the city (N/S/E/W/Fast-travel)")
        print("5. Open inventory")
        print("6. View badges")
        print("7. Quit to Menu")
        draw()
        print()

        action = input("# ")

        if action == "1":
            print("Where do you want to travel?")
            for city in traveling.cities:
                if city != traveling.current_city:
                    print(f"- {city}")
            destination = input("# ")

            if destination in traveling.cities:
                traveling.current_city = destination

                # Update map and player position based on city
                if destination == "London":
                    traveling.current_map = traveling.london_map
                    traveling.player_pos = (2, 3)
                elif destination == "Paris":
                    traveling.current_map = traveling.paris_map
                    traveling.player_pos = (2, 3)
                elif destination == "Cairo":
                    traveling.current_map = traveling.cairo_map
                    traveling.player_pos = (2, 3)

                print(f"You have traveled to {destination}.")
                print(f"Do you want to view {destination}'s map (y/n)")
                map_input = input("# ")
                if map_input == "y":
                    draw()
                    for row in traveling.current_map:
                        print(" ".join(traveling.symbols[tile] for tile in row))
                    draw()
            else:
                print("Invalid city.")
            input("> Press Enter...")

        elif action == "2":
            if traveling.current_map == traveling.london_map:
                traveling.player_pos = (2, 3)
            elif traveling.current_map == traveling.paris_map:
                traveling.player_pos = (2, 3)
            elif traveling.current_map == traveling.cairo_map:
                traveling.player_pos = (3, 2)
            print(f"You're in the heart of {traveling.current_city}")
            input("> Press Enter...")
        elif action == "3":
            shopping.open_shop()

        elif action == "4":
            clear_screen()
            draw()
            print("Which direction do you want to move?")
            print("N - North")
            print("S - South")
            print("E - East")
            print("W - West")
            print("F - Fast Travel")
            draw()
            direction = input("# ").upper()

            if direction in ["N", "S", "E", "W"]:
                result = traveling.move(direction)
                print(result)

                NPC.check_for_npcs(traveling.current_city, traveling.get_current_tile())

                # Trigger quest enemy if present
                quest_enemy_fought = False
                for q_name in quest.quests.keys():
                    enemy_name = quest.trigger_quest_enemy(q_name, traveling.current_city, traveling.get_current_tile())
                    if enemy_name:
                        enemy_obj = fighting.Enemy(enemy_name)
                        defeated_enemy, looted_items = fighting.combat(enemy_obj)
                        quest.check_quest_progress(
                            q_name,
                            traveling.current_city,
                            traveling.get_current_tile(),
                            defeated_enemy,
                            looted_items,
                        )
                        quest_enemy_fought = True
                        break

                # Only check for random enemies if no quest enemy was fought
                if not quest_enemy_fought:
                    defeated_enemy, looted_items = fighting.check_for_enemy()
                    if defeated_enemy:
                        for q_name in quest.quests.keys():
                            quest.check_quest_progress(
                                q_name,
                                traveling.current_city,
                                traveling.get_current_tile(),
                                defeated_enemy,
                                looted_items,
                            )

            elif direction == "F":
                traveling.fast_travel()
                NPC.check_for_npcs(traveling.current_city, traveling.get_current_tile())

                quest_enemy_fought = False
                for q_name in quest.quests.keys():
                    enemy_name = quest.trigger_quest_enemy(q_name, traveling.current_city, traveling.get_current_tile())
                    if enemy_name:
                        enemy_obj = fighting.Enemy(enemy_name)
                        defeated_enemy, looted_items = fighting.combat(enemy_obj)
                        quest.check_quest_progress(
                            q_name,
                            traveling.current_city,
                            traveling.get_current_tile(),
                            defeated_enemy,
                            looted_items,
                        )
                        quest_enemy_fought = True
                        break

                if not quest_enemy_fought:
                    defeated_enemy, looted_items = fighting.check_for_enemy()
                    if defeated_enemy:
                        for q_name in quest.quests.keys():
                            quest.check_quest_progress(
                                q_name,
                                traveling.current_city,
                                traveling.get_current_tile(),
                                defeated_enemy,
                                looted_items,
                            )
            else:
                print("Invalid direction.")
            input("> Press Enter...")

        elif action == "5":
            inventory.view_inventory()
            

        elif action == "6":
            badges.view_badges()
            input("> Press Enter...")

        elif action == "7":
            play = False
            menu = True
