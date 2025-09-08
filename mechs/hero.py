class Hero:
   def  __init__(self, hp, dp, weapon):
      self.hp = hp
      self.dp = dp
      self.weapon = weapon
    
class Weapon:
   def __init__(self, kind, heaviness):
      self.kind = kind
      self.heaviness = heaviness

class Hero:
    def __init__ (self, hp, dp, weapon):
        self.hp = hp
        self.dp = dp
        self.weapon = weapon

class Weapon:
    def __init__ (self, kind, heaviness):
        self.kind = kind
        self.heaviness = heaviness

#create weapons
wand = Weapon("small", "light")
dagger = Weapon("small", "medium")
sword = Weapon("large", "light")

# mage assasin warrior
mage = Hero(1000, 400, wand)
assasin = Hero(600, 800, dagger)
warrior = Hero(400, 600, sword)

#mage assasin warrior
mage = Hero(1000, 400, wand)
assasin = Hero(600, 800, dagger)
warrior = Hero(400, 600, sword)

