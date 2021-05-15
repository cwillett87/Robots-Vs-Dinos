from dinosaur import Dinosaur

class Herd:

    def __init__(self):
        self.dinos = []
        self.move_to_heard()


    def move_to_heard(self):
        dino_1 = Dinosaur('T-rex', 40)
        dino_2 = Dinosaur('Raptor', 25)
        dino_3 = Dinosaur('Pterodactyl', 35)
        self.dinos.append(dino_1)
        self.dinos.append(dino_2)
        self.dinos.append(dino_3)