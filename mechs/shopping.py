from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt
from mechs import traveling

console = Console()

# --- Player Variables ---
player_gold = 500
inventory = []


# --- SHOPS DATABASE ---
shops = {
    "London": {
        "Market": {
            "A loaf of bread": {"price": 5, "desc": "Baked in a simple oven.", "stock": 5},
            "Astrolabe": {"price": 400, "desc": "An instrument of navigation.", "stock": 5},
            "Gemstone": {"price": 800, "desc": "A rare gemstone.", "stock": 1},
            "Health Potion": {"price": 450, "desc": "Restores health instantly.", "stock": 6},
            "Map Of London": {"price": 10, "desc": "The map of London.", "stock": 2}
        },
        "Armory": {
            "Longsword": {"price": 80, "desc": "Strong blade favored by knights.", "damage": 300, "stock": 2},
            "Battle Axe": {"price": 100, "desc": "Heavy axe for brutal combat.", "damage": 350, "stock": 2},
            "Short Bow": {"price": 60, "desc": "Simple bow with limited range.", "damage": 200, "stock": 3},
            "Warhammer": {"price": 120, "desc": "Crush your foes with force.", "damage": 400, "stock": 1},
            "Dagger": {"price": 30, "desc": "Quick, light, and deadly.", "damage": 150, "stock": 4}
        }
    },

    "Paris": {
        "Market": {
            "Book": {"price": 30, "desc": "A tome of medieval knowledge.", "stock": 3},
            "Wine": {"price": 20, "desc": "A fine Parisian vintage.", "stock": 5},
            "Illuminated Manuscript": {"price": 60, "desc": "A missing part of something unknown.", "stock": 1},
            "Map Of Paris": {"price": 8, "desc": "The Map of Paris.", "stock": 3}
        },
        "Armory": {
            "Rapier": {"price": 90, "desc": "Elegant fencing blade.", "damage": 250, "stock": 2},
            "Halberd": {"price": 110, "desc": "A polearm used by Parisian guards.", "damage": 370, "stock": 2},
            "Crossbow": {"price": 100, "desc": "Powerful but slow to reload.", "damage": 320, "stock": 2},
            "Mace": {"price": 70, "desc": "Crushing weapon popular among clergy knights.", "damage": 280, "stock": 3},
            "Dirk": {"price": 40, "desc": "Slim blade used by assassins.", "damage": 180, "stock": 4}
        }
    },

    "Cairo": {
        "Bazaar": {
            "Spices": {"price": 25, "desc": "Exotic spices from the East.", "stock": 5},
            "Halum Cheese": {"price": 50, "desc": "A half pound of local cheese.", "stock": 3},
            "A copy of matn al-ajrumiyyah": {"price": 100, "desc": "Rare Arabic grammar manuscript.", "stock": 1},
            "Map Of Cairo": {"price": 8, "desc": "The Map of Cairo.", "stock": 3}
        },
        "Armory": {
            "Shamshir": {"price": 85, "desc": "Curved sword, swift and sharp.", "damage": 270, "stock": 2},
            "Spear": {"price": 60, "desc": "Simple but effective.", "damage": 240, "stock": 3},
            "Composite Bow": {"price": 95, "desc": "Strong bow with great range.", "damage": 280, "stock": 2},
            "Khopesh": {"price": 120, "desc": "Ancient Egyptian sickle-sword.", "damage": 360, "stock": 1},
            "Jambiya": {"price": 35, "desc": "Curved dagger from Arabia.", "damage": 160, "stock": 4}
        }
    },

    "Prague": {
        "Market": {
            "Medieval Bread": {"price": 5, "desc": "A loaf from Prague bakery.", "stock": 5},
            "Ale": {"price": 15, "desc": "Locally brewed dark ale.", "stock": 8},
            "Map Of Prague": {"price": 10, "desc": "The Map Of Prague.", "stock": 3},
            "Amber Necklace": {"price": 100, "desc": "Necklace made from Bohemian amber.", "stock": 2}
        },
        "Armory": {
            "Sword": {"price": 80, "desc": "Forged in Bohemia.", "damage": 300, "stock": 2},
            "War Axe": {"price": 100, "desc": "Heavy axe favored by knights.", "damage": 350, "stock": 2},
            "Throwing Knives": {"price": 90, "desc": "Set of sharp throwing knives.", "damage": 100, "stock": 3},
            "Mace": {"price": 70, "desc": "A crushing weapon for close combat.", "damage": 270, "stock": 2},
        }
    },

    "Venice": {
        "Market": {
            "Glass Beads": {"price": 25, "desc": "Finely made Venetian glass.", "stock": 5},
            "Wine": {"price": 20, "desc": "Local Venetian vintage.", "stock": 6},
            "Map Of Venice": {"price": 12, "desc": "The Map Of Venice.", "stock": 3},
            "Silk Cloth": {"price": 60, "desc": "Imported silk from the East.", "stock": 2}
        },
        "Armory": {
            "Stiletto": {"price": 90, "desc": "Elegant Venetian blade.", "damage": 250, "stock": 2},
            "Pike": {"price": 110, "desc": "Used by city guards.", "damage": 370, "stock": 2},
            "Short Bow": {"price": 60, "desc": "Compact city bow.", "damage": 200, "stock": 3},
            "Cinquedea": {"price": 35, "desc": "Triangular dagger.", "damage": 160, "stock": 4}
        }
    },

    "Tours": {
        "Market": {
            "Cheese": {"price": 15, "desc": "Local Tours cheese.", "stock": 5},
            "Wine": {"price": 20, "desc": "Fine Loire Valley wine.", "stock": 6},
            "Map Of Tours": {"price": 8, "desc": "The Map Of Tours.", "stock": 3},
            "Book of Prayers": {"price": 50, "desc": "A local religious text.", "stock": 2}
        },
        "Armory": {
            "Arming Sword": {"price": 80, "desc": "Strong soldier’s blade.", "damage": 200, "stock": 2},
            "Poleaxe": {"price": 100, "desc": "Light but powerful axe.", "damage": 250, "stock": 2},
            "Throwing Spear": {"price": 90, "desc": "A balanced spear.", "damage": 180, "stock": 3},
            "Warhammer": {"price": 120, "desc": "Crush your foes.", "damage": 400, "stock": 1},
        }
    }
}

city_market_pos = {
    "London": (3, 5),
    "Paris": (3, 5),
    "Cairo": (1, 1),
    "Prague": (1, 5),
    "Venice": (1, 5),
    "Tours": (1, 5),
}

# --- FUNCTIONS ---

def show_city_shops(city):
    """Shows all shops in the city and allows player to enter them"""
    if city not in shops:
        console.print(f"[bold red]No shops available in {city}[/bold red]")
        return

    while True:
        console.clear()
        console.print(Panel.fit(f"[bold cyan]{city} Shops[/bold cyan]", border_style="bright_blue"))
        city_shops = shops[city]
        for shop_name in city_shops:
            console.print(f"[bold yellow]- {shop_name}[/bold yellow]")
        console.print("[red]B[/red] - Go back to the Market")

        selected = Prompt.ask("[green]Enter shop name[/green]").strip()
        if selected.lower() == "b":
            set_player_to_market(city)
            break
        elif selected in city_shops:
            open_shop(city, selected)
        else:
            console.print("[red]Invalid shop name![/red]")

def open_shop(city, shop_name):
    global player_gold
    shop = shops[city][shop_name]
    console.clear()
    console.print(Panel.fit(f"[bold cyan]{shop_name} - {city}[/bold cyan]", border_style="yellow"))

    table = Table(title=f"{shop_name} Inventory", header_style="bold blue")
    table.add_column("Item", style="bold green")
    table.add_column("Price", justify="right")
    table.add_column("Stock", justify="center")
    table.add_column("Description", justify="left")

    for item, data in shop.items():
        table.add_row(item, f"{data['price']} gold", str(data['stock']), data['desc'])
    console.print(table)

    console.print(f"[bold magenta]Your gold:[/bold magenta] {player_gold}")
    buy_item = Prompt.ask("[green]Enter item to buy[/green] or [red]B to go back[/red]")
    if buy_item.lower() == "b":
        return
    if buy_item in shop:
        item = shop[buy_item]
        if player_gold >= item["price"] and item["stock"] > 0:
            player_gold -= item["price"]
            item["stock"] -= 1
            inventory.append(buy_item)
            console.print(f"[bold green]You bought {buy_item}![/bold green]")
        else:
            console.print("[red]You can’t afford that or it’s out of stock![/red]")
    else:
        console.print("[red]Invalid item name![/red]")

    input("> Press Enter...")


def show_inventory():
    console.print(Panel.fit("[bold cyan]Your Inventory[/bold cyan]", border_style="bright_magenta"))
    if not inventory:
        console.print("[italic yellow]Your inventory is empty.[/italic yellow]")
    else:
        for i, item in enumerate(inventory, 1):
            console.print(f"[bold green]{i}.[/bold green] {item}")
    console.print(f"\n[bold magenta]Gold:[/bold magenta] {player_gold}")
    input("> Press Enter...")


def set_player_to_market(city):
    """After leaving shop, set player to market tile"""
    pos = city_market_pos.get(city, (2, 3))
    traveling.player_pos = pos
