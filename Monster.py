from Character import Character


class Monster(Character):
    def __init__(self):
        self.name = 'monster'
        self.max_hp = 100
        self.hp = 100
        self.power = 10
        self.attack_dmg = 0
