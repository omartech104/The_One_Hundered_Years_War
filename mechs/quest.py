from mechs import fighting, shopping

quests = {
    "Lost Relic": {
        "name": "The Lost Relic",
        "giver": "Father Guillaume",  # NPC
        "location": ("Paris", "Cathedral"),  # City and tile
        "description": (
            "In the depths of the Paris Cathedral, Father Guillaume seeks help. "
            "An ancient relic has been stolen by bandits and hidden in the Louvre."
        ),
        "objective": {
            "city": "Paris",
            "tile": "Cathedral",
            "enemy": "Templar",
            "item": "Ancient Relic",
        },
        "reward": {
            "gold": 300,
            "items": ["Blessed Wine"],
            "message": "You have proven yourself a true protector of the faith.",
        },
        "completed": False,
    },
    "Missing Ring": {
        "name": "The Missing Ring",
        "giver": "Fatima The Merchant",  # NPC
        "location": ("Cairo", "Bazaar"),  # City and tile
        "description": (
            "In the Bazaar, you find Fatima the Merchant. "
            "A golden ring has been stolen by a thief and hidden in the Citadel."
        ),
        "objective": {
            "city": "Cairo",
            "tile": "Bazaar",
            "enemy": "Thief",
            "item": "Golden Ring",
        },
        "reward": {
            "gold": 450,
            "items": ["A Ruby"],
            "message": "You found it! My heart is lighter now. Take this gift as thanks.",
        },
        "completed": False,
    },
    "Smuggled Goods": {
        "name": "Smuggled Goods",
        "giver": "Captain Rowley",
        "location": ("London", "Docks"),
        "description": (
            "Captain Rowley has discovered smugglers hiding contraband in the London Docks. "
            "Recover the stolen cargo before it disappears."
        ),
        "objective": {
            "city": "London",
            "tile": "Docks",
            "enemy": "Thief",
            "item": "Stolen Cargo",
        },
        "reward": {
            "gold": 250,
            "items": ["Bottle of Rum"],
            "message": "The docks are safer thanks to you.",
        },
        "completed": False,
    },
    "Crossroad Ambush": {
        "name": "Crossroad Ambush",
        "giver": "Sir Aldred",
        "location": ("London", "Crossroad"),
        "description": (
            "Travelers have been ambushed at the London Crossroad. "
            "Sir Aldred asks you to deal with the bandits causing trouble."
        ),
        "objective": {
            "city": "London",
            "tile": "Crossroad",
            "enemy": "Bandit",
            "item": "Bandit Blade",
        },
        "reward": {
            "gold": 320,
            "items": ["Steel Dagger"],
            "message": "The people can travel freely again.",
        },
        "completed": False,
    },
    "Castle Intruder": {
        "name": "Castle Intruder",
        "giver": "Lady Eleanor",
        "location": ("London", "Castle"),
        "description": (
            "Lady Eleanor has heard of Templar spies hiding in the Castle. "
            "She tasks you with rooting them out."
        ),
        "objective": {
            "city": "London",
            "tile": "Castle",
            "enemy": "Templar",
            "item": "Templar Insignia",
        },
        "reward": {
            "gold": 500,
            "items": ["Emerald Brooch"],
            "message": "You have secured the castle’s honor.",
        },
        "completed": False,
    },
    "Tavern Brawl": {
        "name": "Tavern Brawl",
        "giver": "Innkeeper Martin",
        "location": ("Paris", "Tavern"),
        "description": (
            "The Paris Tavern has become dangerous. "
            "Bandits are harassing the patrons late at night."
        ),
        "objective": {
            "city": "Paris",
            "tile": "Tavern",
            "enemy": "Bandit",
            "item": "Broken Mug",
        },
        "reward": {
            "gold": 180,
            "items": ["Fine Ale"],
            "message": "Peace has returned to the tavern.",
        },
        "completed": False,
    },
    "Gatehouse Thief": {
        "name": "Gatehouse Thief",
        "giver": "Guard Henri",
        "location": ("Paris", "Gatehouse"),
        "description": (
            "Guard Henri reports thieves sneaking past the Paris Gatehouse. "
            "Catch one and recover stolen coins."
        ),
        "objective": {
            "city": "Paris",
            "tile": "Gatehouse",
            "enemy": "Thief",
            "item": "Stolen Coins",
        },
        "reward": {
            "gold": 220,
            "items": ["Silver Buckle"],
            "message": "The city treasury is safe once more.",
        },
        "completed": False,
    },
    "Defender of the Faith": {
        "name": "Defender of the Faith",
        "giver": "Archbishop Louis",
        "location": ("Paris", "Cathedral"),
        "description": (
            "The Archbishop fears Templar influence in the Cathedral. "
            "He asks you to confront them and recover sacred texts."
        ),
        "objective": {
            "city": "Paris",
            "tile": "Cathedral",
            "enemy": "Templar",
            "item": "Sacred Texts",
        },
        "reward": {
            "gold": 600,
            "items": ["Blessed Cross"],
            "message": "You have defended the holy word.",
        },
        "completed": False,
    },
    "Oasis Raid": {
        "name": "Oasis Raid",
        "giver": "Nomad Elder",
        "location": ("Cairo", "Oasis"),
        "description": (
            "A group of bandits has raided the Cairo Oasis, stealing precious water skins. "
            "The nomads ask for your help."
        ),
        "objective": {
            "city": "Cairo",
            "tile": "Oasis",
            "enemy": "Bandit",
            "item": "Water Skins",
        },
        "reward": {
            "gold": 275,
            "items": ["Leather Waterskin"],
            "message": "The desert people are grateful for your aid.",
        },
        "completed": False,
    },
    "Citadel Intrigue": {
        "name": "Citadel Intrigue",
        "giver": "Vizier Khalid",
        "location": ("Cairo", "Citadel"),
        "description": (
            "The Citadel is rumored to be infiltrated by Templars. "
            "The Vizier commands you to eliminate their spies."
        ),
        "objective": {
            "city": "Cairo",
            "tile": "Citadel",
            "enemy": "Templar",
            "item": "Spy Reports",
        },
        "reward": {
            "gold": 550,
            "items": ["Jeweled Dagger"],
            "message": "The Citadel remains strong under your protection.",
        },
        "completed": False,
    },
    "Bazaar Pickpocket": {
        "name": "Bazaar Pickpocket",
        "giver": "Shopkeeper Layla",
        "location": ("Cairo", "Bazaar"),
        "description": (
            "Pickpockets plague the Cairo Bazaar. "
            "Layla asks you to recover her stolen necklace."
        ),
        "objective": {
            "city": "Cairo",
            "tile": "Bazaar",
            "enemy": "Thief",
            "item": "Silver Necklace",
        },
        "reward": {
            "gold": 200,
            "items": ["Spice Pouch"],
            "message": "The Bazaar is safe for merchants once more.",
        },
        "completed": False,
    },
    "Highway Robbery": {
        "name": "Highway Robbery",
        "giver": "Merchant Thomas",
        "location": ("London", "Crossroad"),
        "description": (
            "Bandits ambush travelers at the London Crossroad. "
            "Merchant Thomas begs for protection."
        ),
        "objective": {
            "city": "London",
            "tile": "Crossroad",
            "enemy": "Bandit",
            "item": "Merchant’s Ledger",
        },
        "reward": {
            "gold": 260,
            "items": ["Travel Cloak"],
            "message": "The roads are safe for trade once again.",
        },
        "completed": False,
    },
    "Stolen Cargo": {
        "name": "Stolen Cargo",
        "giver": "Dockmaster Hugh",
        "location": ("London", "Docks"),
        "description": (
            "Dockmaster Hugh has reported missing cargo. "
            "Thieves at the docks are the likely culprits."
        ),
        "objective": {
            "city": "London",
            "tile": "Docks",
            "enemy": "Thief",
            "item": "Crate of Spices",
        },
        "reward": {
            "gold": 300,
            "items": ["Sailor’s Compass"],
            "message": "Trade can flourish again.",
        },
        "completed": False,
    },
    "Knight’s Oath": {
        "name": "Knight’s Oath",
        "giver": "Sir Geoffrey",
        "location": ("London", "Castle"),
        "description": (
            "Sir Geoffrey swears the honor of the realm is threatened by Templars in the Castle. "
            "He entrusts you with restoring order."
        ),
        "objective": {
            "city": "London",
            "tile": "Castle",
            "enemy": "Templar",
            "item": "Knight’s Seal",
        },
        "reward": {
            "gold": 480,
            "items": ["Silver Gauntlet"],
            "message": "The realm’s honor is preserved.",
        },
        "completed": False,
    },
    "Drunken Raiders": {
        "name": "Drunken Raiders",
        "giver": "Barkeep Roland",
        "location": ("Paris", "Tavern"),
        "description": (
            "Bandits drunk on stolen ale cause chaos in the Paris Tavern. "
            "Roland pleads for your help."
        ),
        "objective": {
            "city": "Paris",
            "tile": "Tavern",
            "enemy": "Bandit",
            "item": "Stolen Ale",
        },
        "reward": {
            "gold": 190,
            "items": ["Iron Tankard"],
            "message": "The tavern returns to peace.",
        },
        "completed": False,
    },
    "City Gate Break-in": {
        "name": "City Gate Break-in",
        "giver": "Captain Lucien",
        "location": ("Paris", "Gatehouse"),
        "description": (
            "Thieves plan to break into the city through the Paris Gatehouse. "
            "Captain Lucien asks you to stop them."
        ),
        "objective": {
            "city": "Paris",
            "tile": "Gatehouse",
            "enemy": "Thief",
            "item": "Lockpicks",
        },
        "reward": {
            "gold": 240,
            "items": ["Bronze Shield"],
            "message": "The gates remain secure.",
        },
        "completed": False,
    },
    "Desert Justice": {
        "name": "Desert Justice",
        "giver": "Sheikh Omar",
        "location": ("Cairo", "Oasis"),
        "description": (
            "Bandits terrorize caravans resting at the Cairo Oasis. "
            "Sheikh Omar demands they be punished."
        ),
        "objective": {
            "city": "Cairo",
            "tile": "Oasis",
            "enemy": "Bandit",
            "item": "Caravan Goods",
        },
        "reward": {
            "gold": 310,
            "items": ["Gold Bracelet"],
            "message": "Justice is served in the desert.",
        },
        "completed": False,
    },
}



def start_quest(quest_name):
    quest = quests.get(quest_name)
    if quest and not quest["completed"]:
        print(f"\n Quest Started: {quest['name']}")
        print(quest["description"])
    else:
        print("This quest is not available or already completed.")


def check_quest_progress(quest_name, city, tile, defeated_enemy, looted_items):
    quest = quests.get(quest_name)

    if not quest or quest.get("completed"):
        print("Quest isn't triggered or already completed.")
        print(defeated_enemy)
        print(looted_items)
        return  # Exit early to avoid errors

    obj = quest["objective"]
    if city == obj["city"] and tile == obj["tile"] and defeated_enemy == obj["enemy"]:
        if obj["item"] in looted_items:
            print(f"\nQuest Update: You recovered the {obj['item']}!")
            complete_quest(quest_name)



def complete_quest(quest_name):
    quest = quests.get(quest_name)
    if quest and not quest["completed"]:
        quest["completed"] = True
        
        reward = quest["reward"]

        shopping.player_gold += reward["gold"]
        for item in reward["items"]:
            shopping.inventory.append(item)

        print(f"\n Quest Completed: {quest['name']}")
        print(reward["message"])
        print(f"You received {reward['gold']} gold and items: {', '.join(reward['items'])}")

def quest_log():
    for name, quest in quests.items():
        status = "Completed" if quest["completed"] else "In Progress"
        print(f"{quest['name']} - {status}")

def trigger_quest_enemy(quest_name, city, tile):
    quest = quests.get(quest_name)
    if not quest or quest["completed"]:
        return None
    obj = quest["objective"]
    if city == obj["city"] and tile == obj["tile"]:
        print(f"You sense danger... {obj['enemy']} is nearby for the quest '{quest['name']}'!")
        return obj["enemy"]
    return None
