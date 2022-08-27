class item(): # define items within the text based game
    "Base for all items within the story"
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)

class Heart(item): #define Heart with a lock from previously dealt hands of life
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="Heart",
        description="the object that everyone looks for and doesn't find the key",
        value=self.amt)

class Key(item): # key to unlocking the heart
    def __init__(self):
        super().__init__(name="Key",
        description="the Key to unlocking his heart",
        value=None)

class Weapon(item): # defining weapon
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)

class Katana(Weapon): #defining sword in inventory
    def __init__(self):
        super().__init__(name="Katana", 
        description="a mighty sword that weilds great power", 
        value=100,
        damage=50)

class Bat(Weapon): # defining bat in inventory
    def __init__(self):
        super().__init__(name="Bat", 
        description="a weapon used to cause bruises",
        value=10,
        damage=15)