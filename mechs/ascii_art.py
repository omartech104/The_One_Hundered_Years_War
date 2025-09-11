import shutil
import pyfiglet

def print_title_screen():
    columns = shutil.get_terminal_size().columns
    banner = pyfiglet.figlet_format("The One Hundred Years' War", font="roman", width=columns)
    print(banner.center(columns))

