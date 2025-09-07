import traveling

player_gold = 100
inventory = []

shops = {
    "London": {
        "Market": {
            "Longsword": {"price": 50, "desc": "A Long sharp blade for battle."},
            "Shield": {"price": 40, "desc": "Protects against attacks."},
            "A loaf of bread": {"price": 5, "desc": "Baked in simple oven"}
        }
    },
    "Paris": {
        "Market": {
            "Book": {"price": 30, "desc": "A tome of medieval knowledge."},
            "Wine": {"price": 20, "desc": "A fine Parisian vintage."},
            "Illuminated Manuscript": {"price": 60, "desc": "A missing part of someting unknown"}
        }
    },
    "Cairo": {
        "Bazaar": {
            "Spices": {"price": 25, "desc": "Exotic spices from the East."},
            "Halum Cheese": {"price": 50, "desc": "A half pound of local-made Cheese"},
            "A copy of matn al-ajrumiyyah": {"price": 100, "desc": "A rare copy of matn al-ajrumiyyah"}
        }
    }
}


