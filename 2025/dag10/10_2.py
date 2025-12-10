# /// script
# dependencies = [
#   "minizinc",
# ]
# ///
import sys

from minizinc import Instance, Model, Solver


def main():
    with open(sys.argv[1], "r") as f:
        data = f.readlines()
        data = [line.strip() for line in data]
        total = 0
        for line in data:
            elems = line.split(" ")
            indicator_lights = elems[0]
            joltage_requirements = list(map(int, elems[-1][1:-1].split(",")))
            button_wiring_schematics = elems[1:-1]
            button_wiring_schematics = [
                list(map(int, elem[1:-1].split(",")))
                for elem in button_wiring_schematics
            ]
            max_presses = sum(joltage_requirements)
            total_model_str = ""
            for i, button in enumerate(button_wiring_schematics):
                button_constraint = f"var 0..{max_presses}: button_{i};\nconstraint button_{i} >= 0;\n\n"
                # print(i, button)
                # print(button_constraint)
                total_model_str += button_constraint
            total_model_str += "\n"

            for i, elem in enumerate(indicator_lights[1:-1]):
                indicator_light_constraint = []
                eq = 1 if elem == "#" else 0
                for j, button in enumerate(button_wiring_schematics):
                    if i in button:
                        indicator_light_constraint.append(f"button_{j}")
                light_constraint = (
                    "constraint "
                    + " + ".join(indicator_light_constraint)
                    + f" = {joltage_requirements[i]};\n\n"
                )
                # print(light_constraint)
                total_model_str += light_constraint
            total_model_str += "\n"

            # indicator_light_status_constraint = [
            #     f"({'not ' if elem == '#' else ''}light_{i})"
            #     for i, elem in enumerate(indicator_lights[1:-1])
            # ]
            # indicator_light_status_constraint = (
            #     "constraint "
            #     + " /\\ ".join(indicator_light_status_constraint)
            #     + ";\n\n"
            # )
            # total_model_str += indicator_light_status_constraint
            # print(indicator_light_status_constraint)

            total_constraint = []
            for i, _ in enumerate(button_wiring_schematics):
                total_constraint.append(f"button_{i}")

            total_constraint = (
                "var int: total;\nconstraint total >= 0;\nconstraint total = "
                + " + ".join(total_constraint)
                + ";\nsolve minimize total;\n"
            )
            total_model_str += total_constraint

            # print(total_model_str)
            # print(elems)
            # break
            # continue
            gecode = Solver.lookup("gecode")
            trivial = Model()
            trivial.add_string(total_model_str)
            instance = Instance(gecode, trivial)
            result = instance.solve(intermediate_solutions=True)
            total += result.objective
            # print(result.objective)
        print(total)

        # break

        # print(data)


if __name__ == "__main__":
    main()
