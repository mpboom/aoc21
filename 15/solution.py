import itertools


def shortest_path(data):
    unvisited = set(itertools.product(range(len(data)), range(len(data[0]))))
    distances = {node: None if node != (0, 0) else 0 for node in unvisited}
    c = (0, 0)
    i = 0 #
    while True:
        print(i) #
        i += 1 #
        if c == (len(data) - 1, len(data[0]) - 1):
            return distances[c]
        unvisited.remove(c)
        distances.update({
            n: data[n[1]][n[0]] + distances[c]
            for n in [(c[0], c[1] + 1), (c[0] + 1, c[1]), (c[0] - 1, c[1]), (c[0], c[1] - 1)]
            if n in unvisited \
                and ((distances[n] is None) or (distances[n] > data[n[1]][n[0]] + distances[c]))
        })
        reversed_distances = {v: k for k, v in distances.items() if v and k in unvisited}
        c = reversed_distances[min(reversed_distances.keys())]



with open('input.txt') as fp:
    data = [[int(y) for y in x] for x in fp.read().split('\n') if len(x) > 2]

# Part I
print(shortest_path(data))

# Part II (slow)
for row in range(len(data)):
    data[row] = list(itertools.chain(
        *[list(map(lambda n: n + i if n + i < 10 else n + i - 9, data[row])) for i in range(5)]
    ))
height = len(data)
for i in range(1, 5):
    for row in data[:height]:
        data.append(list(map(lambda n: n + i if n + i < 10 else n + i - 9, row)))
print(shortest_path(data))
