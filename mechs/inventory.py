
from mechs import shopping

def view_inventory():
    inv = shopping.inventory
    if inv:

        print("Your inventory contains:")
        for item in inv:
            print(f"- {item}")
    else:
        print("Your inventory is empty")
        
view_inventory()