def count_routes(second_visit=False):
    result = 0
    known_paths = [['start']]
    while len(known_paths):
        new_known_paths = []
        for path in known_paths:
            destinations = [y for x, y in routes if x == path[-1] and y != 'start']
            result += 1 if 'end' in destinations else 0
            new_known_paths = new_known_paths + [
                path + [dst] for dst in destinations
                if dst != 'end' and (dst.isupper() or dst not in path or (
                    second_visit and
                    len(list(filter(lambda n: n.islower(), path))) == 
                    len(set(filter(lambda n: n.islower(), path)))
                ))
            ]
        known_paths = new_known_paths
    return result


with open('input.txt') as fp:
    routes = [tuple(x.split('-')) for x in fp.read().split('\n') if len(x) > 2]
    routes = set(routes + [tuple(reversed(x)) for x in routes])

# Part I
print(count_routes())

# Part II
print(count_routes(second_visit=True))
