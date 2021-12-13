def fold(dots, across_x, at):
    d = filter(lambda d: (across_x and d[0] > at) or (not across_x and d[1] > at), frozenset(dots))
    for x, y in d:
        dots.add(
            (list(reversed(range(2 * at + 1))).index(x), y) if across_x else
            (x, list(reversed(range(2 * at + 1))).index(y))
        )
        dots.remove((x, y))
    return dots


with open('input.txt') as fp:
    dots, folds = fp.read().split('\n\n')
    dots = {k for k in [(int(d.split(',')[0]), int(d.split(',')[1])) for d in dots.split('\n')]}
    folds = [('x' in f, int(f.split('=')[1])) for f in folds.split('\n') if len(f) > 2]

# Part I
print(len(fold(dots.copy(), *folds[0])))

# Part II
for across_x, at in folds:
    fold(dots, across_x, at)
print('\n'.join([
    ''.join(['#' if (x, y) in dots else ' ' for x in range(max(xx for xx, _ in dots) + 1)])
    for y in range(max(yy for _, yy in dots) + 1)
]))
