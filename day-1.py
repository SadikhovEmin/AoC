import heapq

if __name__ == '__main__':
    f = open('inputs/1_input.txt')

    data = []
    count = 0
    for i in f:
        if i.strip() != "":
            count += int(i)
        else:
            heapq.heappush(data, -count)
            count = 0

    if count != 0:
        heapq.heappush(data, -count)

    res = heapq.heappop(data)
    res += heapq.heappop(data)
    res += heapq.heappop(data)

    print(abs(res))
