import random

class NPC:
    def __init__(self, gender, name):
        self.gender = gender
        self.name = name 

    def message_to_player(self, msg):
        # NPC speaks to the player
        print(f"{self.name} ({self.gender}): {msg}")


female_names = [
    "Adelaide", "Beatrice", "Cecilia", "Eleanor", "Isolde",
    "Matilda", "Rosalind", "Margery", "Clarissa", "Sibyl",
    "Christiana", "Aveline", "Emmeline", "Isabella", "Joan",
    "Agnes", "Alice", "Amice", "Constance", "Gisela",
    "Helena", "Juliana", "Lucia", "Melisende", "Philippa",
    "Rowena", "Seraphina", "Theodora", "Yolande", "Brunhild"
]

male_names = [
    "Alaric", "Baldwin", "Cedric", "Godfrey", "Leofric",
    "Oswald", "Roland", "Geoffrey", "Hugh", "William",
    "Richard", "Robert", "Edmund", "Harold", "Thomas",
    "Anselm", "Bartholomew", "Berengar", "Charles", "Eustace",
    "Frederick", "Gerard", "Hubert", "Lambert", "Louis",
    "Odo", "Percival", "Ranulf", "Simon", "Walter"
]


male_characters = [NPC("male", random.choice(male_names)) for _ in range(30)]
female_characters = [NPC("female", random.choice(female_names)) for _ in range(30)]

for i in range(len(male_characters)):
    print(male_characters[i].name)
    print(male_characters[i].gender)



for i in range(len(female_characters)):
    print(female_characters[i].name)
    print(female_characters[i].gender)


