import random


class Character:
    def __init__(self, name, hp, power):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.power = power
        self.mp = 20
        self.attack_dmg = 0

    def attack(self, other):
        self.attack_dmg = self.power
        if random.randint(1, 2) > 1:
            self.attack_dmg = self.attack_dmg*2
        print(f"{self.name}의 공격!")
        other.attacked_by_other(self)

    def magic(self, other):
        self.attack_dmg = random.randint(self.mp - 5, self.mp + 5)
        print(f"{self.name}의 마법!")
        other.attacked_by_other(self)

    def magic_power(self):
        add_mp = random.randint(0, 10)
        self.mp += add_mp
        print(f"{self.name}의 마법 파워가 {add_mp}만큼 증가하였습니다.")

    def attacked_by_other(self, other):
        self.hp = self.hp - other.attack_dmg
        print(f"{self.name}에게 {other.attack_dmg}의 데미지를 입혔습니다.")

    def alive(self):
        if self.hp <= 0:
            print(f"{self.name}이(가) 죽었습니다.")
            return False

    def show_status(self):
        print(f"{self.name}의 상태: HP {self.hp}/{self.max_hp}")


class Warrior(Character):
    def __init__(self, name):
        self.name = name
        self.max_hp = 150
        self.hp = 150
        self.barrier = 10
        self.power = 15

    def inc_barrier(self):
        self.barrier += 10
        print(f"{self.name}의 베리어가 10만큼 증가하였습니다.")

    def strong_attack(self, other):
        self.attack_dmg = self.barrier
        if random.randint(1, 2) > 1:
            self.attack_dmg = self.attack_dmg*2
        print(f"{self.name}의 강공격!")
        other.attacked_by_other(self)

    def show_status(self):
        print(
            f"{self.name}의 상태: HP {self.hp}/{self.max_hp}\tbarrier {self.barrier}")

    def attacked_by_other(self, other):
        if self.barrier > 0:
            self.barrier = self.barrier - other.attack_dmg

        if self.barrier < 0:
            self.hp = self.hp + self.barrier
            self.barrier = 0

        print(f"{self.name}에게 {other.attack_dmg}의 데미지를 입혔습니다.")
