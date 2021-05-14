class Robot:

    def __init__(self, name, Weapon):
        self.name = name
        self.power_level = 100
        self.health = 100
        self.weapon = Weapon

    def attack_dino(self,dinosaur):
        dinosaur.health -= self.weapon.attack_power
        self.power_level -= 15