import collections


def calculate_polymer(n, polymer, raw_polymer):
    for _ in range(n):
        new_polymer = collections.defaultdict(int)
        for (left, right), value in polymer.items():
            new_polymer[(left, mapping[left + right])] += value
            new_polymer[(mapping[left + right], right)] += value
        polymer = new_polymer
    totals = {
        k: sum(y for (x, _), y in polymer.items() if x == k) + (1 if k == raw_polymer[-1] else 0)
        for k, _ in polymer.keys()
    }
    return max(totals.values()) - min(totals.values())


with open('input.txt') as fp:
    raw_polymer, mapping = fp.read().split('\n\n')
mapping = {x.split(' -> ')[0]: x.split(' -> ')[1] for x in mapping.split('\n') if len(x) > 3}
polymer = {(a, b): 1 for a, b in zip(raw_polymer, raw_polymer[1:len(raw_polymer)])}

# Part I
print(calculate_polymer(10, polymer.copy(), raw_polymer))

# Part II
print(calculate_polymer(40, polymer.copy(), raw_polymer))
