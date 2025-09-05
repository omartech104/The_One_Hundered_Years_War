import sys, os

pltform = sys.platform

# Clear screen based on OS
def clear_screen():
    if pltform in ("linux", "darwin"):
        os.system("clear")
    elif pltform == "win32":
        os.system("cls")

# Clear at the start
clear_screen()

run = True
menu = True
play = False
rules = False

def draw():
    print("xX--------------------xX")

while run:
    while menu:
        draw()
        print("1, NEW GAME")
        # We'll Work on loading savefile later
        print("2, LOAD GAME")
        print("3, RULES")
        print("4, QUIT GAME")
        draw()

        if rules:
            print("play the game cleanfully")
            rules = False
            choice = ""
            input("> ")
        else:
            choice = input("# ")

        if choice == "1":
            pass
        elif choice == "2":
            pass
        elif choice == "3":
            clear_screen()
            rules = True  # fixed indentation
        elif choice == "4":
            clear_screen()
            print("Farewell, Hero")
            quit()
        else:
            print("Insert a valid command")




