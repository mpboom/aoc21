with open('input.txt') as fp:
    lines = [x for x in fp.read().split('\n') if len(x) > 2]
    data = [tuple(line.split(' | ')) for line in lines]
    data = [([set(a) for a in x.split(' ')], [set(b) for b in y.split(' ')]) for x, y in data]

# Part I
print(sum(sum(1 for y in x if len(y) in [2, 4, 7, 3]) for _, x in data))

# Part II
result = 0
for input, output in data:
    input = sorted(input, key=lambda n: len(n)) 
    key = {
        1: input[0],
        4: input[2],
        7: input[1],
        8: input[9],
    }
    key[3] = next(x for x in input[3:6] if key[1].issubset(x))
    key[5] = next(x for x in input[3:6] if list(key[4] - key[3])[0] in x)
    key[2] = next(x for x in input[3:6] if x not in [key[5], key[3]])
    key[6] = next(x for x in input[6:9] if not key[1].issubset(x))
    key[9] = next(x for x in input[6:9] if key[5].issubset(x) and x != key[6])
    key[0] = next(x for x in input[6:9] if x not in [key[9], key[6]])
    reverse_key = {frozenset(v): k for k, v in key.items()}
    result += int(''.join([str(reverse_key[frozenset(digit)]) for digit in output]))
print(result)
