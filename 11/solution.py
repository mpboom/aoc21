import itertools


def get_flashes(grid):
    grid.update({k: v + 1 for k, v in grid.items()})
    flashes = 0
    while n := next(filter(lambda k: grid[k] > 9, grid.keys()), None):
        grid[n] = 0
        flashes += 1
        for neighbor in [
            x for x in itertools.product(range(n[0] - 1, n[0] + 2), range(n[1] - 1, n[1] + 2))
            if x != (n[0], n[1]) and x in grid and grid[x] > 0
        ]:
            grid[neighbor] += 1
    return flashes


with open('input.txt') as fp:
    d = [[int(y) for y in x] for x in fp.read().split('\n') if len(x) > 2]
grid = {(x, y): d[y][x] for y, x in list(itertools.product(range(len(d)), range(len(d[0]))))}

# Part I
print(sum(get_flashes(grid) for _ in range(100)))

# Part II
print(max(itertools.takewhile(lambda n: get_flashes(grid) < len(grid), itertools.count())) + 102)
