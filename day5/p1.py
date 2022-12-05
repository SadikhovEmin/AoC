stacks = [
    ["B", "Z", "T"],
    ["V", "H", "T", "D", "N"],
    ["B", "F", "M", "D"],
    ["T", "J", "G", "W", "V", "Q", "L"],
    ["W", "D", "G", "P", "V", "F", "Q", "M"],
    ["V", "Z", "Q", "G", "H", "F", "S"],
    ["Z", "S", "N", "R", "L", "T", "C", "W"],
    ["Z", "H", "W", "D", "J", "N", "R", "M"],
    ["M", "Q", "L", "F", "D", "S"]
]

f = open("input.txt")
operations = []
change = False

for i in f:
    if i.strip() == '':
        change = True

    if change:
        operation = i.strip().lstrip("move ").split()
        operations.append(operation)

operations.pop(0)
ops = [[int(i[0]), int(i[2]), int(i[4])] for i in operations]
print(ops)

for i in ops:
    # to_append = stacks[i[1] - 1][:i[0]]
    for j in range(i[0]):
        poping = stacks[i[1] - 1].pop()
        stacks[i[2] - 1].append(poping)


res = []

for i in stacks:
    res.append(i[-1])

print("".join(res))

print(stacks)