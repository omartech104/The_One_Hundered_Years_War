from mechs import traveling

# Example player variables
player_gold = 500
inventory = []


# Shops dictionary with stock
shops = {
    "London": {
        "Market": {
            "A loaf of bread": {"price": 5, "desc": "Baked in a simple oven.", "stock": 5},
            "Astrolabe": {"price": 400, "desc": "A insturment of navigation.", "stock": 5},
            "Gemstone": {"price": 800, "desc": "A rare gemstone", "stock": 1}
        },
        "Armory": {
            "Longsword": {"price": 80, "desc": "A strong blade favored by knights.", "damage": 300, "stock": 2},
            "Battle Axe": {"price": 100, "desc": "A heavy axe for brutal combat.", "damage": 350, "stock": 2},
            "Short Bow": {"price": 60, "desc": "A simple bow with limited range.", "damage": 200, "stock": 3},
            "Warhammer": {"price": 120, "desc": "Crush your foes with sheer force.", "damage": 400, "stock": 1},
            "Dagger": {"price": 30, "desc": "Quick, light, and deadly up close.", "damage": 150, "stock": 4}
        }
    },
    "Paris": {
        "Market": {
            "Book": {"price": 30, "desc": "A tome of medieval knowledge.", "stock": 3},
            "Wine": {"price": 20, "desc": "A fine Parisian vintage.", "stock": 5},
            "Illuminated Manuscript": {"price": 60, "desc": "A missing part of something unknown.", "stock": 1}
        },
        "Armory": {
            "Rapier": {"price": 90, "desc": "Elegant and deadly fencing blade.", "damage": 250, "stock": 2},
            "Halberd": {"price": 110, "desc": "A polearm used by Parisian guards.", "damage": 370, "stock": 2},
            "Crossbow": {"price": 100, "desc": "Powerful but slow to reload.", "damage": 320, "stock": 2},
            "Mace": {"price": 70, "desc": "A crushing weapon popular among clergy knights.", "damage": 280, "stock": 3},
            "Dirk": {"price": 40, "desc": "A slim blade used by assassins.", "damage": 180, "stock": 4}
        }
    },
    "Cairo": {
        "Bazaar": {
            "Spices": {"price": 25, "desc": "Exotic spices from the East.", "stock": 5},
            "Halum Cheese": {"price": 50, "desc": "A half pound of local-made Cheese.", "stock": 3},
            "A copy of matn al-ajrumiyyah": {"price": 100, "desc": "A rare copy of matn al-ajrumiyyah.", "stock": 1}
        },
        "Armory": {
            "Scimitar": {"price": 85, "desc": "A curved sword, swift and sharp.", "damage": 270, "stock": 2},
            "Spear": {"price": 60, "desc": "Simple but effective in battle.", "damage": 240, "stock": 3},
            "Composite Bow": {"price": 95, "desc": "Strong bow with great range.", "damage": 280, "stock": 2},
            "Khopesh": {"price": 120, "desc": "An ancient Egyptian sickle-sword.", "damage": 360, "stock": 1},
            "Jambiya": {"price": 35, "desc": "A traditional curved dagger.", "damage": 160, "stock": 4}
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
        traveling.player_pos = (1, 1)

    elif city == "Paris" and shop_type == "Market":
        traveling.player_pos = (3, 5)
    elif city == "Paris" and shop_type == "Armory":
        traveling.player_pos = (1, 5)

    elif city == "Cairo" and shop_type == "Bazaar":
        traveling.player_pos = (1, 1)
    elif city == "Cairo" and shop_type == "Armory":
        traveling.player_pos = (3, 1)

    row, col = traveling.player_pos
    print(f"\nYou walk to the {shop_type} in {city}.")
    print(f"You are now at {traveling.current_map[row][col]}.\n")

    # Fetch shop
    city_shop = shops[city][shop_type]

    while True:
        print("Items for sale:")
        for i, item in enumerate(city_shop, start=1):
            info = city_shop[item]
            stock_info = f"(Stock: {info['stock']})" if "stock" in info else ""
            print(f"{i}. {item} - {info['price']} gold - {info['desc']} {stock_info}")

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
        item_data = city_shop[item_name]

        if item_data.get("stock", 1) <= 0:
            print(f"{item_name} is out of stock.\n")
            continue

        if player_gold >= item_data["price"]:
            player_gold -= item_data["price"]
            inventory.append(item_name)
            item_data["stock"] -= 1
            print(f"You bought {item_name}! Remaining gold: {player_gold}\n")
        else:
            print("Not enough gold!\n")

