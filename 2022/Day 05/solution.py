import os
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
    result = 0
    for line in readFile(f"{fileName}.txt"):
        pass
    return result


def solutionTwo(fileName: str):
    result = 0
    for line in readFile(f"{fileName}.txt"):
        pass
    return result


if __name__ == "__main__":
    answer = Answers()
    assert solutionOne("test") == answer.partOne
    print("Part One: ", solutionOne("input"))
    assert solutionTwo("test") == answer.partTwo
    print("Part Two: ", solutionTwo("input"))
