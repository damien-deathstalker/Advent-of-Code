
def file_reader(filepath):
    with open(filepath) as file:
        for line in file.readlines():
            yield line

def maximumCalories(fileName:str):
    sums = []
    value = 0
    for line in file_reader(f"{fileName}.txt"):
        if line == "\n":
            if value > 0: sums.append(value)
            value = 0
        else: 
            value = value + int(line.rstrip("\n"))
    else:
        sums.append(value)
    return max(sums)

def maximumCaloriesByTop3(fileName:str):
    sums = []
    value = 0
    with open(f"{fileName}.txt", "r") as file:
        for line in file.readlines():
            if line == "\n":
                if value > 0: sums.append(value)
                value = 0
            else: 
                value = value + int(line.rstrip("\n"))
        else:
            sums.append(value)
    sums.sort(reverse=True)
    return sum(sums[:3])

print(maximumCalories("test"))
print(maximumCaloriesByTop3("test"))
print(maximumCalories("input"))
print(maximumCaloriesByTop3("input"))