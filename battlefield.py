from fleet import Fleet
from herd import Herd


class Battlefield:

    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()



    def run_game(self):
        self.display_greeting()
        self.battle()


    def display_greeting(self):
        print('Welcome to Robots Vs Dinosaurs!')


    def battle(self):
        turn1 = input('Who goes first? robots or dinos')

        if turn1 == 'dinos':
            while self.herd.dinos[0].health > 0 or self.fleet.robots[0].health > 0:
                if len(self.herd.dinos) > 0 and len(self.fleet.robots) > 0:
                    self.dino_turn()
                    self.robot_turn()
                    if self.herd.dinos[0].health <= 0:
                            self.herd.dinos.remove(self.herd.dinos[0])
                    elif self.fleet.robots[0].health <= 0:
                            self.fleet.robots.remove(self.fleet.robots[0])
                else:
                    self.display_winner()
                    break

        elif turn1 == 'robots':
            while self.fleet.robots[0].health > 0 or self.herd.dinos[0].health > 0:
                if len(self.herd.dinos) > 0 and len(self.fleet.robots) > 0:
                    self.robot_turn()
                    self.dino_turn()
                    if self.fleet.robots[0].health <= 0:
                        self.fleet.robots.remove(self.fleet.robots[0])
                    elif self.herd.dinos[0].health <= 0:
                        self.herd.dinos.remove(self.herd.dinos[0])
                else:
                    self.display_winner()
                    break








    def dino_turn(self):
        self.herd.dinos[0].attack_robot(self.fleet.robots[0])

    def robot_turn(self):
        self.fleet.robots[0].attack_dino(self.herd.dinos[0])



    def dino_opponent_options(self):
        pass


    def robot_opponent_options(self):
        pass

    def display_winner(self):
        if len(self.herd.dinos) == 0:
            print('Robots Win!')
        elif len(self.fleet.robots) == 0:
            print('Dinosaurs Win!')

