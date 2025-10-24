from mechs import fighting, shopping

from .puzzles import cipher


# View inventory and optionally use items
def view_inventory():
    inv = shopping.inventory
    if inv:
        print(f"Your HP: {fighting.player_hp}")
        print(f"Remaining Gold: {shopping.player_gold}")
        print()
        print("Your inventory contains:")

        for idx, item in enumerate(inv, 1):
            print(f"{idx}. {item}")

        print("\nDo you want to use an item? (y/n)")
        choice = input("> ").lower()

        if choice == "y":
            item_choice = input("Enter item number: ")
            if item_choice.isdigit():
                item_choice = int(item_choice) - 1
                if 0 <= item_choice < len(inv):
                    use_item(inv[item_choice])
                else:
                    print("Invalid choice.")
            else:
                print("Invalid input.")
    else:
        print("Your inventory is empty")


content = cipher.encrypted_message
letter_content = "You've finished the game"


# Handle item usage effects
def use_item(item):
    inv = shopping.inventory

    # Special quest items first
    if item == "Illuminated Manuscript":
        print(f"The content of the Manuscript is: {content}")
        if "Illuminated Manuscript" not in inv:
            inv.append("Illuminated Manuscript")
        return
    elif item.lower() == "letter":
        print(f"The content of the letter: {letter_content}")
        # Letter stays in inventory, so we don’t remove it
        return

    # Shop items (healing, etc.)
    shops = shopping.shops
    for city in shops.values():
        for shop_type, shop_items in city.items():
            if item in shop_items:
                if "bread" in item.lower():
                    fighting.player_hp = min(fighting.player_hp + 230, 1500)
                    print(f"You ate {item} and healed 200 HP. Current HP: {fighting.player_hp}")
                    inv.remove(item)
                elif "wine" in item.lower():
                    fighting.player_hp = min(fighting.player_hp + 100, 1500)
                    print(f"You drank {item} and healed 100 HP. Current HP: {fighting.player_hp}")
                    inv.remove(item)
                elif "Blessed Wine" in item:
                    fighting.player_hp = min(fighting.player_hp + 750, 1500)
                    print(f"You drank {item} and healed 100 HP. Current HP: {fighting.player_hp}")
                    inv.remove(item)
                elif "cheese" in item.lower():
                    fighting.player_hp = min(fighting.player_hp + 150, 1500)
                    print(f"You ate {item} and healed 150 HP. Current HP: {fighting.player_hp}")
                    inv.remove(item)
                elif "potion" in item.lower():
                    fighting.player_hp = min(fighting.player_hp + 500, 1500)
                    print(f"You used {item} and restored 500 HP. Current HP: {fighting.player_hp}")
                    inv.remove(item)
                else:
                    print(f"You used {item}, but nothing happened...")

                return

    # If nothing matched
    print(f"{item} cannot be used.")


def sell_item(item):
    inv = shopping.inventory
    shops = shopping.shops

    # 1. Check if player owns the item
    if item not in inv:
        print("You don't have this item in your inventory.")
        return

    # 2. Prevent selling quest or story items
    unsellable_items = ["Illuminated Manuscript", "Letter"]
    if item in unsellable_items:
        print(f"{item} cannot be sold. It's too important to part with.")
        return

    # 3. Find base price across all shops
    base_price = 0
    for city in shops.values():
        for shop_type, shop_items in city.items():
            if isinstance(shop_items, dict):
                # shop_items like {"Bread": 100, "Wine": 200}
                if item in shop_items:
                    base_price = shop_items[item]
                    break
            elif isinstance(shop_items, list):
                # if shop_items is a list, assume a flat default price
                if item in shop_items:
                    base_price = 100  # fallback default
                    break
        if base_price != 0:
            break

    # 4. Handle items with no base price
    if base_price == 0:
        print("No merchant seems interested in buying this item.")
        return

    # 5. Calculate sell value
    sell_multiplier = 0.5  # Merchant buys for half price
    try:
        selling_price = int(int(base_price) * float(sell_multiplier))
    except (TypeError, ValueError):
        print("Error: Invalid price data for this item.")
        return

    # 6. Ask if player wants to sell more than one (optional)
    count_in_inventory = inv.count(item)
    if count_in_inventory > 1:
        print(f"You have {count_in_inventory} of {item}. How many do you want to sell?")
        try:
            quantity = int(input("> ").strip())
        except ValueError:
            print("Invalid number.")
            return
        if quantity <= 0 or quantity > count_in_inventory:
            print("Invalid quantity.")
            return
    else:
        quantity = 1

    total_price = selling_price * quantity

    # 7. Confirm transaction
    print(f"Sell {quantity}x {item} for {total_price} gold? (y/n)")
    choice = input("> ").strip().lower()

    if choice != "y":
        print("Sale cancelled.")
        return

    # 8. Process transaction
    for _ in range(quantity):
        inv.remove(item)
    shopping.player_gold += total_price

    print(f"You sold {quantity}x {item} for {total_price} gold.")
    print(f"Remaining Gold: {shopping.player_gold}")

