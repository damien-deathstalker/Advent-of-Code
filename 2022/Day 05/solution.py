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
    crate_stack:dict[str, list[str]] = {}
    crate_regex = r"([A-Z])"
    instruction_regex = r"^move (?P<number_to_move>[0-9]+) from (?P<origin>[0-9]+) to (?P<destination>[0-9]+)$"
    count = 1
    for line in readFile(f"{fileName}.txt"):
        crates = re.findall(crate_regex, line)
        if len(crates) > 0:
            crates.reverse()
            crate_stack[str(count)] = crates
            count += 1
        instruction = re.search(instruction_regex, line)
        if instruction:
            instructions = instruction.groupdict()
            for number in range(0, int(instructions["number_to_move"])):
                crate_stack[instructions["destination"]].append(
                    crate_stack[instructions["origin"]].pop()
                )
    result = "".join(x[-1] for x in crate_stack.values())
    return result


def solutionTwo(fileName: str):
    result = ""
    crate_stack:dict[str, list[str]] = {}
    crate_regex = r"([A-Z])"
    instruction_regex = r"^move (?P<number_to_move>[0-9]+) from (?P<origin>[0-9]+) to (?P<destination>[0-9]+)$"
    count = 1
    for line in readFile(f"{fileName}.txt"):
        crates = re.findall(crate_regex, line)
        if len(crates) > 0:
            crates.reverse()
            crate_stack[str(count)] = crates
            count += 1
        instruction = re.search(instruction_regex, line)
        if instruction:
            instructions = instruction.groupdict()
            crate_stack[instructions["destination"]] += [crts for crts in crate_stack[instructions["origin"]][-int(instructions["number_to_move"]):]]
            for number in range(0, int(instructions["number_to_move"])):
                crate_stack[instructions["origin"]].pop()
    result = "".join(x[-1] for x in crate_stack.values())
    return result


if __name__ == "__main__":
    answer = Answers("CMZ", "MCD")
    assert solutionOne("test") == answer.partOne
    print("Part One: ", solutionOne("input"))
    assert solutionTwo("test") == answer.partTwo
    print("Part Two: ", solutionTwo("input"))
