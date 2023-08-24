import sys


class Collection:

    EMPTY = (0, 0, 0, 0)
    ORE = (1, 0, 0, 0)
    CLAY = (0, 1, 0, 0)
    OBSIDIAN = (0, 0, 1, 0)
    GEODE = (0, 0, 0, 1)

    def __init__(self, ore: int, clay: int, obsidian: int, geode: int) -> None:
        self.ore = ore
        self.clay = clay
        self.obsidian = obsidian
        self.geode = geode


    def __add__(self, other: object) -> object:
        if type(other) == tuple:
            return Collection(self.ore + other[0], self.clay + other[1], self.obsidian + other[2], self.geode + other[3])
        return Collection(self.ore + other.ore, self.clay + other.clay, self.obsidian + other.obsidian, self.geode + other.geode)

    def __sub__(self, other):
        if type(other) == tuple:
            return Collection(self.ore - other[0], self.clay - other[1], self.obsidian - other[2], self.geode - other[3])
        return Collection(self.ore - other.ore, self.clay - other.clay, self.obsidian - other.obsidian, self.geode - other.geode)


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

    def __copy__(self) -> object:
        return Collection(self.ore, self.clay, self.obsidian, self.geode)


class State:
    def __init__(self, robots: Collection, materials: Collection, timestamp: int, debug_repr: str = "") -> None:
        self.robots = Collection(0, 0, 0, 0) + robots
        self.materials = Collection(0, 0, 0, 0) + materials
        self.timestamp = timestamp
        self.debug_repr = debug_repr

    def __eq__(self, other: object) -> bool:
        return self.robots == other.robots and \
               self.materials == other.materials and \
               self.timestamp == other.timestamp
    
    def __hash__(self) -> int:
        return 100 * hash(self.robots) + 10 * hash(self.materials) + self.timestamp

    def __repr__(self) -> str:
        return f'\n---\nRobots: {repr(self.robots)}\nMaterials: {repr(self.materials)}\nTimestamp: {self.timestamp}'

    def show_debug(self) -> None:
        print(self.debug_repr)


class Blueprint:
    def __init__(self, ore: Collection, clay: Collection, obsidian: Collection, geode: Collection) -> None:
        self.ore = ore
        self.clay = clay
        self.obsidian = obsidian
        self.geode = geode

    def __repr__(self) -> str:
        return f'Blueprint(\nore={self.ore},\nclay={self.clay},\nobsidian={self.obsidian},\ngeode={self.geode})'


def optimize_blueprint(blueprint: Blueprint, depth: int = 1, state: State = State(Collection.ORE, Collection.EMPTY, 1) , allow_build: Collection = Collection(True, True, True, True), all_states: dict[State, int] = {}) -> tuple[int, dict]:

    ## -1: get values from current state
    materials = state.materials
    robots = state.robots
    timestamp = state.timestamp

    result = materials.geode

    ## 0: early return if possible

    # If you are not allowed to build any more robots, skip simulating more minutes 
    if allow_build == Collection(False, False, False, False):
        all_states[state] = (result, state.debug_repr)
        return result, all_states, state.debug_repr

    # return cached result if it is computed
    if state in all_states:
        return all_states[state][0], all_states, all_states[state][1]
    
    #for tmp_state in all_states:
    #    if tmp_state.materials == materials and tmp_state.robots == robots and tmp_state.timestamp < timestamp:
    #        return all_states[tmp_state], all_states


    # end recursion at minute 24
    if depth > 24:
        all_states[State(robots, materials, depth)] = (result, state.debug_repr)
        return result, all_states, state.debug_repr

    
    ## 1: get materials repending on how many robots you curently have
    
    test_materials = materials + robots

    ## try to build a robot
    new_allow_build = allow_build.__copy__()
    test_repr = state.debug_repr
    if blueprint.geode <= materials and allow_build.geode:
        test_robots = robots + Collection.GEODE
        test_state = State(test_robots, test_materials - blueprint.geode, depth, state.debug_repr + 'g')
        test_result, all_states, new_repr = optimize_blueprint(blueprint, depth + 1, test_state, allow_build, all_states)
        result = max(result, test_result)
        if result == test_result:
            test_repr = new_repr
        new_allow_build.geode = False

    if blueprint.obsidian <= materials and allow_build.obsidian:
        test_robots = robots + Collection.OBSIDIAN
        test_state = State(test_robots, test_materials - blueprint.obsidian, depth, state.debug_repr + '*')
        test_result, all_states, new_repr = optimize_blueprint(blueprint, depth + 1, test_state, allow_build, all_states)
        result = max(result, test_result)
        if result == test_result:
            test_repr = new_repr
        new_allow_build.obsidian = False

    if blueprint.clay <= materials and allow_build.clay:
        test_robots = robots + Collection.CLAY
        test_state = State(test_robots, test_materials - blueprint.clay, depth, state.debug_repr + 'c')
        test_result, all_states, new_repr = optimize_blueprint(blueprint, depth + 1, test_state, allow_build, all_states)
        result = max(result, test_result)
        if result == test_result:
            test_repr = new_repr
        new_allow_build.clay = False

    if blueprint.ore <= materials and allow_build.ore:
        test_robots = robots + Collection.ORE
        test_state = State(test_robots, test_materials - blueprint.ore, depth, state.debug_repr + 'o')
        test_result, all_states, new_repr = optimize_blueprint(blueprint, depth + 1, test_state, allow_build, all_states)
        result = max(result, test_result)
        if result == test_result:
            test_repr = new_repr
        new_allow_build.ore = False



    # Try skip building robot, i.e. save resources til later 
    test_state = State(robots, test_materials, depth, state.debug_repr + '.')
    test_result, all_states, new_repr = optimize_blueprint(blueprint, depth + 1, test_state, new_allow_build, all_states)
    result = max(result, test_result)
    if result == test_result:
        test_repr = new_repr

    all_states[State(materials, robots, depth)] = (result, test_repr)

    return result, all_states, test_repr


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

    total = 0
    # optimize
    for i, blueprint in enumerate(blueprint_list, start=1):
        partial_result, other, result_repr = optimize_blueprint(blueprint)
        print(blueprint)
        print(result_repr)
        print(partial_result)
        
        total += i * partial_result

    # print total
    print(total)


if __name__ == '__main__':
    main()
