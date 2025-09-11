import random

class NPC:
    def __init__(self, gender, name, city, location):
        self.gender = gender
        self.name = name
        self.city = city        # City NPC belongs to
        self.location = location  # Specific landmark or tile

    def message_to_player(self, msg=None):
        if not msg:
            msg = random.choice([
                "Welcome, traveler—may your journey be blessed.",
                "Good day to you. Have you heard news from London?",
                "The roads are long and dangers many; stay sharp.",
                "I barter in secrets as well as goods—what do you seek?",
                "They say the Pyramids glow at dusk. Have you seen them?",
                "Be strong. Fortune favors the bold.",
                "Spare some coin? A small donation for a hungry soul.",
                "The Templars passed through here yesterday. Rumors follow.",
                "Your weapon looks worn. Might be time for a new blade.",
                "A loaf of bread is more precious than gold when hungry.",
                "Drink this wine by candlelight—it soothes the heart.",
                "Books hold power. Read, learn, you’ll survive longer.",
                "Music in the tavern tonight—come join if you can handle the ale.",
                "May your shields hold, and your blade stay sharp.",
                "Yesterday’s storms destroyed the bridge outside town.",
                "If you help a stranger, the gods will help you in return.",
                "Beware the bandits at dusk—they know every winding path.",
                "Even the simplest traveler has tales to share.",
                "Let me tell you of the old wars and the ghosts they left behind."

            ])
        print(f"{self.name} ({self.gender}) at {self.location}, {self.city}: {msg}")


# Names
female_names = [
    "Adelaide","Beatrice","Cecilia","Eleanor","Isolde",
    "Matilda","Rosalind","Margery","Clarissa","Sibyl",
    "Christiana","Aveline","Emmeline","Isabella","Joan",
    "Agnes","Alice","Amice","Constance","Gisela",
    "Helena","Juliana","Lucia","Melisende","Philippa",
    "Rowena","Seraphina","Theodora","Yolande","Brunhild"
]

male_names = [
    "Alaric","Baldwin","Cedric","Godfrey","Leofric",
    "Oswald","Roland","Geoffrey","Hugh","William",
    "Richard","Robert","Edmund","Harold","Thomas",
    "Anselm","Bartholomew","Berengar","Charles","Eustace",
    "Frederick","Gerard","Hubert","Lambert","Louis",
    "Odo","Percival","Ranulf","Simon","Walter"
]


# Landmarks per city
city_landmarks = {
    "London": ["Market", "Castle", "Tower", "Bridge", "Docks", "Gatehouse", "Crossroad", "Road"],
    "Paris": ["Market", "Cathedral", "Louvre", "Tavern", "Gatehouse", "Inn", "Crossroad", "Road"],
    "Cairo": ["Bazaar", "Pyramids", "Mosque", "Citadel", "Oasis", "Caravanserai", "Crossroad", "Road"]
}

# Weighted spawn rates → Markets & Inns busier
landmark_weights = {
    "Market": 6,
    "Bazaar": 6,
    "Inn": 5,
    "Tavern": 5,
    "Cathedral": 4,
    "Castle": 4,
    "Tower": 4,
    "Mosque": 4,
    "Citadel": 4,
    "Caravanserai": 3,
    "Bridge": 3,
    "Gatehouse": 3,
    "Oasis": 2,
    "Crossroad": 2,
    "Road": 1,
    "Louvre": 3,
    "Pyramids": 3,
}


# NPC List
npc_list = []


def weighted_choice(landmarks):
    """Pick a landmark with weighted probability."""
    weights = [landmark_weights.get(l, 1) for l in landmarks]
    return random.choices(landmarks, weights=weights, k=1)[0]


# Generate NPCs for each city
for city, landmarks in city_landmarks.items():
    for _ in range(15):  # 15 NPCs per city
        gender = random.choice(["male", "female"])
        name = random.choice(male_names if gender == "male" else female_names)
        location = weighted_choice(landmarks)
        npc_list.append(NPC(gender, name, city, location))


# Function to check NPCs
def check_for_npcs(current_city, current_tile):
    """Check if NPCs are in the player's current location."""
    npcs_here = [npc for npc in npc_list if npc.city == current_city and npc.location == current_tile]
    if npcs_here:
        print(f"\nYou see {len(npcs_here)} person(s) here:")
        for npc in npcs_here:
            npc.message_to_player()
    else:
        print("\nNo one is here.")

