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
            "tile": "Louvre",
            "enemy": "Bandit",
            "item": "Ancient Relic",
        },
        "reward": {
            "gold": 300,
            "items": ["Blessed Wine"],
            "message": "You have proven yourself a true protector of the faith.",
        },
        "completed": False,
    },
    "Missing ring": {
        "name": "The Missing ring",
        "giver": "Fatima The Merchant",  # NPC
        "location": ("Cairo", "Bazaar"),  # City and tile
        "description": (
            "In Bazaar, You find Fatima the Merchant "
            "A golden ring has been stolen by a thief and hidden in the citadel."
        ),
        "objective": {"city": "Cairo", "tile": "Citadel", "enemy": "Thief", "item": "Golden Ring"},
        "reward": {
            "gold": 450,
            "items": ["A Ruby"],
            "message": "You found it! My heart is lighter now. Take this gift as thanks.",
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
    if not quest or quest["completed"]:
        return

    obj = quest["objective"]
    if city == obj["city"] and tile == obj["tile"] and defeated_enemy == obj["enemy"]:
        if obj["item"] in looted_items:
            print(f"\n Quest Update: You recovered the {obj['item']}!")
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

