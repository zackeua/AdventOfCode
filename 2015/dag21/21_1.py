import sys

from itertools import combinations

class Item:
    
    def __init__(self, name, cost, damage, armor) -> None:
        self._name = name
        self._cost = cost
        self._damage = damage
        self._armor = armor

    def get_cost(self) -> int:
        return self._cost

    def get_damage(self) -> int:
        return self._damage

    def get_armor(self) -> int:
        return self._armor


class character:
    def __init__(self, health, items, name) -> None:
        self._health = health
        self._cost = sum([i._cost for i in items])
        self._attack = sum([i._damage for i in items])
        self._armor = sum([i._armor for i in items])
        self._name = name
    
    def attack(self, other):
        damage = max([1, self._attack - other._armor])
        other._health -= damage
        #print(f'{self._name} deals {other._armor}-{self._attack}={damage} damage; {other._name} goes down to {other._health} hit points.')

weapon_list = [Item('Dagger', 8, 4, 0),
               Item('Whortsword', 10, 5, 0),
               Item('Warhammer', 25, 6, 0),
               Item('Longsword', 40, 7, 0),
               Item('Greataxe', 74, 8, 0)]

armor_list = [Item('Nothing', 0, 0, 0),
              Item('Leather', 13, 0, 1),
              Item('Chainmail', 31, 0, 2),
              Item('Splintmail', 53, 0, 3),
              Item('Bandedmail', 75, 0, 4),
              Item('Platemail', 102, 0, 5)]

ring_list = [Item('Damage+0', 0, 0, 0),
             Item('Defense+0', 0, 0, 0),
             Item('Damage+1', 25, 1, 0),
             Item('Damage+2', 50, 2, 0),
             Item('Damage+3', 100, 3, 0),
             Item('Defense+1', 20, 0, 1),
             Item('Defense+2', 40, 0, 2),
             Item('Defense+3', 80, 0, 3)]



with open(sys.argv[1], 'r') as f:
    data = f.readlines()
    _, boss_health = data[0].split(': ')
    boss_health = int(boss_health)
    _, boss_attack = data[1].split(': ')
    boss_attack = int(boss_attack)
    _, boss_armor = data[2].split(': ')
    boss_armor = int(boss_armor)

min_cost = 100000
for weapon in weapon_list:
    for armor in armor_list:
        for ring1, ring2 in combinations(ring_list, 2):
            player = character(100, [weapon, armor, ring1, ring2], 'The player')
            boss = character(boss_health, [Item('', 0, boss_attack, boss_armor)], 'The boss')
            print('Before:')
            print(f'Player: health: {player._health}, attack: {player._attack}, armor: {player._armor}')
            print(f'Boss: health: {boss._health}, attack: {boss._attack}, armor: {boss._armor}')
            while player._health > 0 and boss._health > 0:
                player.attack(boss)
                if player._health > 0 and boss._health > 0:
                    boss.attack(player)
            
            print('After:')
            print(f'Player: health: {player._health}, attack: {player._attack}, armor: {player._armor}')
            print(f'Boss: health: {boss._health}, attack: {boss._attack}, armor: {boss._armor}')
            print('\n')
            print('\n')

            if player._health > 0 and player._cost < min_cost: min_cost = player._cost

print(min_cost)

# player = character(8, [Item('', 0, 5, 5)], 'The player')
# boss = character(12, [Item('', 0, 7, 2)], 'The boss')
# while player._health > 0 and boss._health > 0:
#     player.attack(boss)
#     if player._health > 0 and boss._health > 0:
#         boss.attack(player)
