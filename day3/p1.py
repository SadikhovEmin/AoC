f = open('input.txt')

contents = []

for i in f:
    p1 = i[:len(i) // 2].strip()
    p2 = i[len(i) // 2:].strip()

    contents.append((p1, p2))

result = 0

for i in contents:
    chars = set()
    for c in i[0]:
        chars.add(c)

    for c in i[1]:
        if c in chars:
            if c.isupper():
               result += ord(c) - 38
            else:
                result += ord(c) - 96
            break

print(result)