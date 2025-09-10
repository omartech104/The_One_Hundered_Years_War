import pyfiglet

def print_title_screen():
    # Adjust width so the roman font stays readable
    banner = pyfiglet.figlet_format(
        "The One Hundred Years' War",
        font="roman",
        width=120  # try 80, 100, 120 depending on your terminal
    )
    print(banner)

