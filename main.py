import random
import time
from Character import Character
from Monster import Monster


# from Character import Warrior

# class Character:
#     def __init__(self, name, hp, power):
#         self.name = name
#         self.max_hp = hp
#         self.hp = hp
#         self.power = power
#         self.mp = 20

#     def attack(self, other):
#         damage = random.randint(self.power - 2, self.power + 2)
#         other.hp = max(other.hp - damage, 0)
#         print(f"{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")

#     def magic(self, other):
#         damage = random.randint(self.mp - 5, self.mp + 5)
#         other.hp = max(other.hp - damage, 0)
#         print(f"{self.name}의 마법! {other.name}에게 {damage}의 데미지를 입혔습니다.")

#     def magic_power(self):
#         add_mp = random.randint(0, 10)
#         self.mp += add_mp
#         print(f"{self.name}의 마법 파워가 {add_mp}만큼 증가하였습니다.")

#     def alive(self):
#         if self.hp == 0:
#             print(f"{self.name}이(가) 죽었습니다.")
#             return False

#     def show_status(self):
#         print(f"{self.name}의 상태: HP {self.hp}/{self.max_hp}")


# class Monster(Character):
#     def __inti__(self):
#         super().__init__()


def intro():
    print("="*75)
    print("\t\t\t\tStart Game")
    print("="*75)


def ending():
    print("="*75)
    time.sleep(1)
    if player.hp == 0:
        print("당신은 패배했습니다.")

    if monster.hp == 0:
        print("당신은 승리했습니다.")


def status(player, monster):
    player.show_status()
    monster.show_status()


def player_turn(player, monster):

    print(f"{player.name}의 순서")

    input_ = input("공격 타입을 고르세요\n1. 일반 공격\t2.마법공격\t3.마법 공격력 증가\n")

    if input_ != '1' and input_ != '2' and input_ != '3':
        print("잘못된 선택입니다. 랜덤한 공격이 출력됩니다.")
        input_ = str(random.randint(1, 3))

    if input_ == '1':
        player.attack(monster)
    elif input_ == '2':
        player.magic(monster)
    elif input_ == '3':
        player.magic_power()


def monster_turn(monster, player):

    print(f"{monster.name}의 순서")

    monster.attack(player)

# def create_char() :


intro()

# print("Choose Player : ")

# input_ = input("1. warrior\t2. Wizard\t3. Bowman\n")
# if input_ == '1':
#     choose_class = Warrior

set_name = input("Player Name : ")

choose_class = Character
# choose_class = Warrior

player = choose_class(set_name, 100, 10)
# player = choose_class(set_name)

monster = Monster('monster', 100, 10)

# player = choose_class


while True:
    status(player, monster)
    time.sleep(1)
    print("="*75)

    player_turn(player, monster)

    if monster.alive() == False:
        break

    time.sleep(1)

    monster_turn(monster, player)

    if player.alive() == False:
        break

    time.sleep(1)

    print("="*75)

ending()
