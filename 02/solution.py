with open('input.txt') as fp:
    data = fp.read().replace('forward', 'h').replace('down', 'd').replace('up ', 'd -')
    commands = [(int(x.split(' ')[1]), x.split(' ')[0]) for x in data.split('\n') if len(x) > 1]

# Part I
horizontal = sum(amount for amount, operation in commands if operation == 'h')
depth = sum(amount for amount, operation in commands if operation == 'd')
print(horizontal * depth)

# Part II
aim = 0
depth = 0
for amount, operation in commands:
    if operation == 'd':
        aim += amount
    else:
        depth += aim * amount
print(horizontal * depth)
