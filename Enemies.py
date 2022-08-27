class Enemy: # defining Enemy
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def is_alive(self):
        return self.hp > 0

class Ex_Spouse(Enemy): #defining spouse
    def __init__(self):
        super().__init__(name="Ex", 
        hp = 150,
        damage = 50)

class Life(Enemy): #defining life enemy
    def __init__(self):
        super().__init__(name="Life",
        hp=1000,
        damage=500)