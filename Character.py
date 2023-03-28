import random


class Character:
    def __init__(self, name, hp, power):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.power = power
        self.mp = 20

    def attack(self, other):
        damage = random.randint(
            self.power - self.power/10, self.power + self.power/10)
        other.hp = max(other.hp - damage, 0)
        print(f"{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")

    def magic(self, other):
        damage = random.randint(self.mp - 5, self.mp + 5)
        other.hp = max(other.hp - damage, 0)
        print(f"{self.name}의 마법! {other.name}에게 {damage}의 데미지를 입혔습니다.")

    def magic_power(self):
        add_mp = random.randint(0, 10)
        self.mp += add_mp
        print(f"{self.name}의 마법 파워가 {add_mp}만큼 증가하였습니다.")

    def alive(self):
        if self.hp == 0:
            print(f"{self.name}이(가) 죽었습니다.")
            return False

    def show_status(self):
        print(f"{self.name}의 상태: HP {self.hp}/{self.max_hp}")


# class Warrior(Character):
#     def __init__(self, name):
#         self.name = name
#         self.max_hp = 150
#         self.hp = 150
#         self.barrier = 20
#         self.power = 15

#     def barrier(self):
#         self.barrier += 10
#         print(f"{self.name}의 베리어가 10만큼 증가하였습니다.")

#     def strong_attack(self, other):
#         damage = random.randint(self.power + self.barrier,
#                                 self.power + self.barrier + 5)
#         if random.randint(1, 2) > 1:
#             damage = damage*2
#         other.hp = max(other.hp - damage, 0)
#         print(f"{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")

#     def show_status(self):
#         print(f"{self.name}의 상태: HP {self.hp}/{self.max_hp}")
#         print(f"{self.name}의 베리어: barrier {self.barrier}")
