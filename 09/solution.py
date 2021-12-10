import math
import itertools


def get_neighbors(mapping, x, y, exclude=None):
    return [z for z in [
        (mapping[x - 1][y], x - 1, y) if x - 1 >= 0 else None,
        (mapping[x + 1][y], x + 1, y) if x + 1 < len(mapping) else None,
        (mapping[x][y - 1], x, y - 1) if y - 1 >= 0 else None,
        (mapping[x][y + 1], x, y + 1) if y + 1 < len(mapping[0]) else None,
    ] if z != None and z[0] != exclude and mapping[x][y] != exclude]


with open('input.txt') as fp:
    mapping = [list(map(lambda n: int(n), x)) for x in fp.read().split('\n') if len(x) > 2]

# Part I
indexes = list(itertools.product(range(len(mapping)), range(len(mapping[0]))))
print(sum(
    mapping[x][y] + 1 for x, y in indexes \
    if min(map(lambda n: n[0], get_neighbors(mapping, x, y))) > mapping[x][y]
))

# Part II
pairs, basins = [], []
for x, y in indexes:
    pairs.extend([((x, y), (n[1], n[2])) for n in get_neighbors(mapping, x, y, exclude=9)])
for me, nb in pairs:
    updated = len([(b.add(me), b.add(nb)) for b in basins if nb in b or me in b])
    if not updated:
        basins.append(set([me, nb]))
    elif updated > 1:
        basins = [set().union(*[b for b in basins if nb in b or me in b])] + \
                    [b for b in basins if not (nb in b or me in b)]
print(math.prod(sorted(list(map(lambda n: len(n), basins)), reverse=True)[0:3]))
