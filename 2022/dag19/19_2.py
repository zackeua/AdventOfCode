import sys
import time

MAX_DEPTH = 32


class Collection:

    def __init__(self, ore: int, clay: int, obsidian: int, geode: int) -> None:
        self.ore = ore
        self.clay = clay
        self.obsidian = obsidian
        self.geode = geode

    def __add__(self, other: object) -> object:
        return Collection(self.ore + other.ore, self.clay + other.clay, self.obsidian + other.obsidian, self.geode + other.geode)

    def __sub__(self, other):
        return Collection(self.ore - other.ore, self.clay - other.clay, self.obsidian - other.obsidian, self.geode - other.geode)

    def __repr__(self) -> str:
        return f'(ore={self.ore}, clay={self.clay}, obsidian={self.obsidian}, geode={self.geode})'

    def __eq__(self, other):
        return self.ore == other.ore and self.clay == other.clay and self.obsidian == other.obsidian and self.geode == other.geode

    def __lt__(self, other):
        return self.ore < other.ore and self.clay < other.clay and self.obsidian < other.obsidian and self.geode < other.geode

    def __le__(self, other):
        return self.ore <= other.ore and self.clay <= other.clay and self.obsidian <= other.obsidian and self.geode <= other.geode

    def __copy__(self) -> object:
        return Collection(self.ore, self.clay, self.obsidian, self.geode)


class State:
    def __init__(self, robots: Collection, materials: Collection, debug_string: str = "") -> None:
        self.robots = Collection(0, 0, 0, 0) + robots
        self.materials = Collection(0, 0, 0, 0) + materials
        self.debug_string = debug_string

    def __eq__(self, other: object) -> bool:
        return self.robots == other.robots and \
            self.materials == other.materials

    def __hash__(self) -> int:
        return 10 * hash(self.robots) + hash(self.materials)

    def __repr__(self) -> str:
        return f'\n---\nRobots: {repr(self.robots)}\nMaterials: {repr(self.materials)}'

    def show_debug(self) -> None:
        print(self.debug_string)


class Blueprint:
    def __init__(self, ore: Collection, clay: Collection, obsidian: Collection, geode: Collection) -> None:
        self.ore = ore
        self.clay = clay
        self.obsidian = obsidian
        self.geode = geode

        self._max_needed = Collection(max([self.ore.ore, self.clay.ore, self.obsidian.ore, self.geode.ore]),
                                      max([self.ore.clay, self.clay.clay, self.obsidian.clay, self.geode.clay]),
                                      max([self.ore.obsidian, self.clay.obsidian, self.obsidian.obsidian, self.geode.obsidian]),
                                      max([self.ore.geode, self.clay.geode, self.obsidian.geode, self.geode.geode]))

        # self._max_needed = Collection(sys.float_info.max, sys.float_info.max, sys.float_info.max, sys.float_info.max)

    def get_max_needed(self) -> Collection:
        return self._max_needed

    def __le__(self, other: Collection) -> bool:
        blueprint = self
        materials = other
        return (blueprint.ore <= materials and blueprint.clay <= materials and blueprint.obsidian <= materials and blueprint.geode <= materials)

    def __repr__(self) -> str:
        return f'Blueprint(\nore={self.ore},\nclay={self.clay},\nobsidian={self.obsidian},\ngeode={self.geode})'

EMPTY = Collection(0, 0, 0, 0)
ORE = Collection(1, 0, 0, 0)
CLAY = Collection(0, 1, 0, 0)
OBSIDIAN = Collection(0, 0, 1, 0)
GEODE = Collection(0, 0, 0, 1)


def optimize_blueprint(blueprint: Blueprint, depth: int = 1, state: State = State(ORE, EMPTY), allow_build: Collection = Collection(True, True, True, True), current_best_result: int = 0, visited_nodes: int = 0) -> tuple[int, dict]:

    # -1: get values from current state
    materials = state.materials.__copy__()
    robots = state.robots.__copy__()


    test_materials = materials + robots

    result = test_materials.geode

    # 0: early return if possible

    time_left = max(0, (MAX_DEPTH - depth))
    best_upper_bound = result + robots.geode * time_left + time_left*(time_left+1)/2

    # If you can't get enough resources to beat the best result, skip simulating more minutes
    if best_upper_bound < current_best_result:
        return result, state.debug_string, 1 + visited_nodes

    # If you are not allowed to build any more robots, skip simulating more minutes
    if allow_build == Collection(False, False, False, False):
        return result, state.debug_string, 1 + visited_nodes

    # end recursion at minute MAX_DEPTH (32)
    if depth == MAX_DEPTH:
        return result, state.debug_string, 1 + visited_nodes

    # 1: get materials repending on how many robots you curently have


    # try to build a robot
    allow_build_nothing_built = allow_build.__copy__()
    test_repr = "" + state.debug_string
    if blueprint.geode <= materials and allow_build.geode:
        test_robots = robots + GEODE
        tmp_allow_build = allow_build.__copy__()
        test_state = State(test_robots, test_materials - blueprint.geode, state.debug_string + 'g')
        new_result, new_repr, new_visited_nodes = optimize_blueprint(blueprint, depth + 1, test_state, tmp_allow_build, result, visited_nodes)
        result = max(result, new_result)
        if result == new_result:
            test_repr = new_repr
        visited_nodes = new_visited_nodes
        allow_build_nothing_built.geode = False
    else: # dont bother trying anything else if you can build a geode robot

        if blueprint.obsidian <= materials and allow_build.obsidian:
            test_robots = robots + OBSIDIAN
            tmp_allow_build = allow_build.__copy__()
            tmp_allow_build.obsidian = blueprint.get_max_needed().obsidian > test_robots.obsidian
            test_state = State(test_robots, test_materials - blueprint.obsidian, state.debug_string + '*')
            new_result, new_repr, new_visited_nodes = optimize_blueprint(blueprint, depth + 1, test_state, tmp_allow_build, result, visited_nodes)
            result = max(result, new_result)
            if result == new_result:
                test_repr = new_repr
            visited_nodes = new_visited_nodes
            allow_build_nothing_built.obsidian = False

        if blueprint.clay <= materials and allow_build.clay:
            test_robots = robots + CLAY
            tmp_allow_build = allow_build.__copy__()
            tmp_allow_build.clay = blueprint.get_max_needed().clay > test_robots.clay
            test_state = State(test_robots, test_materials - blueprint.clay, state.debug_string + 'c')
            new_result, new_repr, new_visited_nodes = optimize_blueprint(blueprint, depth + 1, test_state, tmp_allow_build, result, visited_nodes)
            result = max(result, new_result)
            if result == new_result:
                test_repr = new_repr
            visited_nodes = new_visited_nodes
            allow_build_nothing_built.clay = False

        if blueprint.ore <= materials and allow_build.ore:
            test_robots = robots + ORE
            tmp_allow_build = allow_build.__copy__()
            tmp_allow_build.ore = blueprint.get_max_needed().ore > test_robots.ore and depth < MAX_DEPTH - blueprint.ore.ore # no need to build ore robot if it cant repay itself
            test_state = State(test_robots, test_materials - blueprint.ore, state.debug_string + 'o')
            new_result, new_repr, new_visited_nodes = optimize_blueprint(blueprint, depth + 1, test_state, tmp_allow_build, result, visited_nodes)
            result = max(result, new_result)
            if result == new_result:
                test_repr = new_repr
            visited_nodes = new_visited_nodes
            allow_build_nothing_built.ore = False

        # Try skip building robot, i.e. save resources til later
        if not (blueprint <= materials):
            test_state = State(robots, test_materials, state.debug_string + '.')
            new_result, new_repr, new_visited_nodes = optimize_blueprint(blueprint, depth + 1, test_state, allow_build_nothing_built, result, visited_nodes)
            result = max(result, new_result)
            if result == new_result:
                test_repr = new_repr
            visited_nodes = new_visited_nodes
    
    return result, test_repr, visited_nodes


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

    total = 1
    # optimize
    for i, blueprint in enumerate(blueprint_list[:3], start=1):
        t1 = time.time()
        partial_result, result_string, visited_nodes = optimize_blueprint(blueprint, 1)
        print(blueprint)
        print(result_string)
        print('Blueprint result: ', partial_result)
        print('visited nodes: ', visited_nodes)
        print('Blueprint time: ', time.time() - t1)

        total *= partial_result

    # print total
    print(total)
    assert (total > 2145)


if __name__ == '__main__':
    main()
