import os
import sys

from mechs import shopping, traveling, NPC

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
        draw()
        print("1. NEW GAME")
        # We'll work on loading savefile later
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
            pass
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
        draw()
        print()
        draw()
        print("1. Travel to another city")
        print("2. Visit the shop")
        print("3. Move inside the city (N/S/E/W)")
        print("4. Quit to Menu")
        draw()
        print()

        action = input("# ")

        # ---- Travel ----
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
                    traveling.player_pos = (2, 3)  # London start
                elif destination == "Paris":
                    traveling.current_map = traveling.paris_map
                    traveling.player_pos = (2, 3)  # Paris start
                elif destination == "Cairo":
                    traveling.current_map = traveling.cairo_map

                print(f"You have traveled to {destination}.")
            else:
                print("Invalid city.")
            input("> Press Enter...")

        # ---- Move inside city ----
        elif action == "3":
            clear_screen()
            draw()
            print("Which direction do you want to move?")
            print("N - North")
            print("S - South")
            print("E - East")
            print("W - West")
            draw()
            direction = input("# ").upper()

            if direction in ["N", "S", "E", "W"]:
                result = traveling.move(direction)
                print(result)
            else:
                print("Invalid direction.")
            input("> Press Enter...")
        elif action == "2":
            shopping.open_shop()
        elif action == "4":
            play=False
            menu=True
