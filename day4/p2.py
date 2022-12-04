f = open("input.txt")
count = 0

for i in f:
    row = i.strip().split(",")
    elf1 = row[0].split("-")
    elf2 = row[1].split("-")
    elf1 = [int(i) for i in elf1]
    elf2 = [int(i) for i in elf2]

    if (elf1[0] <= elf2[0] <= elf1[1]) or elf1[0] <= elf2[1] <= elf1[1]:
        count += 1
    elif elf2[0] <= elf1[0] <= elf2[1] or elf2[0] <= elf1[1] <= elf2[1]:
        count += 1

print(count)