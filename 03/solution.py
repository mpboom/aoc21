with open('input.txt') as fp:
    lines = [x for x in fp.read().split('\n') if len(x) > 2]

# Part I
parsed = ''.join([
    str(int(len([y[x] for y in lines if y[x] == '1']) >= len(lines) / 2)) \
    for x in range(len(lines[0]))
])
gamma = int(parsed, 2)
epsilon = int(''.join(['1' if x == '0' else '0' for x in parsed]), 2)
print(gamma * epsilon)

# Part II
oxygen = lines
co2 = lines
for bit in range(len(lines[0])):
    most_common = str(int(len([x[bit] for x in oxygen if x[bit] == '1']) >= len(oxygen) / 2))
    oxygen = [x for x in oxygen if x[bit] == most_common or len(oxygen) == 1]
    least_common = str(int(len([x[bit] for x in co2 if x[bit] == '1']) < len(co2) / 2))
    co2 = [x for x in co2 if x[bit] == least_common or len(co2) == 1]
print(int(co2[0], 2) * int(oxygen[0], 2))
