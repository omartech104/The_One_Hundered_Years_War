from mechs import cathedral_boss
from .puzzles import riddle

# --- Maps ---

symbols = {
    "empty": " ",
    "Road": "▪",
    "Crossroad": "+",
    
    # London area
    "London": "L",
    "Castle": "K",     # Keep 'K' for Castle
    "Docks": "D",
    "Gatehouse": "H",  # H = House, avoids clash
    
    # Paris area
    "Paris": "P",
    "Louvre": "V",     # V from LouVre
    "Cathedral": "C",
    "Tavern": "T",
    "Inn": "I",
    
    # Cairo area
    "Cairo": "R",      # R from CaiRo
    "Mosque": "M",
    "Pyramids": "Y",   # Y from pYramids
    "Citadel": "Z",    # Z = citadel stronghold
    "Oasis": "O",
    "Caravanserai": "N", # N = iNn/caravaN, avoids G
    
    # Common locations
    "Armory": "A",
    "Market": "M",     # ⚠ clash with Mosque, so change:
    "Market": "E",     # E = ExchangE
    "Bazaar": "B",
    "Tower": "W",      # W from toWer
    "Bridge": "R",      # ⚠ clash with Cairo, so change:
    "Bridge": "X"      # but Bazaar already B → make Bridge = "X"
}


# London Map (7x7)
london_map = [
    ["Road", "Road", "Road", "Crossroad", "Road", "Road", "Road"],
    ["Road", "Armory", "Tower", "Road", "Road", "Road", "Bridge"],
    ["Road", "Road", "Crossroad", "London", "Crossroad", "Road", "Road"],
    ["Road", "Castle", "Road", "Crossroad", "Road", "Market", "Road"],
    ["Road", "Road", "Road", "Crossroad", "Road", "Road", "Road"],
    ["Road", "Docks", "Road", "Road", "Road", "Gatehouse", "Road"],
    ["Road", "Road", "Road", "Crossroad", "Road", "Road", "Road"]
]

# Paris Map (7x7)
paris_map = [
    ["Road", "Road", "Road", "Crossroad", "Road", "Road", "Road"],
    ["Road", "Armory", "Louvre", "Road", "Road", "Road", "Tavern"],
    ["Road", "Road", "Crossroad", "Paris", "Crossroad", "Road", "Road"],
    ["Road", "Cathedral", "Road", "Crossroad", "Road", "Market", "Road"],
    ["Road", "Road", "Road", "Crossroad", "Road", "Road", "Road"],
    ["Road", "Gatehouse", "Road", "Road", "Road", "Inn", "Road"],
    ["Road", "Road", "Road", "Crossroad", "Road", "Road", "Road"]
]

# Cairo Map (7x7)
cairo_map = [
    ["Road", "Road", "Road", "Crossroad", "Road", "Road", "Road"],
    ["Road", "Bazaar", "Road", "Road", "Road", "Armory", "Mosque"],
    ["Road", "Road", "Crossroad", "Cairo", "Crossroad", "Road", "Road"],
    ["Road", "Pyramids", "Road", "Crossroad", "Road", "Citadel", "Road"],
    ["Road", "Road", "Road", "Crossroad", "Road", "Road", "Road"],
    ["Road", "Oasis", "Road", "Road", "Road", "Caravanserai", "Road"],
    ["Road", "Road", "Road", "Crossroad", "Road", "Road", "Road"]
]

london_landmarks = [
    {"name": "Tower", "coords": (1, 2)},
    {"name": "Bridge", "coords": (1, 6)},
    {"name": "London", "coords": (2, 3)},
    {"name": "Castle", "coords": (3, 1)},
    {"name": "Docks", "coords": (5, 1)},
    {"name": "Gatehouse", "coords": (5, 5)}
]

# Paris Landmarks
paris_landmarks = [
    {"name": "Louvre", "coords": (1, 2)},
    {"name": "Tavern", "coords": (1, 6)},
    {"name": "Paris", "coords": (2, 3)},
    {"name": "Cathedral", "coords": (3, 1)},
    {"name": "Gatehouse", "coords": (5, 1)},
    {"name": "Inn", "coords": (5, 5)}
]

# Cairo Landmarks
cairo_landmarks = [
    {"name": "Mosque", "coords": (1, 6)},
    {"name": "Cairo", "coords": (2, 3)},
    {"name": "Pyramids", "coords": (3, 1)},
    {"name": "Citadel", "coords": (3, 5)},
    {"name": "Oasis", "coords": (5, 1)},
    {"name": "Caravanserai", "coords": (5, 5)}
]

# Starting location
current_city = "London"
player_pos = (2, 3)
cities = ["London", "Paris", "Cairo"]
current_map = london_map


def get_location_name():
    row, col = player_pos
    tile = current_map[row][col]

    # Generic descriptions for roads and crossroads
    if tile == "Road":
        if current_city == "London":
            return "a cobblestone road, damp from the English mist"
        elif current_city == "Paris":
            return "a narrow stone road, echoing with footsteps"
        elif current_city == "Cairo":
            return "a sandy path, warm under the desert sun"
    elif tile == "Crossroad":
        return "a busy crossroad where paths meet"

    # Landmark descriptions
    landmark_descriptions = {
        # London
        "Tower": "The Tower of London, grim and foreboding",
        "Bridge": "A wooden bridge spanning the river",
        "Castle": "The royal castle, strong and majestic",
        "Market": "The bustling London market, full of traders",
        "Docks": "The docks by the Thames, busy with ships",
        "Gatehouse": "The gatehouse guarding the city walls",

        # Paris
        "Louvre": "The Louvre, a palace of kings and art",
        "Tavern": "A lively tavern, filled with laughter and wine",
        "Cathedral": "The great cathedral, its bells tolling",
        "Market": "Parisian market stalls with spices and fabrics",
        "Gatehouse": "The old gatehouse at the edge of Paris",
        "Inn": "A modest inn for weary travelers",

        # Cairo
        "Bazaar": "The Cairo bazaar, alive with merchants and scents",
        "Mosque": "A grand mosque, echoing with prayers",
        "Pyramids": "The great pyramids, ancient and timeless",
        "Citadel": "The Citadel, standing proud over Cairo",
        "Oasis": "A small oasis, refreshing and green",
        "Caravanserai": "A caravanserai where travelers rest"
    }

    if tile in landmark_descriptions:
        return landmark_descriptions[tile]

    # City centers
    if tile in ["London", "Paris", "Cairo"]:
        return f"the heart of {tile}, filled with life and activity"
        
    # Default
    return tile


def get_current_tile():
    row, col = player_pos
    return current_map[row][col]


def get_tile_description():
    row, col = player_pos
    tile = current_map[row][col]

    # Paris Cathedral event
    if tile == "Cathedral" and current_city == "Paris" and cathedral_boss.defeated == False:
        print("You step into the grand Paris Cathedral...")
        cathedral_boss.fight_cathedral_boss()
        return "The Cathedral stands tall, silent after the battle."

    # Cairo Citadel event
    if tile == "Citadel" and current_city == "Cairo":
        if not riddle.solved:
            print("You arrive at the mighty Cairo Citadel...")
            riddle.play_riddle()
            return "The Citadel tests your wisdom with a riddle."
        else:
            return "The Citadel stands silent, its riddle already solved."

    # Generic descriptions
    descriptions = {
        "Market": {
            "London": "You are now in London Market, filled with goods and merchants.",
            "Paris": "You are now in Parisian market stalls with spices and fabrics.",
            "Cairo": "You are now in Cairo Bazaar, bustling with traders and colors."
        },
        "Castle": {
            "London": "You are in the grand London Castle.",
            "Paris": "You are in the fortified Paris Castle.",
            "Cairo": "You are in the historic Cairo Citadel."
        },
        "Tower": {
            "London": "You stand near the tall Tower of London.",
            "Paris": "Near the iconic Paris Tower.",
            "Cairo": "Near the ancient Cairo Tower."
        },
        "Bridge": {"London": "You are on London Bridge.", "Paris": "You are on the Seine bridge.", "Cairo": "Crossing the Nile bridge."},
        "Docks": {"London": "You are at London Docks.", "Paris": "At the port of Paris.", "Cairo": "At Cairo river docks."},
        "Gatehouse": {"London": "At London Gatehouse.", "Paris": "At Paris Gatehouse.", "Cairo": "At Cairo Gatehouse."},
        "Bazaar": {"Cairo": "Cairo Bazaar is bustling with traders and spices."},
        "Cathedral": {"Paris": "You are inside the Paris Cathedral."},
        "Louvre": {"Paris": "You are in the Louvre Museum."},
        "Pyramids": {"Cairo": "The Pyramids tower over you."},
        "Citadel": {"Cairo": "You are in the mighty Cairo Citadel."},
        "Crossroad": {"London": "You are at a London crossroad.", "Paris": "A Paris crossroad.", "Cairo": "Cairo crossroad."},
        "Road": {"London": "Walking along a London street.", "Paris": "Walking along a Paris street.", "Cairo": "Walking along a Cairo street."}
    }

    if tile in ["London", "Paris", "Cairo"]:
        return descriptions.get(tile, {}).get(current_city, f"The heart of {current_city}, filled with life and activity")
    else:
        return descriptions.get(tile, {}).get(current_city, f"You are at {tile} in {current_city}.")


def move(direction: str):
    global player_pos
    row, col = player_pos

    if direction == "N":
        new_pos = (row - 1, col)
    elif direction == "S":
        new_pos = (row + 1, col)
    elif direction == "W":
        new_pos = (row, col - 1)
    elif direction == "E":
        new_pos = (row, col + 1)
    else:
        return "Invalid direction."

    # Check boundaries
    max_row = len(current_map) - 1
    max_col = len(current_map[0]) - 1
    if 0 <= new_pos[0] <= max_row and 0 <= new_pos[1] <= max_col:
        player_pos = new_pos
        return f"You moved {direction} to {get_location_name()}."
    else:
        return "You cannot go that way."


def fast_travel():
    global player_pos
    print("Travel to any landmark")
    if current_city == "London":
        for i,landmark in enumerate(london_landmarks):
            print(f"{i} - {landmark['name']}")
        landmark_num = input("Type the number of the Landmark: ")
        for i,landmark in enumerate(london_landmarks):
            if i == int(landmark_num):
                row, col = player_pos
                new_pos = landmark["coords"]
                player_pos = new_pos
                print(player_pos)
                print(f"You moved to {get_location_name()}.")
    elif current_city == "Paris":
        for i,landmark in enumerate(paris_landmarks):
            print(f"{i} - {landmark['name']}")
        landmark_num = input("Type the number of the Landmark: ")
        for i,landmark in enumerate(paris_landmarks):
            if i == int(landmark_num):
                row, col = player_pos
                new_pos = landmark["coords"]
                player_pos = new_pos
                print(player_pos)
                print(f"You moved to {get_location_name()}.")
    elif current_city == "Cairo":
        for i,landmark in enumerate(cairo_landmarks):
            print(f"{i} - {landmark['name']}")

        landmark_num = input("Type the number of the Landmark: ")
        for i,landmark in enumerate(cairo_landmarks):
            if i == int(landmark_num):
                row, col = player_pos
                new_pos = landmark["coords"]
                player_pos = new_pos
                print(player_pos)
                print(f"You moved to {get_location_name()}.")

