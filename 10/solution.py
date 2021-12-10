import functools


CLOSE = ']})>'
OPEN = '[{(<'
POINTS = {')': (3, 1), ']': (57, 2), '}': (1197, 3), '>': (25137, 4)}


def analyze_line(line):
    stack = []
    for char in line:
        if char in OPEN:
            stack.append(char)
        elif char in CLOSE and not stack.pop() == OPEN[CLOSE.index(char)]:
            return True, char
    return False, ''.join(reversed([CLOSE[OPEN.index(c)] for c in stack]))


with open('input.txt') as fp:
    lines = [x for x in fp.read().split('\n') if len(x) > 2]

# Part I
results = [analyze_line(line) for line in lines]
print(sum(POINTS[char][0] for corrupt, char in results if corrupt))

# Part II
scores = [functools.reduce(lambda a, b: 5 * a + POINTS[b][1], chars, 0) \
            for chars in [chars for corrupt, chars in results if not corrupt]]
print(sorted(scores)[len(scores) // 2])
