import json
import collections
import itertools
import copy


def deep_data(data, idx, new_value=None):
    idx = list(idx)
    pointer = data
    while len(idx) - (1 if new_value != None else 0):
        pointer = pointer[idx.pop(0)]
    if new_value != None:
        pointer[idx.pop()] = new_value
    return pointer if new_value is None else None


def build_tree(data):
    tree = collections.OrderedDict()
    stack = [0]
    while stack:
        c = deep_data(data, stack)
        is_pair = type(c) == list and len(c) == 2 and type(c[0]) == int and type(c[1]) == int
        if is_pair or type(c) == int:
            tree[tuple(stack)] = c
        if type(c) == list and not is_pair:
            stack.append(0)
        elif len(deep_data(data, stack[:-1])) > stack[-1] + 1:
            stack[-1] += 1
        else:
            while stack and not len(deep_data(data, stack[:-1])) > stack[-1] + 1:
                stack.pop()
            if stack:
                stack[-1] += 1
    return tree


def add(a, b):
    data = [a, b]
    data_delta = None
    while str(data) != data_delta:
        data_delta = str(data)
        tree = build_tree(data)
        explode_iterator = iter(tree.items())
        previous_item = None
        for idx, val in explode_iterator:  # explode
            if len(idx) == 4 and type(val) == list:
                next_item = next(explode_iterator, None)
                left, right = val
                deep_data(data, idx, new_value=0)
                if previous_item:
                    is_pair = type(previous_item[1]) == list
                    deep_data(
                        data,
                        list(previous_item[0]) + ([1] if is_pair else []),
                        new_value=(previous_item[1] if not is_pair else previous_item[1][1]) + left
                    )
                if next_item:
                    is_pair = type(next_item[1]) == list
                    deep_data(
                        data,
                        list(next_item[0]) + ([0] if is_pair else []),
                        new_value=(next_item[1] if not is_pair else next_item[1][0]) + right
                    )
                break
            previous_item = (idx, val)
        else:  # split
            for idx, val in tree.items():
                offender = idx if type(val) == int and val > 9 else None
                if type(val) == list and max(val) > 9:
                    offender = list(idx) + [0 if val[0] > 9 else 1]
                    val = val[0 if val[0] > 9 else 1]
                if offender:
                    deep_data(data, offender, new_value=[val // 2, -(-val//2)])
                    break
    return data


def magnitude(data):
    while not (len(data) == 2 and type(data[0]) == int and type(data[1]) == int):
        result_tree = build_tree(data)
        for idx, item in result_tree.items():
            if type(item) != int:
                deep_data(data, idx, new_value=3 * item[0] + 2 * item[1])
    return 3 * data[0] + 2 * data[1]


with open('input.txt') as fp:
    raw_data = [json.loads(x) for x in fp.read().split('\n') if len(x) > 2]

# Part I
print(magnitude(
    list(itertools.accumulate(copy.deepcopy(raw_data), lambda a, b: add(a, b) if a else b))[-1]
))

# Part II
print(max(max(
    magnitude(add(copy.deepcopy(a), copy.deepcopy(b))),
    magnitude(add(copy.deepcopy(b), copy.deepcopy(a))),
) for a, b in itertools.product(raw_data, raw_data)))
