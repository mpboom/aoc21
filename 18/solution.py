import json
import collections
import math
import itertools
import copy


def get_deep(data, idx, new_value=None):
    idx = list(idx)
    ptr = data
    while len(idx) - (1 if new_value != None else 0):
        ptr = ptr[idx.pop(0)]
    if new_value != None:
        ptr[idx.pop()] = new_value
    return ptr if new_value is None else None


def build_tree(data):
    tree = collections.OrderedDict()
    stack = [0]
    while stack:
        c = get_deep(data, stack)
        is_pair = type(c) == list and len(c) == 2 and type(c[0]) == int and type(c[1]) == int
        if is_pair or type(c) == int:
            tree[tuple(stack)] = c
        if type(c) == list and not is_pair:
            stack.append(0)
        elif len(get_deep(data, stack[:-1])) > stack[-1] + 1:
            stack[-1] += 1
        else:
            while stack and not len(get_deep(data, stack[:-1])) > stack[-1] + 1:
                stack.pop()
            if stack:
                stack[-1] += 1
    return tree


def add(a, b):

    data = [a, b]
    previous = None
    while True:

        tree = build_tree(data)
        exploded = False

        # Explode
        prev_idx = None
        iterator = iter(tree.items())
        for idx, val in iterator:
            if len(idx) == 4 and type(val) == list:
                exploded = True
                left, right = val
                get_deep(data, idx, new_value=0)
                if prev_idx:
                    if type(prev_idx[1]) == list:
                        prev_idx = (list(prev_idx[0]) + [1], prev_idx[1][1])
                    get_deep(data, prev_idx[0], new_value=prev_idx[1] + left)
                next_item = next(iterator, None)
                if next_item:
                    if type(next_item[1]) == list:
                        next_item = (list(next_item[0]) + [0], next_item[1][0])
                    get_deep(data, next_item[0], new_value=next_item[1] + right)
                break
            prev_idx = (idx, val)

        if exploded:
            continue

        # Split
        for idx, val in tree.items():
            offender = None
            if type(val) == int and val > 9:
                offender = idx
            elif type(val) == list and max(val) > 9:
                offender = list(idx) + [0 if val[0] > 9 else 1]
                val = val[0 if val[0] > 9 else 1]
            if offender:
                get_deep(data, offender, new_value=[math.floor(val / 2), math.ceil(val / 2)])
                break

        if str(data) == previous:
            break
        previous = str(data)

    return data


def magnitude(data):
    previous = None
    while True:
        result_tree = build_tree(data)
        for idx, item in result_tree.items():
            if type(item) != int:
                get_deep(data, idx, new_value=3 * item[0] + 2 * item[1])
        if str(data) == previous:
            break
        previous = str(data)
    result_tree = build_tree(data)
    return 3 * data[0] + 2 * data[1]


with open('input.txt') as fp:
    raw_data = [json.loads(x) for x in fp.read().split('\n') if len(x) > 2]

# Part I
data = copy.deepcopy(raw_data)
result = data.pop(0)
while data:
    result = add(result, data.pop(0))
print(magnitude(result))

# Part II
max_magnitude = 0
for a, b in itertools.product(raw_data, raw_data):
    max_magnitude = max(
        magnitude(add(copy.deepcopy(a), copy.deepcopy(b))),
        magnitude(add(copy.deepcopy(b), copy.deepcopy(a))),
        max_magnitude
    )
print(max_magnitude)
