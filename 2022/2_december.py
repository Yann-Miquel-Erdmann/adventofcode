outcome = {
    "A X":4,
    "A Y":8,
    "A Z":3,

    "B X":1,
    "B Y":5,
    "B Z":9,

    "C X":7,
    "C Y":2,
    "C Z":6,
}
lose = {
    "A": "Z",
    "B": "X",
    "C": "Y",
}
draw = {
    "A": "X",
    "B": "Y",
    "C": "Z"
}
win = {
    "A": "Y",
    "B": "Z",
    "C": "X"
}
score = 0

with open("2022/adventofcode.com_2022_day_2_input.txt" , "r") as f:
    for line in f.readlines():
        opp, goal = line.split()
        if goal == "X":
            val = outcome[f"{opp} {lose[opp]}"]
        elif goal == "Y":
            val = outcome[f"{opp} {draw[opp]}"]
        else:
            val = outcome[f"{opp} {win[opp]}"]
            
        score+=val

print(score)