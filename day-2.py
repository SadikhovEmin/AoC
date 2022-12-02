shapes = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

f = open("inputs/2.txt")

games = []
for i in f:
    games.append(i.strip().split(" "))

points = 0

'''
0 -> Lost
3 -> Draw
6 -> Win
'''

for i in games:
    if i[0] == "A" and i[1] == "X":
        points += 3
    elif i[0] == "A" and i[1] == "Y":
        points += 6
    elif i[0] == "A" and i[1] == "Z":
        points += 0
    elif i[0] == "B" and i[1] == "X":
        points += 0
    elif i[0] == "B" and i[1] == "Y":
        points += 3
    elif i[0] == "B" and i[1] == "Z":
        points += 6
    elif i[0] == "C" and i[1] == "X":
        points += 6
    elif i[0] == "C" and i[1] == "Y":
        points += 0
    elif i[0] == "C" and i[1] == "Z":
        points += 3
    points += shapes[i[1]]

print(points)