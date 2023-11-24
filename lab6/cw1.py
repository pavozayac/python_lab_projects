from itertools import groupby

def plateau(terrain):
    if len(terrain) == 0:
        return 0

    plateaus = groupby(terrain)
    
    lengths = map(lambda x: len(list(x[1])), plateaus)

    return max(lengths)

print(plateau([1,1,1,2,2,2,2,1,1,3,4,5,5,5]))
print(plateau([1,2,3,2,5]))
print(plateau([]))