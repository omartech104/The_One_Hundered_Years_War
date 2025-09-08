from mechs import traveling

# Example player variables
player_gold = 100
inventory = []

# Shops dictionary
shops = {
    "London": {
        "Market": {
            "Longsword": {"price": 50, "desc": "A Long sharp blade for battle."},
            "Shield": {"price": 40, "desc": "Protects against attacks."},
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

    # Move player to Market/Bazaar automatically
    market_name = "Market" if city != "Cairo" else "Bazaar"
    if city == "London":
        traveling.player_pos = (3, 5)  # London Market coordinates
    elif city == "Paris":
        traveling.player_pos = (3, 5)  # Paris Market coordinates
    elif city == "Cairo":
        traveling.player_pos = (1, 1)  # Cairo Bazaar coordinates

    row, col = traveling.player_pos
    print(f"\nYou walk to the {market_name} in {city}.")
    print(f"You are now at {traveling.current_map[row][col]}.\n")

    city_shop = shops[city][market_name]

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

