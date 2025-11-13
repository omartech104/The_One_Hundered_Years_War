from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt, IntPrompt, Confirm
from rich.text import Text
from rich.panel import Panel
from mechs import fighting, shopping, traveling
from .puzzles import cipher

console = Console()

# ========================
# 🔹 Inventory Management
# ========================

def view_inventory():
    """Displays player inventory with Rich tables and color feedback."""
    from mechs.inventory import sell_item, use_item  # avoid circular import
    import mechs.shopping
    import mechs.fighting

    inv = shopping.inventory

    console.rule("[bold gold3] Player Inventory[/bold gold3]")

    if not inv:
        console.print("[red]Your inventory is empty.[/red]")
        return

    console.print(f"[bold cyan]HP:[/bold cyan] {fighting.player_hp}/1500")
    console.print(f"[bold yellow]Gold:[/bold yellow] {shopping.player_gold}\n")

    table = Table(title="Your Items", title_style="bold cyan")
    table.add_column("#", justify="center", style="bright_white")
    table.add_column("Item", justify="left", style="bold green")
    table.add_column("Count", justify="center", style="cyan")

    item_counts = {}
    for item in inv:
        item_counts[item] = item_counts.get(item, 0) + 1

    for idx, (item, count) in enumerate(item_counts.items(), 1):
        table.add_row(str(idx), item, str(count))

    console.print(table)

    console.print("\n[yellow]Do you want to [bold]use[/bold] or [bold]sell[/bold] an item?[/yellow]")
    choice = Prompt.ask(">", choices=["use", "sell"], default="use")

    item_choice = IntPrompt.ask("\nEnter item number", default=1)
    items_list = list(item_counts.keys())

    if not (1 <= item_choice <= len(items_list)):
        console.print("[red]Invalid choice.[/red]")
        return

    selected_item = items_list[item_choice - 1]

    if choice == "use":
        use_item(selected_item)
    elif choice == "sell":
        sell_item(selected_item)


# 🔐 Quest content
content = cipher.encrypted_message
letter_content = "You've finished the game"


# ========================
# 🔹 Item Usage
# ========================

def use_item(item):
    import mechs.shopping
    import mechs.traveling
    inv = shopping.inventory

    console.rule(f"[bold cyan]Using {item}[/bold cyan]")

    # --- Quest items ---
    if item == "Illuminated Manuscript":
        console.print(Panel.fit(f"[bold yellow]{content}[/bold yellow]", title="Illuminated Manuscript"))
        return

    elif item.lower() == "letter":
        console.print(Panel.fit(f"[italic cyan]{letter_content}[/italic cyan]", title="Letter"))
        return

    # --- Consumables & maps ---
    shops = shopping.shops
    for city in shops.values():
        for shop_type, shop_items in city.items():
            if item in shop_items:
                if "bread" in item.lower():
                    fighting.player_hp = min(fighting.player_hp + 230, 1500)
                    inv.remove(item)
                    console.print(f"[green]You ate {item} and healed 230 HP![/green]")
                elif "wine" in item.lower():
                    fighting.player_hp = min(fighting.player_hp + 100, 1500)
                    inv.remove(item)
                    console.print(f"[magenta]You drank {item} and restored 100 HP![/magenta]")
                elif "Blessed Wine" in item:
                    fighting.player_hp = min(fighting.player_hp + 750, 1500)
                    inv.remove(item)
                    console.print(f"[bold magenta]You drank {item} and restored 750 HP![/bold magenta]")
                elif "cheese" in item.lower():
                    fighting.player_hp = min(fighting.player_hp + 150, 1500)
                    inv.remove(item)
                    console.print(f"[green]You ate {item} and healed 150 HP![/green]")
                elif "potion" in item.lower():
                    fighting.player_hp = min(fighting.player_hp + 500, 1500)
                    inv.remove(item)
                    console.print(f"[cyan]You used {item} and restored 500 HP![/cyan]")
                elif "Map Of" in item:
                    console.print(f"[bold cyan]Showing {item}...[/bold cyan]")
                    for row in traveling.current_map:
                        console.print(" ".join(traveling.symbols[tile] for tile in row))
                    input("> Press Enter to continue...")
                else:
                    console.print(f"[yellow]You used {item}, but nothing happened...[/yellow]")
                return

    console.print(f"[red]{item} cannot be used.[/red]")


# ========================
# 🔹 Selling Items
# ========================

def sell_item(item):
    import mechs.shopping as shopping
    inv = shopping.inventory
    shops = shopping.shops

    if item not in inv:
        console.print("[red]You don't have this item in your inventory.[/red]")
        return

    unsellable_items = ["Illuminated Manuscript", "Letter"]
    if item in unsellable_items:
        console.print(f"[yellow]{item} cannot be sold. It's too important.[/yellow]")
        return

    base_price = 0
    for city in shops.values():
        for shop_type, shop_items in city.items():
            if isinstance(shop_items, dict) and item in shop_items:
                item_data = shop_items[item]
                base_price = item_data.get("price", 0) if isinstance(item_data, dict) else item_data
                break
        if base_price:
            break

    if base_price == 0:
        console.print("[gray]No merchant seems interested in buying this item.[/gray]")
        return

    sell_multiplier = 0.5
    selling_price = int(base_price * sell_multiplier)
    count_in_inventory = inv.count(item)

    if count_in_inventory > 1:
        quantity = IntPrompt.ask(
            f"[cyan]You have {count_in_inventory} of {item}. How many to sell?[/cyan]",
            default=1
        )
        if quantity <= 0 or quantity > count_in_inventory:
            console.print("[red]Invalid quantity.[/red]")
            return
    else:
        quantity = 1

    total_price = selling_price * quantity

    confirm = Confirm.ask(f"Sell {quantity}x [bold yellow]{item}[/bold yellow] for [bold gold3]{total_price} gold[/bold gold3]?")
    if not confirm:
        console.print("[gray]Sale cancelled.[/gray]")
        return

    for _ in range(quantity):
        inv.remove(item)

    shopping.player_gold = int(shopping.player_gold) + total_price

    console.print(
        f"[green]✅ You sold {quantity}x {item} for {total_price} gold![/green]\n"
        f"[bold yellow]💰 Remaining Gold: {shopping.player_gold}[/bold yellow]"
    )

