import sys


class Collection:
    def __init__(self, ore: int, clay: int, obsidian: int, geode: int) -> None:
        self.ore = ore
        self.clay = clay
        self.obsidian = obsidian
        self.geode = geode


    def __add__(self, __value: object) -> object:
        if type(__value) == tuple:
            return Collection(self.ore + __value[0], self.clay + __value[1], self.obsidian + __value[2], self.geode + __value[3])
        return Collection(self.ore + __value.ore, self.clay + __value.clay, self.obsidian + __value.obsidian, self.geode + __value.geode)

    def __sub__(self, other):
        if type(other) == tuple:
            return Collection(self.ore + other[0], self.clay + other[1], self.obsidian + other[2], self.geode + other[3])
        return Collection(self.ore + other.ore, self.clay + other.clay, self.obsidian + other.obsidian, self.geode + other.geode)


    def __repr__(self) -> str:
        return f'(ore={self.ore}, clay={self.clay}, obsidian={self.obsidian}, geode={self.geode})'

    def __eq__(self, other):
        if type(other) == tuple:
            return self.ore == other[0] and self.clay == other[1] and self.obsidian == other[2] and self.geode == other[3]
        return self.ore == other.ore and self.clay == other.clay and self.obsidian == other.obsidian and self.geode == other.geode

    def __lt__(self, other):
        if type(other) == tuple:
            return self.ore < other[0] and self.clay < other[1] and self.obsidian < other[2] and self.geode < other[3]
        return self.ore < other.ore and self.clay < other.clay and self.obsidian < other.obsidian and self.geode < other.geode

    def __le__(self, other):
        if type(other) == tuple:
            return self.ore <= other[0] and self.clay <= other[1] and self.obsidian <= other[2] and self.geode <= other[3]
        return self.ore <= other.ore and self.clay <= other.clay and self.obsidian <= other.obsidian and self.geode <= other.geode
    
    def __hash__(self) -> int:
        return 1000 * self.ore + 100 * self.clay + 10 * self.obsidian + self.geode


class State:
    def __init__(self, robots: Collection, materials: Collection, timestamp: int) -> None:
        self.robots = robots
        self.materials = materials
        self.timestamp = timestamp

    def __eq__(self, __value: object) -> bool:
        return self.robots == __value.robots and \
               self.materials == __value.materials and \
               self.timestamp == __value.timestamp
    
    def __hash__(self) -> int:
        return 100 * hash(self.robots) + 10 * hash(self.materials) + self.timestamp

    def __repr__(self) -> str:
        return f'\n---\nRobots: {repr(self.robots)}\nMaterials: {repr(self.materials)}\nTimestamp: {self.timestamp}'


class Blueprint:
    def __init__(self, ore: Collection, clay: Collection, obsidian: Collection, geode: Collection) -> None:
        self.ore = ore
        self.clay = clay
        self.obsidian = obsidian
        self.geode = geode

    def __repr__(self) -> str:
        return f'Blueprint(\nore={self.ore},\nclay={self.clay},\nobsidian={self.obsidian},\ngeode={self.geode})'


def optimize_blueprint(blueprint: Blueprint, depth: int = 1, state: State = State(Collection(1, 0, 0, 0), Collection(0, 0, 0, 0), 1) , allow_build: Collection = Collection(True, True, True, True), all_states: dict[State, int] = {}) -> tuple[int, dict]:

    materials = state.materials
    robots = state.robots
    timestamp = state.timestamp

    result = materials.geode


    if allow_build == Collection(False, False, False, False):
        all_states[state] = result
        return result, all_states

    if state in all_states:
        return all_states[state], all_states
    
    for tmp_state in all_states:
        if tmp_state.materials == materials and tmp_state.robots == robots and tmp_state.timestamp < timestamp:
            return all_states[tmp_state], all_states


    if depth > 24:
        all_states[State(robots, materials, depth)] = result
        return result, all_states

    
    test_materials = materials + robots
    test_state = State(robots, test_materials, depth)
    could_build = False
    if blueprint.geode <= materials and allow_build.geode:
        test_robots = robots + (0, 0, 0, 1)
        test_state = State(test_robots, test_materials - blueprint.geode, depth)
        test_result, all_states = optimize_blueprint(blueprint, depth + 1, test_state, allow_build, all_states)
        result = max(result, test_result)
        could_build = True

    if blueprint.obsidian <= materials and allow_build.obsidian:
        test_robots = robots + (0, 0, 1, 0)
        test_state = State(test_robots, test_materials - blueprint.obsidian, depth)
        test_result, all_states = optimize_blueprint(blueprint, depth + 1, test_state, allow_build, all_states)
        result = max(result, test_result)
        could_build = True


    if blueprint.clay <= materials and allow_build.clay:
        test_robots = robots + (0, 1, 0, 0)
        test_state = State(test_robots, test_materials - blueprint.clay, depth)
        test_result, all_states = optimize_blueprint(blueprint, depth + 1, test_state, allow_build, all_states)
        result = max(result, test_result)
        could_build = True


    if blueprint.ore <= materials and allow_build.ore:
        test_robots = robots + (1, 0, 0, 0)
        test_state = State(test_robots, test_materials - blueprint.ore, depth)
        test_result, all_states = optimize_blueprint(blueprint, depth + 1, test_state, allow_build, all_states)
        result = max(result, test_result)
        could_build = True

    if could_build:
        allow_build = Collection(not blueprint.ore <= materials, not blueprint.clay <= materials, not blueprint.obsidian <= materials, not blueprint.geode <= materials)
    
    test_result, all_states = optimize_blueprint(blueprint, depth + 1, test_state, allow_build, all_states)
    result = max(result, test_result)


    all_states[State(materials, robots, depth)] = result

    return result, all_states


def main():
    with open(sys.argv[1], 'r') as f:
        blueprint_list = []
        data = f.readlines()

        data = [line.strip().split(':')[1] for line in data]
        data = [[elem.strip() for elem in line.split('.') if elem != ''] for line in data]

        # parse input to datastructres
        for blueprint in data:
            recepie_dictionary = {}
            for recepie_str in blueprint:
                tmp_recepie_dictionary = {'ore': 0, 'clay': 0, 'obsidian': 0, 'geode': 0}

                recepie_str = recepie_str.split(' robot costs ')
                recepie_str[0] = recepie_str[0][5:]
                for mineral in recepie_str[1].split(' and '):
                    tmp_recepie_dictionary[mineral.split(' ')[1]] = int(mineral.split(' ')[0])

                recepie = Collection(**tmp_recepie_dictionary)
                recepie_dictionary[recepie_str[0]] = recepie

            blueprint_list.append(Blueprint(**recepie_dictionary))

        print(blueprint_list)

    # optimize
    for i, blueprint in enumerate(blueprint_list):
        result, other = optimize_blueprint(blueprint)
        print(blueprint)
        print(result)
        #print(other)

    # print result


if __name__ == '__main__':
    main()
