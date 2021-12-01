def get_larger(measurements):
    return sum(1 for i, x in enumerate(measurements) if x > measurements[i - 1] and i > 0)


with open('input.txt') as fp:
    measurements = [int(x) for x in fp.read().split('\n') if len(x) > 1]

# Part I
larger = get_larger(measurements)
print(larger)

# Part II
WINDOW_SIZE = 3
buckets = [measurements[i:i + WINDOW_SIZE] for i in range(len(measurements) - 1)]
larger = get_larger([sum(bucket) for bucket in buckets if len(bucket) == WINDOW_SIZE])
print(larger)
