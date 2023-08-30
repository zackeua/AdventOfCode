import sys

class Character:

    def __init__(self, hit_points: int, damage: int, mana: int = 0, mana_spent: int = 0, shield_effect: int = 0, poison_effect: int = 0, recharge_effect: int = 0) -> None:
        self.hit_points = hit_points
        self.damage = damage
        self.mana = mana
        self.mana_spent = mana_spent
        self.shield_effect = shield_effect
        self.poison_effect = poison_effect
        self.recharge_effect = recharge_effect

    def __copy__(self):
        return Character(self.hit_points,
                         self.damage,
                         self.mana,
                         self.mana_spent,
                         self.shield_effect,
                         self.poison_effect,
                         self.recharge_effect)

    def attack(self, amount: int):
        armour = 7 * (self.shield_effect > 0)
        self.hit_points -= max(1, amount - armour)

    def shield_trigger(self):
        if self.shield_effect:
            self.shield_effect -= 1

    def shield(self):
        assert self.can_shield()
        self.shield_effect = 6
        self.mana -= 113
        self.mana_spent += 113

    def can_shield(self):
        return self.shield_effect == 0 and self.mana > 113

    def recharge_trigger(self):
        if self.recharge_effect:
            self.mana += 101
            self.recharge_effect -= 1

    def recharge(self):
        assert self.can_recharge()
        self.recharge_effect = 5
        self.mana -= 229
        self.mana_spent += 229
    
    def can_recharge(self):
        return self.recharge_effect == 0 and self.mana > 229
    


    def poison_attack(self, other):
        poison_damage = 3
        if self.poison_effect:
            other.hit_points -= poison_damage
            self.poison_effect -= 1
    
    def poison(self):
        assert self.can_poison() 
        self.poison_effect = 6
        self.mana -= 173
        self.mana_spent += 173
    
    def can_poison(self):
        return self.poison_effect == 0 and self.mana > 173


    def drain_attack(self, other):
        assert self.can_drain()
        drain_damage = 2
        other.hit_points -= drain_damage
        self.hit_points += drain_damage
        self.mana -= 73
        self.mana_spent += 73

    def can_drain(self):
        return self.mana > 73


    def missile_attack(self, other):
        assert self.can_missile_attack()
        missile_damage = 4
        other.hit_points -= missile_damage
        self.mana -= 53
        self.mana_spent += 53


    def can_missile_attack(self):
        return self.mana > 53

    def to_low_mana(self):
        return not (self.can_shield() or self.can_recharge() or self.can_poison() or self.can_drain() or self.can_missile_attack())




def simulate(player: Character, boss: Character, min_mana_spent: int = sys.float_info.max, turn: int = 1):
    
    #print('hej')
    if turn % 2 == 1:
        player.hit_points -= 1
        if player.hit_points <= 0:
            return sys.float_info.max
    player.shield_trigger()
    player.poison_attack(boss)
    player.recharge_trigger()

    if boss.hit_points <= 0:
        #print('case 1')
        return player.mana_spent 
    elif player.hit_points <= 0:
        #print('case 2')
        return sys.float_info.max
    elif player.to_low_mana():
        #print('case 3')
        return sys.float_info.max
    elif player.mana_spent > min_mana_spent:
        #print('case 4')
        return sys.float_info.max
    
    if turn % 2 == 0:
        player.attack(boss.damage)
        return simulate(player, boss, min_mana_spent, turn+1)
    else:

        if player.can_poison(): # and turn in [7]:
            new_person = player.__copy__()
            new_boss = boss.__copy__()
            new_person.poison()
            new_mana_spent = simulate(new_person, new_boss, min_mana_spent, turn+1)
            min_mana_spent = min(min_mana_spent, new_mana_spent)

        if player.can_recharge(): #  and turn in [1]:
            new_person = player.__copy__()
            new_boss = boss.__copy__()
            new_person.recharge()
            new_mana_spent = simulate(new_person, new_boss, min_mana_spent, turn+1)
            min_mana_spent = min(min_mana_spent, new_mana_spent)

        if player.can_shield(): #  and turn in [3]:
            new_person = player.__copy__()
            new_boss = boss.__copy__()
            new_person.shield()
            new_mana_spent = simulate(new_person, new_boss, min_mana_spent, turn+1)
            min_mana_spent = min(min_mana_spent, new_mana_spent)

        if player.can_drain(): #  and turn in [5]:
            new_person = player.__copy__()
            new_boss = boss.__copy__()
            new_person.drain_attack(new_boss)
            new_mana_spent = simulate(new_person, new_boss, min_mana_spent, turn+1)
            min_mana_spent = min(min_mana_spent, new_mana_spent)

        if player.can_missile_attack(): #  and turn in [9]:
            new_person = player.__copy__()
            new_boss = boss.__copy__()
            new_person.missile_attack(new_boss)
            new_mana_spent = simulate(new_person, new_boss, min_mana_spent, turn+1)
            min_mana_spent = min(min_mana_spent, new_mana_spent)


    return min_mana_spent

        


def main():
    with open(sys.argv[1], 'r') as f:
        data = f.readlines()
        
        Boss = Character(int(data[0].split(':')[1]), int(data[1].split(':')[1]))
        #Boss = Character(14, 8)



        Player = Character(50, 4, 500)

        min_mana = simulate(Player, Boss)
        print(min_mana)
        assert min_mana > 424

if __name__ == '__main__':
    main()