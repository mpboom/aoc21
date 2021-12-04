import itertools


with open('input.txt') as fp:
    raw_drawn, raw_boards = fp.read().split('\n', 1)
    parsed_boards = raw_boards.strip().replace('  ', ' 0').replace('\n ', '\n0').split('\n\n')
    drawn = [x.zfill(2) for x in raw_drawn.split(',')]
    boards = [
        list(map(lambda s: s.split(' '), x.strip().split('\n'))) for x in parsed_boards
    ]

# Part I
scores = {}
for board in boards:
    bingos = board + [[row[col] for row in board] for col in range(len(board[0]))]
    score = min([drawn.index(sorted(bingo, key=lambda n: drawn.index(n))[-1]) for bingo in bingos])
    unmarked = sum([int(x) for x in set(itertools.chain(*board)) - set(drawn[0:score + 1])])
    scores[score] = unmarked * int(drawn[score])
print(scores[min(scores.keys())])

# Part II
print(scores[max(scores.keys())])
