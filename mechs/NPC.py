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
                "Greetings, traveler.",
                "The roads are dangerous, beware.",
                "Have you heard the latest news?",
                "Supplies are scarce these days.",
                "May fortune smile upon you."
            ])
        print(f"{self.name} ({self.gender}) at {self.location}, {self.city}: {msg}")


# Names
female_names = ["Adelaide","Beatrice","Cecilia","Eleanor","Isolde",
                "Matilda","Rosalind","Margery","Clarissa","Sibyl",
                "Christiana","Aveline","Emmeline","Isabella","Joan",
                "Agnes","Alice","Amice","Constance","Gisela",
                "Helena","Juliana","Lucia","Melisende","Philippa",
                "Rowena","Seraphina","Theodora","Yolande","Brunhild"]

male_names = ["Alaric","Baldwin","Cedric","Godfrey","Leofric",
              "Oswald","Roland","Geoffrey","Hugh","William",
              "Richard","Robert","Edmund","Harold","Thomas",
              "Anselm","Bartholomew","Berengar","Charles","Eustace",
              "Frederick","Gerard","Hubert","Lambert","Louis",
              "Odo","Percival","Ranulf","Simon","Walter"]

# Landmarks per city
city_landmarks = {
    "London": ["Market", "Castle", "Tower", "Bridge", "Docks", "Gatehouse", "Crossroad", "Road"],
    "Paris": ["Market", "Cathedral", "Louvre", "Tavern", "Gatehouse", "Inn", "Crossroad", "Road"],
    "Cairo": ["Bazaar", "Pyramids", "Mosque", "Citadel", "Oasis", "Caravanserai", "Crossroad", "Road"]
}

npc_list = []

# Generate NPCs for each city
for city, landmarks in city_landmarks.items():
    for name in random.sample(male_names, 5):
        npc_list.append(NPC("male", name, city, random.choice(landmarks)))
    for name in random.sample(female_names, 5):
        npc_list.append(NPC("female", name, city, random.choice(landmarks)))


# Function to check NPCs at current city + tile
def check_for_npcs(current_city, current_tile):
    npcs_here = [npc for npc in npc_list if npc.city == current_city and npc.location == current_tile]
    if npcs_here:
        print(f"\nYou see {len(npcs_here)} person(s) here:")
        for npc in npcs_here:
            npc.message_to_player()
    else:
        print("\nNo one is here.")

