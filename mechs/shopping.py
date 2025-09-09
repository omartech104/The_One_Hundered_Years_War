from mechs import traveling

# Example player variables
player_gold = 100
inventory = []

# Shops dictionary
# Shops dictionary
shops = {
    "London": {
        "Market": {
            "A loaf of bread": {"price": 5, "desc": "Baked in a simple oven."}
        }
    },
    "Paris": {
        "Market": {
            "Book": {"price": 30, "desc": "A tome of medieval knowledge."},
            "Wine": {"price": 20, "desc": "A fine Parisian vintage."},
            "Illuminated Manuscript": {"price": 60, "desc": "A missing part of something unknown."}
        }
    },
    "Cairo": {
        "Bazaar": {
            "Spices": {"price": 25, "desc": "Exotic spices from the East."},
            "Halum Cheese": {"price": 50, "desc": "A half pound of local-made Cheese."},
            "A copy of matn al-ajrumiyyah": {"price": 100, "desc": "A rare copy of matn al-ajrumiyyah."}
        }
    }
}


def open_shop():
    global player_gold, inventory

    city = traveling.current_city

    # Player chooses which shop
    shop_type = None
    if city == "Cairo":
        shop_type = input("Do you want to visit the Bazaar or Armory? ").capitalize()
        if shop_type not in ["Bazaar", "Armory"]:
            print("Invalid choice.")
            return
    else:
        shop_type = input("Do you want to visit the Market or Armory? ").capitalize()
        if shop_type not in ["Market", "Armory"]:
            print("Invalid choice.")
            return

    # Change player position (example coords)
    if city == "London" and shop_type == "Market":
        traveling.player_pos = (3, 5)
    elif city == "London" and shop_type == "Armory":
        traveling.player_pos = (1, 1)  # Example coords for Armory

    elif city == "Paris" and shop_type == "Market":
        traveling.player_pos = (3, 5)
    elif city == "Paris" and shop_type == "Armory":
        traveling.player_pos = (1, 5)  # Example coords for Armory

    elif city == "Cairo" and shop_type == "Bazaar":
        traveling.player_pos = (1, 1)
    elif city == "Cairo" and shop_type == "Armory":
        traveling.player_pos = (3, 1)  # Example coords for Armory

    row, col = traveling.player_pos
    print(f"\nYou walk to the {shop_type} in {city}.")
    print(f"You are now at {traveling.current_map[row][col]}.\n")

    # Fetch shop
    city_shop = shops[city][shop_type]

    while True:
        print("Items for sale:")
        for i, item in enumerate(city_shop, start=1):
            info = city_shop[item]
            print(f"{i}. {item} - {info['price']} gold - {info['desc']}")

        print(f"\nYour gold: {player_gold}")
        print("Type the item number to buy, or 0 to exit.")

        choice = input("# ")

        if choice == "0":
            print("Leaving the shop...")
            break

        if not choice.isdigit() or int(choice) < 1 or int(choice) > len(city_shop):
            print("Invalid choice, try again.\n")
            continue

        item_name = list(city_shop.keys())[int(choice) - 1]
        item_price = city_shop[item_name]["price"]

        if player_gold >= item_price:
            player_gold -= item_price
            inventory.append(item_name)
            print(f"You bought {item_name}! Remaining gold: {player_gold}\n")
        else:
            print("Not enough gold!\n")

