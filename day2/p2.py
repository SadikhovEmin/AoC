shapes = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

moves = {
    "X": 0,
    "Y": 3,
    "Z": 6
}

f = open("input.txt")

games = []
for i in f:
    games.append(i.strip().split(" "))

points = 0


def moveToMake(opponentMove, condition):
    if opponentMove == "A" and condition == "X":
        return shapes["Z"]
    elif opponentMove == "A" and condition == "Y":
        return shapes["X"]
    elif opponentMove == "A" and condition == "Z":
        return shapes["Y"]
    elif opponentMove == "B" and condition == "X":
        return shapes["X"]
    elif opponentMove == "B" and condition == "Y":
        return shapes["Y"]
    elif opponentMove == "B" and condition == "Z":
        return shapes["Z"]
    elif opponentMove == "C" and condition == "X":
        return shapes["Y"]
    elif opponentMove == "C" and condition == "Y":
        return shapes["Z"]
    elif opponentMove == "C" and condition == "Z":
        return shapes["X"]


for i in games:
    points += moveToMake(i[0], i[1])
    points += moves[i[1]]

print(points)