# mechs/ascii_art.py

from rich.console import Console

console = Console()

def welcome_screen():
    art = r'''
          o 
       o^/|\^o
    o_^|\/*\/|^_o
   o\*`'.\|/.'`*/o
    \\\\\\|//////
     {><><@><><}
     `"""""""""`
    '''
    menu = [
        "[bold green]1. NEW GAME[/bold green]",
        "[bold cyan]2. LOAD GAME[/bold cyan]",
        "[bold yellow]3. RULES[/bold yellow]",
        "[bold red]4. QUIT GAME[/bold red]"
    ]

    # Print ASCII art (plain)
    console.print(art)

    # Print colored menu (plain alignment)
    for item in menu:
        console.print(item)

