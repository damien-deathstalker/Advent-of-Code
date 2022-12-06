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

from itertools import islice

def window(seq, n=4):
    "Returns a sliding window (of width n) over data from the iterable"
    "   s -> (s0,s1,...s[n-1]), (s1,s2,...,sn), ...                   "
    it = iter(seq)
    result = tuple(islice(it, n))
    if len(result) == n:
        yield result
    for elem in it:
        result = result[1:] + (elem,)
        yield result


def readFile(filepath):
    with open(os.path.join(os.path.dirname(__file__), filepath)) as file:
        line = file.readline()
        while line:
            yield line.rstrip("\n")
            line = file.readline()


def solutionOne(fileName: str):
    result = 0
    number_of_characters = 4
    for line in readFile(f"{fileName}.txt"):
        for index, chars in enumerate(window(line, number_of_characters)):
            charset = set(chars)
            if len(charset) == len(chars):
                result = index+number_of_characters
                break
    return result


def solutionTwo(fileName: str):
    result = 0
    number_of_characters = 14
    for line in readFile(f"{fileName}.txt"):
        for index, chars in enumerate(window(line, number_of_characters)):
            charset = set(chars)
            if len(charset) == len(chars):
                result = index+number_of_characters
                break
    return result


if __name__ == "__main__":
    answer = Answers(5, 23)
    assert solutionOne("test") == answer.partOne
    print("Part One: ", solutionOne("input"))
    assert solutionTwo("test") == answer.partTwo
    print("Part Two: ", solutionTwo("input"))
