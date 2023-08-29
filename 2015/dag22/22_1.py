import sys

class Character:

    def __init__(self, hit_points: int, damage: int, mana: int = 0, mana_spent: int = 0, shield_effect: int = 0, poison_effect: int = 0, recharge_effect: int = 0, is_boss: bool = False) -> None:
        self.hit_points = hit_points
        self.damage = damage
        self.mana = mana
        self.mana_spent = mana_spent
        self.shield_effect = shield_effect
        self.poison_effect = poison_effect
        self.recharge_effect = recharge_effect
        self.is_boss = is_boss

    def __copy__(self):
        return Character(self.hit_points,
                         self.damage,
                         self.mana,
                         self.mana_spent,
                         self.shield_effect,
                         self.poison_effect,
                         self.recharge_effect,
                         self.is_boss)

    def attack(self, amount: int):
        armour = 7 * self.shield_effect > 0
        self.hit_points -= max(1, amount - armour)

    def shield_trigger(self):
        if self.shield_effect:
            self.shield_effect -= 1

    def recharge(self):
        if self.recharge_effect:
            self.mana += 101
            self.recharge_effect -= 1

    def poison(self, other):
        poison_damage = 3
        if self.poison_effect:
            other.hit_points -= poison_damage
            self.poison_effect -= 1


def simulate(Player1: Character, Player2: Character):
    
    Player1.shield_trigger()
    Player1.poison(Player2)
    Player1.recharge()

    if Player2.hit_points <= 0:
        return Player1.mana_spent if Player2.is_boss else sys.float_info.max 

    
    if Player1.is_boss:
        Player2.attack(Player1.damage)

        


def main():
    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        
        Boss = Character(int(data[0].split(':')[1]), int(data[1].split(':')[1]), is_boss=True)

        Player = Character(50, 4, 500)

        


if __name__ == '__main__':
    main()