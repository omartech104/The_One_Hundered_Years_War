import random
from rich.console import Console
console = Console()

from mechs import fighting, shopping, inventory
from .puzzles import cipher

# Boss stats
boss_hp = 1500
boss_attack = (50, 390)  # random attack range
equipped_weapon = None
equipped_damage = 50  # fists by default
defeated = False  # ✅ track boss defeat state


# -----------------------------------------------------------
# Weapon Equip
# -----------------------------------------------------------
def equip_weapon():
    global equipped_weapon, equipped_damage

    if not shopping.inventory:
        console.print("[bold red]You have no items in your inventory![/bold red]")
        return

    weapon_list = []
    for item in shopping.inventory:
        for city in shopping.shops.values():
            if "Armory" in city and item in city["Armory"]:
                weapon_list.append((item, city["Armory"][item]["damage"]))

    if not weapon_list:
        console.print("[bold yellow]No usable weapons found — fighting with fists (50 dmg).[/bold yellow]")
        equipped_weapon = None
        equipped_damage = 50
        return

    console.print("\n[bold cyan]Choose a weapon to equip:[/bold cyan]")
    for idx, (weapon, dmg) in enumerate(weapon_list, 1):
        console.print(f"[green]{idx}.[/green] {weapon} [bold yellow]({dmg} dmg)[/bold yellow]")

    choice = input("> ").strip()
    if choice.isdigit():
        choice = int(choice) - 1
        if 0 <= choice < len(weapon_list):
            equipped_weapon, equipped_damage = weapon_list[choice]
            console.print(f"[bold cyan]You equipped {equipped_weapon}![/bold cyan] Damage set to [bold yellow]{equipped_damage}[/bold yellow]")
            return

    console.print("[bold red]Invalid choice. Fighting with fists (50 dmg).[/bold red]")
    equipped_weapon = None
    equipped_damage = 50


# -----------------------------------------------------------
# Boss Fight: Cathedral Guardian
# -----------------------------------------------------------
def fight_cathedral_boss():
    global boss_hp, defeated

    if defeated:
        console.print("\n[bold white]The Cathedral Guardian[/bold white] has already been defeated.")
        return

    console.print("\nYou enter the dark Cathedral...")
    console.print("[bold white]A towering knight — the Guardian of Shifts — blocks your way![/bold white]")

    equip_weapon()

    while boss_hp > 0 and fighting.player_hp > 0:
        console.print(f"\nYour HP: [bold green]{fighting.player_hp}[/bold green] | Boss HP: [bold red]{boss_hp}[/bold red]")
        console.print("[bold red]1.[/bold red] Attack  |  [bold yellow]2.[/bold yellow] Use Item  |  [bold blue]3.[/bold blue] Run")
        choice = input("> ").strip()

        # 🗡️ Attack
        if choice == "1":
            damage = equipped_damage
            boss_hp -= damage
            console.print(f"You strike the [bold white]Cathedral Guardian[/bold white] with {equipped_weapon or 'fists'} for [bold red]{damage}[/bold red] damage!")

        # 🧪 Use Item
        elif choice == "2":
            if not shopping.inventory:
                console.print("[bold red]Your inventory is empty![/bold red]")
            else:
                console.print("\n[bold yellow]Choose an item to use:[/bold yellow]")
                for idx, item in enumerate(shopping.inventory, 1):
                    console.print(f"[green]{idx}.[/green] {item}")
                item_choice = input("> ").strip()
                if item_choice.isdigit():
                    item_choice = int(item_choice) - 1
                    if 0 <= item_choice < len(shopping.inventory):
                        inventory.use_item(shopping.inventory[item_choice])
                    else:
                        console.print("[bold red]Invalid choice.[/bold red]")
                else:
                    console.print("[bold red]Invalid input.[/bold red]")

        # 🏃 Run
        elif choice == "3":
            console.print("[bold yellow]You flee from the Cathedral... but the Guardian still stands.[/bold yellow]")
            defeated = False
            return

        else:
            console.print("[bold red]Invalid choice.[/bold red]")
            continue

        # 🩸 Boss counterattack
        if boss_hp > 0:
            boss_damage = random.randint(*boss_attack)
            fighting.player_hp -= boss_damage
            console.print(f"The [bold white]Guardian[/bold white] smashes you for [bold red]{boss_damage}[/bold red] damage!")
            if fighting.player_hp <= 0:
                console.print("\n[bold red]You were slain by the Cathedral Guardian...[/bold red]")
                defeated = False
                return

    # 🏆 Victory
    if boss_hp <= 0:
        console.print("\n[bold green]You defeated the Cathedral Guardian![/bold green]")
        defeated = True
        post_boss_event()


# -----------------------------------------------------------
# Post-boss Event
# -----------------------------------------------------------
def post_boss_event():
    console.print("\nAs the Guardian falls, his voice echoes through the Cathedral halls...")
    console.print('"The amount of shifts... is [bold yellow]3[/bold yellow]..."')
    console.print("\nA chest appears before you. It seems to need a number to open.")

    attempt = input("Enter the number: ").strip()
    if attempt == "3":
        console.print("\n[bold green]The chest clicks open...[/bold green]")
        inventory.content = cipher.message
        console.print("[bold cyan]You obtained the real message![/bold cyan]")
        shopping.player_gold += 355
        console.print("[bold yellow]+355 Gold[/bold yellow]")
    else:
        console.print("\n[bold red]The chest remains sealed... Maybe try again later.[/bold red]")

