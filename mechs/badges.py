def get_fighting_module():
    from mechs import fighting
    return fighting
badges = [
    {
        "name": "Bandit Breaker",
        "desc": "Earned by crushing a ruthless bandit in battle. Your strikes now carry legendary force.",
        "boost": lambda: get_fighting_module().player_dp + 40,
        "unlocked": False
    },
    {
        "name": "Master of Coin",
        "desc": "Awarded for striking five deals in the bustling Market. Wealth fuels your vitality.",
        "boost": {"Health": +100},
        "unlocked": False
    },
    {
        "name": "Crown of Triumph",
        "desc": "Bestowed only upon those who complete the grand quest. Your fortune multiplies with every victory.",
        "boost": {"Gold earnings": +2},
        "unlocked": False
    },
    {
        "name": "Wanderer's Emblem",
        "desc": "Granted to those who have tread upon every path, from castles to deserts. The world itself aids your recovery.",
        "boost": {"Healing": +35},
        "unlocked": False
    }
]


unlocked_badges = []
def add_badges():
    for badge in badges:
        if badge["unlocked"] and badge not in unlocked_badges:
            badge["boost"]()
            unlocked_badges.append(badge)
    

def view_badges():
    add_badges()
    if unlocked_badges:
        print("Your badges: ")
        
        for idx, badge in enumerate(unlocked_badges,1):
            print(f"{idx}. {badge['name']}")
        print("Type a badge number to view it's details")
        badge_choice = input("> ")
        if badge_choice.isdigit():
            badge_choice = int(badge_choice) - 1
            if 0 <= badge_choice < len(unlocked_badges):
                print(unlocked_badges[badge_choice]["name"])
                print(unlocked_badges[badge_choice]["desc"])

            else:
                print("Invalid choice.")
        else:
            print("Invalid input.")
    else:
        print("You haven't unlocked any badges")
