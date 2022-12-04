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


class Pair:
    def __init__(self, min, max) -> None:
        self.min = int(min)
        self.max = int(max)


class Section:
    def __init__(self, p1: Pair, p2: Pair) -> None:
        self.pairOne = p1
        self.pairTwo = p2

    def pairContainsAnother(self) -> bool:
        pairOneList = set(
            value for value in range(self.pairOne.min, self.pairOne.max + 1)
        )
        pairTwoList = set(
            value for value in range(self.pairTwo.min, self.pairTwo.max + 1)
        )
        conditions = [
            pairOneList.issubset(pairTwoList),
            pairOneList.issuperset(pairTwoList),
        ]
        if any(conditions):
            return True
        return False

    def pairOverlaps(self) -> bool:
        pairOneList = set(
            value for value in range(self.pairOne.min, self.pairOne.max + 1)
        )
        pairTwoList = set(
            value for value in range(self.pairTwo.min, self.pairTwo.max + 1)
        )
        intersection = pairOneList.intersection(pairTwoList)
        if len(intersection) > 0:
            return True
        return False


def readFile(filepath):
    with open(os.path.join(os.path.dirname(__file__), filepath)) as file:
        line = file.readline()
        while line:
            yield line.rstrip("\n")
            line = file.readline()


def solutionOne(fileName: str):
    result = 0
    for line in readFile(f"{fileName}.txt"):
        parts = line.split(",")
        pairOne = Pair(*parts[0].split("-"))
        pairTwo = Pair(*parts[1].split("-"))
        section = Section(pairOne, pairTwo)
        if section.pairContainsAnother():
            result = result + 1
    return result


def solutionTwo(fileName: str):
    result = 0
    for line in readFile(f"{fileName}.txt"):
        parts = line.split(",")
        pairOne = Pair(*parts[0].split("-"))
        pairTwo = Pair(*parts[1].split("-"))
        section = Section(pairOne, pairTwo)
        if section.pairOverlaps():
            result = result + 1
    return result


if __name__ == "__main__":
    answer = Answers(2, 4)
    assert solutionOne("test") == answer.partOne
    print("Part One: ", solutionOne("input"))
    assert solutionTwo("test") == answer.partTwo
    print("Part Two: ", solutionTwo("input"))
