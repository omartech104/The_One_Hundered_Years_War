# riddle.py
from mechs import shopping

solved = False

def get_citadel_riddle():
    riddle_text = (
        "In the Citadel of Cairo, where history stands tall,\n"
        "I ask you about something very small.\n"
        "It cannot be seen by the naked eye,\n"
        "Yet it builds the world, low and high.\n"
        "It gathers, it scatters, in patterns so fine,\n"
        "From it the universe begins its design.\n"
        "What is it?"
    )
    answer = "particle"
    return riddle_text, answer


def play_riddle():
    global solved
    riddle, solution = get_citadel_riddle()
    print("\nRiddle:\n")
    print(riddle)

    user_answer = input("\nEnter your answer: ").strip().lower()

    if user_answer == solution:
        print("\nCorrect! The answer is 'particle'.\nOpen the letter")
        solved = True
        shopping.inventory.append("Letter")
        shopping.player_gold += 400
    else:
        print("\nFalse, try again later.")
        solved = False
