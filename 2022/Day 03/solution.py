import string


def readFile(filepath):
    with open(filepath) as file:
        line = file.readline()
        while line:
            yield line.rstrip("\n")
            line = file.readline()


priorities = {
    letter: value
    for letter, value in zip(
        string.ascii_lowercase + string.ascii_uppercase,
        [number for number in range(1, 53)],
    )
}


def solutionOne(fileName: str):
    result = 0
    for line in readFile(f"{fileName}.txt"):
        halfLength = len(line) // 2
        commonItem = list(set(line[:halfLength]).intersection(set(line[halfLength:])))
        assert len(commonItem) == 1
        result = result + priorities[commonItem.pop()]
    return result


def solutionTwo(fileName: str):
    result = 0
    arrayOfThrees: list = []
    for line in readFile(f"{fileName}.txt"):
        if len(arrayOfThrees) != 3:
            arrayOfThrees.append(line)
        if len(arrayOfThrees) == 3:
            groupCommonItem = set.intersection(*map(set, arrayOfThrees))
            badge = list(groupCommonItem)[0]
            result = result + priorities[badge]
            arrayOfThrees = []
    return result


if __name__ == "__main__":
    assert solutionOne("test") == 157
    print(solutionOne("test"))
    assert solutionTwo("test") == 70
    print(solutionTwo("input"))
