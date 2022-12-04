def readFile(filepath):
    with open(filepath) as file:
        line = file.readline()
        while line:
            yield line.rstrip("\n")
            line = file.readline()

player = {}
player["X"] = "Rock"
player["Y"] = "Paper"
player["Z"] = "Scissors"

opponent = {}
opponent["A"] = "Rock"
opponent["B"] = "Paper"
opponent["C"] = "Scissors"

scores = {}
scores["X"] = 1
scores["Y"] = 2
scores["Z"] = 3

outcomes = {}
outcomes["lose"] = 0
outcomes["draw"] = 3
outcomes["win"] = 6

round_outcomes = {}
round_outcomes["X"] = "lose"
round_outcomes["Y"] = "draw"
round_outcomes["Z"] = "win"

shapeScores = {}
shapeScores["Rock"] = 1
shapeScores["Paper"] = 2
shapeScores["Scissors"] = 3

def strategy_one(oppenent_choice, player_choice):
    oppenent_choice = opponent[oppenent_choice]
    player_choice = player[player_choice]
    winning_conditions = [
        player_choice == "Rock" and oppenent_choice != "Paper",
        player_choice == "Paper" and oppenent_choice != "Scissors",
        player_choice == "Scissors" and oppenent_choice != "Rock"
    ]
    if oppenent_choice == player_choice: outcome = "draw"
    elif any(winning_conditions): outcome = "win"
    else: outcome = "lose"
    score = outcomes[outcome]+ shapeScores[player_choice]
    return score

def strategy_two(opponent_choice, round_outcome):
    opponent_choice = opponent[opponent_choice]
    round_outcome = round_outcomes[round_outcome] 
    if round_outcome == "draw":
         player_choice = opponent_choice
    elif opponent_choice == "Rock": 
        if round_outcome == "win": player_choice = "Paper"
        elif round_outcome == "lose": player_choice = "Scissors"
    elif opponent_choice == "Paper": 
        if round_outcome == "win": player_choice = "Scissors"
        elif round_outcome == "lose": player_choice = "Rock"
    elif opponent_choice == "Scissors": 
        if round_outcome == "win": player_choice = "Rock"
        elif round_outcome == "lose": player_choice = "Paper"
    score = outcomes[round_outcome] + shapeScores[player_choice]
    return score
        

def setup(strategy, fileName):
    result = 0
    for line in readFile(f"{fileName}.txt"):
        opponent_choice = line[0]
        player_choice = line[-1]
        result = result + strategy(opponent_choice, player_choice)
    return result

if __name__ == "__main__":
    assert setup(strategy_one, "test") == 15
    assert setup(strategy_two, "test") == 12

    # print(setup(strategy_one, "input"))
    # print(setup(strategy_two, "input"))