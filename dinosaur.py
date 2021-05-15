class Dinosaur:
    def __init__(self, type, attack_power):
        self.type = type
        self.energy = 100
        self.attack_power = attack_power
        self.health = 100

    def attack_robot(self, robot):
        if self.health > 0 and self.energy >= 20:
            robot.health -= self.attack_power
            self.energy -= 20