from mechs import shopping, fighting
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
    if item.lower() == "manuscript":
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
                    fighting.player_hp = min(fighting.player_hp + 200, 1500)
                    print(f"You ate {item} and healed 200 HP. Current HP: {fighting.player_hp}")
                elif "wine" in item.lower():
                    fighting.player_hp = min(fighting.player_hp + 100, 1500)
                    print(f"You drank {item} and healed 100 HP. Current HP: {fighting.player_hp}")
                elif "cheese" in item.lower():
                    fighting.player_hp = min(fighting.player_hp + 150, 1500)
                    print(f"You ate {item} and healed 150 HP. Current HP: {fighting.player_hp}")
                elif "potion" in item.lower():
                    fighting.player_hp = min(fighting.player_hp + 500, 1500)
                    print(f"You used {item} and restored 500 HP. Current HP: {fighting.player_hp}")
                else:
                    print(f"You used {item}, but nothing happened...")

                # Shop consumables are removed after use
                inv.remove(item)
                return

    # If nothing matched
    print(f"{item} cannot be used.")

