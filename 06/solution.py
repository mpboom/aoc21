def get_fish(fish, days):
    for _ in range(days):
        fish = {k: fish[k + 1 if k != 8 else 0] + (fish[0] if k == 6 else 0) \
            for k in sorted(fish.keys(), reverse=True)}
    return sum(fish.values())


with open('input.txt') as fp:
    data = [int(x) for x in fp.read().split('\n')[0].split(',')]
    fish = {x: sum(1 for y in data if y == x) for x in range(0, 9)}

# Part I
print(get_fish(fish, 80))

# Part II
print(get_fish(fish, 256))
