import os, re


class Answers:
    def __init__(self, partOne: int = 0, partTwo: int = 0) -> None:
        self.__partOne = partOne
        self.__partTwo = partTwo

    @property
    def partOne(self):
        return self.__partOne

    @property
    def partTwo(self):
        return self.__partTwo


def readFile(filepath):
    with open(os.path.join(os.path.dirname(__file__), filepath)) as file:
        line = file.readline()
        while line:
            yield line.rstrip("\n")
            line = file.readline()


def solutionOne(fileName: str):
    result = ""
    crate_stack: dict[str, list[str]] = {}
    instruction_regex = r"^move (?P<number_to_move>[0-9]+) from (?P<origin>[0-9]+) to (?P<destination>[0-9]+)$"
    for line in readFile(f"{fileName}.txt"):
        instruction = re.search(instruction_regex, line)
        if not instruction:
            crates = [line[i : i + 4][1] for i in range(0, len(line), 4)]
            num_crates = len(crates)
            for num in range(0, num_crates):
                if crates[num].strip() != "":
                    if not re.search(r"\d", crates[num]):
                        key = str(num + 1)
                        if key in crate_stack.keys():
                            crate_stack[key].insert(0, crates[num])
                        else:
                            crate_stack[key] = [crates[num]]
        if instruction:
            instructions = instruction.groupdict()
            for number in range(0, int(instructions["number_to_move"])):
                crate_stack[instructions["destination"]].append(
                    crate_stack[instructions["origin"]].pop()
                )
    keys = sorted(int(key) for key in crate_stack.keys())
    result = "".join(crate_stack[str(key)][-1] for key in keys)
    return result


def solutionTwo(fileName: str):
    result = ""
    crate_stack: dict[str, list[str]] = {}
    instruction_regex = r"^move (?P<number_to_move>[0-9]+) from (?P<origin>[0-9]+) to (?P<destination>[0-9]+)$"
    for line in readFile(f"{fileName}.txt"):
        instruction = re.search(instruction_regex, line)
        if not instruction:
            crates = [line[i : i + 4][1] for i in range(0, len(line), 4)]
            num_crates = len(crates)
            for num in range(0, num_crates):
                if crates[num].strip() != "":
                    if not re.search(r"\d", crates[num]):
                        key = str(num + 1)
                        if key in crate_stack.keys():
                            crate_stack[key].insert(0, crates[num])
                        else:
                            crate_stack[key] = [crates[num]]
        if instruction:
            instructions = instruction.groupdict()
            crate_stack[instructions["destination"]] += [
                crts
                for crts in crate_stack[instructions["origin"]][
                    -int(instructions["number_to_move"]) :
                ]
            ]
            for number in range(0, int(instructions["number_to_move"])):
                crate_stack[instructions["origin"]].pop()
    keys = sorted(int(key) for key in crate_stack.keys())
    result = "".join(crate_stack[str(key)][-1] for key in keys)
    return result


if __name__ == "__main__":
    answer = Answers("CMZ", "MCD")
    assert solutionOne("test") == answer.partOne
    print("Part One: ", solutionOne("input"))
    assert solutionTwo("test") == answer.partTwo
    print("Part Two: ", solutionTwo("input"))
