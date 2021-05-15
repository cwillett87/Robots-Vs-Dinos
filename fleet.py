from robot import Robot
from weapon import Weapon

class Fleet:

    def __init__(self):
        self.robots = []
        self.put_in_fleet()
    def put_in_fleet(self):
        weapon_1 = Weapon('Uzi', 25)
        weapon_2 = Weapon('AK-47', 35)
        weapon_3 = Weapon('Laser', 50)
        robot_1 = Robot('R2D2',weapon_1)
        robot_2 = Robot('Luke', weapon_2)
        robot_3 = Robot('Jax', weapon_3)
        self.robots.append(robot_1)
        self.robots.append(robot_2)
        self.robots.append(robot_3)