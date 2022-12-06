f = open('input.txt')

for i in f:
    print(i.strip())
    chars = set()
    count = 0
    l = 0
    for j in range(len(i)):
        if count == 4:
            print(j)
            break
        while i[j] in chars:
            chars.remove(i[l])
            count -= 1
            l += 1
        count += 1
        chars.add(i[j])