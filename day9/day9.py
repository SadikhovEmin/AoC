f = open('input.txt')

head_row, head_col = 0, 0
tail_row, tail_col = -1, 4
visited = set()

directions = {
    "R": (0, 1),
    "L": (0, -1),
    "U": (-1, 0),
    "D": (1, 0)
}

def moveTail(head_row, head_col) -> tuple:
    r, c = (head_row - tail_row), (head_col - tail_col)
    if abs(r) <= 1 and abs(c) <= 1:
        return tail_row, tail_col
    elif abs(r) >= 2 and abs(c) >= 2:
        return head_row - 1 if tail_row < head_row else head_row + 1, head_col - 1 if tail_col < head_col else head_col + 1
    elif abs(r) >= 2:
        return head_row - 1 if tail_row < head_row else head_row + 1, head_col
    elif abs(c) >= 2:
        return head_row, head_col - 1 if tail_col < head_col else head_col + 1

for i in f:
    dirs = i.strip().split()
    for j in range(int(dirs[1])):
        dr, dc = directions[dirs[0]]
        head_row += dr
        head_col += dc

        # tr, tc = moveTail(head_row, head_col)
        tail_row, tail_col = moveTail(head_row, head_col)
        # tail_row += tr
        # tail_col += tc
        visited.add((tail_row, tail_col))

print(len(visited))


if __name__ == '__main__':
    print(moveTail(-3, 4))