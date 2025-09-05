# Adding maps

# London Map (7x7)
london_map = [
    [".", ".", ".", ".", ".", ".", "."],
    [".", "Tower", ".", ".", ".", "Bridge", "."],
    [".", ".", ".", "London", ".", ".", "."],
    [".", "Castle", ".", ".", ".", "Market", "."],
    [".", ".", ".", ".", ".", ".", "."],
    [".", "Docks", ".", ".", ".", "Gatehouse", "."],
    [".", ".", ".", ".", ".", ".", "."]
]

# Paris Map (7x7)
paris_map = [
    [".", ".", ".", ".", ".", ".", "."],
    [".", "Louvre", ".", ".", ".", "Tavern", "."],
    [".", ".", ".", "Paris", ".", ".", "."],
    [".", "Cathedral", ".", ".", ".", "Market", "."],
    [".", ".", ".", ".", ".", ".", "."],
    [".", "Gatehouse", ".", ".", ".", "Inn", "."],
    [".", ".", ".", ".", ".", ".", "."]
]

# Cairo Map (7x7)
cairo_map = [
    [".", ".", ".", ".", ".", ".", "."],
    [".", "Bazaar", ".", ".", ".", "Mosque", "."],
    [".", ".", ".", "Cairo", ".", ".", "."],
    [".", "Pyramids", ".", ".", ".", "Citadel", "."],
    [".", ".", ".", ".", ".", ".", "."],
    [".", "Oasis", ".", ".", ".", "Caravanserai", "."],
    [".", ".", ".", ".", ".", ".", "."]
]


# Setting an init location
init_city = "London"
current_city = "London"
player_pos = london_map[2][3]

def Change_location(dest):
    dest=input("Where You want to Go: ")
    if dest == "London" or dest == "london":
        current_city = "London"
        player_pos = london_map[2][3]
    elif dest == "Paris" or dest == "paris": 
        current_city = "Paris"
        player_pos = paris_map[2][2]
    elif dest == "Cairo" or dest == "cairo": 
        current_city = "Cairo"
        player_pos = cairo_map[2][2]
    else:
        print("Enter a valid destination, Sir")
