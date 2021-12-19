import itertools


with open('input.txt') as fp:
    raw = fp.read()
x_t = tuple(int(x) for x in raw.split('x=')[1].split(',')[0].split('..'))
y_t = tuple(int(y) for y in raw.split('y=')[1].split('\n')[0].split('..'))
reach = max(map(lambda v: abs(v), [x for x in x_t + y_t]))

possible = []
for start in list(itertools.product(range(reach), range(-reach, reach))):
    x_v, y_v = start
    x, y = 0, 0
    highest_y = 0
    while True:
        x = x + x_v
        y = y + y_v
        highest_y = max(highest_y, y)
        y_v -= 1
        x_v = x_v - 1 if x_v > 0 else 0 if x_v == 0 else x_v + 1
        if x <= x_t[1] and x >= x_t[0] and y <= y_t[1] and y >= y_t[0]:
            possible.append(highest_y)
            break
        if x_v == 0 and y_v < min(y_t) or x > max(x_t):
            break

# Part I
print(max(possible))

# Part II
print(len(possible))
