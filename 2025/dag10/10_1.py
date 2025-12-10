# /// script
# dependencies = [
#   "minizinc",
# ]
# ///
import sys
import re

from minizinc import Instance, Model, Solver


def main():
    with open(sys.argv[1], "r") as f:
        data = f.readlines()
        data = [line.strip() for line in data]
        for line in data:
            elems = line.split(" ")
            indicator_lights = elems[0]
            joltage_requirements = elems[-1]
            button_wiring_schematics = elems[1:-1]
            button_wiring_schematics = [
                list(map(int, elem[1:-1].split(",")))
                for elem in button_wiring_schematics
            ]

            # print(indicator_lights, button_wiring_schematics, joltage_requirements)

            indicator_light_constraint = [
                f"{'not ' if elem == '.' else ''}light_{i}"
                for i, elem in enumerate(indicator_lights[1:-1])
            ]
            indicator_light_constraint = (
                "constraint " + " /\\ ".join(indicator_light_constraint) + ";"
            )
            print(indicator_light_constraint)

            for i, elem in enumerate(indicator_lights[1:-1]):
                button_constraint = []
                for j, button in enumerate(button_wiring_schematics):
                    if i in button:
                        button_constraint.append(f"button_{j}")
                button_constraint = (
                    f"constraint light_{i} = ("
                    + " + ".join(button_constraint)
                    + ") mod 2 = 0;"
                )
                print(button_constraint)
            for i, button in enumerate(button_wiring_schematics):
                pass

            print(elems)
        # print(data)


if __name__ == "__main__":
    main()
