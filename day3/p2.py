f = open('input.txt')

contents = []
group = []
count = 0

for i in f:
    if count == 3:
        contents.append(group)
        group = [i.strip()]
        count = 0
    else:
        group.append(i.strip())
    count += 1

if len(group) > 0:
    contents.append(group)

res = []

for i in range(len(contents)):
    chars = {}

    for j in contents[i][0]:
        for c in j:
            if not c in chars:
                chars[c] = 0

    for j in range(1, len(contents[i])):
        for c in contents[i][j]:
            if not c in chars:
                continue
            if c in chars and chars[c] == j - 1:
                chars[c] = j

    # Print the element
    for j in chars:
        if chars[j] == 2:
            res.append(j)

sol = 0

for i in res:
    if i.isupper():
        sol += ord(i) - 38
    else:
        sol += ord(i) - 96

print(sol)