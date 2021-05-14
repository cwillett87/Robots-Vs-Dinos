from weapon import Weapon
from robot import Robot
from dinosaur import Dinosaur
from fleet import Fleet
from herd import Herd
from battlefield import Battlefield


if __name__ == '__main__':
    weapon_1 = Weapon('Uzi',25)
    weapon_2 = Weapon('AK-47', 35)
    weapon_3 = Weapon('Lazer', 50)
    robot_1 = Robot('R2D2',weapon_1)
    robot_2 = Robot('Luke', weapon_2)
    robot_3 = Robot('Jax', weapon_3)
    dino_1 = Dinosaur('T-rex', 40)
    dino_2 = Dinosaur('Raptor', 25)
    dino_3 = Dinosaur('Terradactle', 35)
    fleet = Fleet()
    fleet.put_in_fleet(robot_1)
    fleet.put_in_fleet(robot_2)
    fleet.put_in_fleet(robot_3)
    herd = Herd()
    herd.move_to_heard(dino_1)
    herd.move_to_heard(dino_2)
    herd.move_to_heard(dino_3)
    battle_1 = Battlefield(fleet, herd)
    robot_1.attack_dino(dino_1)
    dino_1.attack_robot(robot_1)
    print(dino_1)