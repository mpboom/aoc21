import collections
import itertools


def get_points(points):
    point_count = collections.defaultdict(int)
    for point in points:
        point_count[point] += 1
    return sum(1 for x in point_count.values() if x > 1)


with open('input.txt') as fp:
    lines = [sorted((
        tuple(int(y) for y in x.split(' -> ')[0].split(',')),
        tuple(int(y) for y in x.split(' -> ')[1].split(','))
    )) for x in fp.read().strip().split('\n')]

# Part I
points = list(itertools.chain(*[list(itertools.product(
    range(a[0], b[0] + 1) or [a[0]], range(a[1], b[1] + 1) or [a[1]])
) for a, b in lines if a[0] == b[0] or a[1] == b[1]]))
print(get_points(points))

# Part II
points = points + list(itertools.chain(*[
    [x for x in zip(range(a[0], b[0] + 1), range(a[1], b[1] + 1))] if \
    b[0] > a[0] and b[1] > a[1] else \
    [x for x in zip(range(a[0], b[0] + 1), reversed(range(b[1], a[1] + 1)))] \
    for a, b in lines if a[0] != b[0] and a[1] != b[1]
]))
print(get_points(points))
