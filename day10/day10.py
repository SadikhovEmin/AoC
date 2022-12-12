f = open('input.txt')

count = 0
X = 1
cycles = [20, 60, 100, 140, 180, 220]
res = 0
for i in f:
    cmd = i.strip().split()

    if len(cmd) == 1:      # Noop
        count += 1
        if count in cycles:
            res += (count * X)
        continue

    for j in range(2):
        count += 1
        if count in cycles:
            res += (count * X)

    X += int(cmd[1])

print(X)
print(res)


