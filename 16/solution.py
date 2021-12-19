import math


def eval_packet(packets, idx):
    operation = packets[idx][1]
    arguments = [
        eval_packet(packets, subpacket[4]) if subpacket[1] != 4 else subpacket[3]
        for subpacket in filter(lambda p: p[2] == idx, packets)
    ]
    return {
        0: sum(arguments),
        1: math.prod(arguments),
        2: min(arguments),
        3: max(arguments),
        5: int(arguments[0] > arguments[1]) if len(arguments) == 2 else None,
        6: int(arguments[0] < arguments[1]) if len(arguments) == 2 else None,
        7: int(arguments[0] == arguments[1]) if len(arguments) == 2 else None,
    }[operation]


with open('input.txt') as fp:
    data = list(''.join([bin(int(x, 16))[2:].zfill(4) for x in fp.read().split('\n')[0]]))

packets = []
current = None
parent_stack = []
while len(data):
    if current is None:
        if len(data) < 8:
            break  # padding reached, end of transmission
        parent = parent_stack.pop() if len(parent_stack) else None
        if parent and parent[1] is not None:
            parent_stack.append(parent)  # parent by size, re-add to stack for next packet
        parent = parent[0] if parent else None
        packets.append([
            int(''.join([data.pop(0) for _ in range(3)]), 2),               # [0] version
            int(''.join([data.pop(0) for _ in range(3)]), 2),               # [1] type
            parent,                                                         # [2] parent
            '',                                                             # [3] value
            len(packets),                                                   # [4] index
        ])
        current = len(packets) - 1
    if packets[current][1] == 4:  # literal packet
        if data.pop(0) == '0':  # final group of literal, end of packet
            packets[current][3] = int(
                packets[current][3] + ''.join([data.pop(0) for _ in range(4)]), 2
            )
            current = None
        else:  # not the final group yet
            packets[current][3] = packets[current][3] + ''.join([data.pop(0) for _ in range(4)])
    else:  # operator packet
        in_bits = data.pop(0) == '0'
        if in_bits:  # next 15 bits represent subpacket size
            size = int(''.join([data.pop(0) for _ in range(15)]), 2)
            parent_stack.append((current, len(data) - size))
        else:  # next 11 bits represent subpacket amount
            parent_stack.extend(
                int(''.join([data.pop(0) for _ in range(11)]), 2) * [(current, None)]
            )
        current = None
    while len(parent_stack) and parent_stack[-1][1] and len(data) <= parent_stack[-1][1]:
        parent_stack.pop()

# Part I
print(sum(p[0] for p in packets))

# Part II
print(eval_packet(packets, 0))
