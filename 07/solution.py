with open('input.txt') as fp:
    d = [int(x) for x in fp.read().split('\n')[0].split(',')]

# Part I
print(min([sum(abs(x - y) for y in d) for x in set(d)]))

# Part II
print(min([sum(sum(range(abs(x - y) + 1)) for y in d) for x in range(min(d), max(d) + 1)]))
