import os
import sys
from rich.console import Console
from rich.text import Text
from rich.panel import Panel

console = Console()

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
    console.print("[bold cyan]xX--------------------xX[/bold cyan]")

def print_menu():
    console.print(Panel.fit("[bold yellow]1.[/bold yellow] Travel to another city\n"
                            "[bold yellow]2.[/bold yellow] Go to the Center of city\n"
                            "[bold yellow]3.[/bold yellow] Visit the shop\n"
                            "[bold yellow]4.[/bold yellow] Move inside the city (N/S/E/W/Fast-travel)\n"
                            "[bold yellow]5.[/bold yellow] Open inventory\n"
                            "[bold yellow]6.[/bold yellow] View badges\n"
                            "[bold yellow]7.[/bold yellow] Quit to Menu", title=f"[bold magenta]{traveling.current_city} Menu[/bold magenta]"))

while run:
    while menu:
        clear_screen()
        draw()
        ascii_art.welcome_screen()
        draw()
        if rules:
            console.print("[bold green]Play the game cleanfully[/bold green]")
            rules = False
            input("> ")
            choice = ""
        else:
            choice = console.input("[bold cyan]# [/bold cyan]")

        if choice == "1":
            menu = False
            play = True
        elif choice == "2":
            console.print("[bold red]Load feature not implemented yet.[/bold red]")
            input("> Press Enter...")
        elif choice == "3":
            clear_screen()
            rules = True
        elif choice == "4":
            clear_screen()
            console.print("[bold magenta]Farewell, Hero[/bold magenta]")
            quit()
        else:
            console.print("[bold red]Insert a valid command[/bold red]")

    while play:
        clear_screen()
        draw()
        console.print(f"[bold yellow]{traveling.get_tile_description()}[/bold yellow]")

        NPC.check_for_npcs(traveling.current_city, traveling.get_current_tile())

        # Quest triggers
        quest_triggers = [
            ("Paris", "Cathedral", "Lost Relic"),
            ("Cairo", "Bazaar", "Missing Ring"),
            ("London", "Docks", "Smuggled Goods"),
            ("London", "Crossroad", "Crossroad Ambush"),
            ("London", "Castle", "Castle Intruder"),
            ("Paris", "Tavern", "Tavern Brawl"),
            ("Paris", "Gatehouse", "Gatehouse Thief"),
            ("Paris", "Cathedral", "Defender of the Faith"),
            ("Cairo", "Oasis", "Oasis Raid"),
            ("Cairo", "Citadel", "Citadel Intrigue"),
            ("Cairo", "Bazaar", "Bazaar Pickpocket"),
            ("London", "Crossroad", "Highway Robbery"),
            ("London", "Docks", "Stolen Cargo"),
            ("London", "Castle", "Knight’s Oath"),
            ("Paris", "Tavern", "Drunken Raiders"),
            ("Paris", "Gatehouse", "City Gate Break-in"),
            ("Cairo", "Oasis", "Desert Justice")
        ]

        for city, tile, quest_name in quest_triggers:
            if (traveling.current_city, traveling.get_current_tile()) == (city, tile):
                start_quest(quest_name)

        draw()
        console.print()
        draw()
        print_menu()
        draw()
        console.print()
        action = console.input("[bold cyan]# [/bold cyan]")

        if action == "1":
            console.print("[bold green]Where do you want to travel?[/bold green]")
            for city in traveling.cities:
                if city != traveling.current_city:
                    console.print(f"- [bold yellow]{city}[/bold yellow]")
            destination = console.input("# ")

            if destination in traveling.cities:
                traveling.current_city = destination

                # Update map and player position based on city
                city_positions = {"London": (traveling.london_map, (2, 3)),
                                  "Paris": (traveling.paris_map, (2, 3)),
                                  "Cairo": (traveling.cairo_map, (2, 3))}
                traveling.current_map, traveling.player_pos = city_positions[destination]

                console.print(f"[bold magenta]You have traveled to {destination}.[/bold magenta]")
                view_map = console.input(f"Do you want to view [bold yellow]{destination}[/bold yellow]'s map (y/n) ")
                if view_map.lower() == "y":
                    draw()
                    for row in traveling.current_map:
                        console.print(" ".join(traveling.symbols[tile] for tile in row))
                    draw()
            else:
                console.print("[bold red]Invalid city.[/bold red]")
            input("> Press Enter...")

        elif action == "2":
            city_center_pos = {"London": (2, 3), "Paris": (2, 3), "Cairo": (3, 2)}
            traveling.player_pos = city_center_pos[traveling.current_city]
            console.print(f"[bold cyan]You're in the heart of {traveling.current_city}[/bold cyan]")
            input("> Press Enter...")

        elif action == "3":
            shopping.show_city_shops(traveling.current_city)

        elif action == "4":
            clear_screen()
            draw()
            console.print("[bold green]Which direction do you want to move?[/bold green]")
            console.print("[bold yellow]N[/bold yellow] - North")
            console.print("[bold yellow]S[/bold yellow] - South")
            console.print("[bold yellow]E[/bold yellow] - East")
            console.print("[bold yellow]W[/bold yellow] - West")
            console.print("[bold yellow]F[/bold yellow] - Fast Travel")
            draw()
            direction = console.input("[bold cyan]# [/bold cyan]").upper()

            if direction in ["N", "S", "E", "W"]:
                result = traveling.move(direction)
                console.print(result)
                NPC.check_for_npcs(traveling.current_city, traveling.get_current_tile())

                quest_enemy_fought = False
                for q_name in quest.quests.keys():
                    enemy_name = quest.trigger_quest_enemy(q_name, traveling.current_city, traveling.get_current_tile())
                    if enemy_name:
                        enemy_obj = fighting.Enemy(enemy_name)
                        defeated_enemy, looted_items = fighting.combat(enemy_obj)
                        quest.check_quest_progress(q_name, traveling.current_city, traveling.get_current_tile(),
                                                   defeated_enemy, looted_items)
                        quest_enemy_fought = True
                        break

                if not quest_enemy_fought:
                    defeated_enemy, looted_items = fighting.check_for_enemy()
                    if defeated_enemy:
                        for q_name in quest.quests.keys():
                            quest.check_quest_progress(q_name, traveling.current_city, traveling.get_current_tile(),
                                                       defeated_enemy, looted_items)

            elif direction == "F":
                traveling.fast_travel()
                NPC.check_for_npcs(traveling.current_city, traveling.get_current_tile())

            else:
                console.print("[bold red]Invalid direction.[/bold red]")
            input("> Press Enter...")

        elif action == "5":
            inventory.view_inventory()
            input("> Press Enter...")

        elif action == "6":
            badges.view_badges()
            input("> Press Enter...")

        elif action == "7":
            play = False
            menu = True

