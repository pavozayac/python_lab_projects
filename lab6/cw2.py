from itertools import *
from functools import *

def squares(pairs):
    org, sec = tee(pairs)

    squares = starmap(pow, sec)
    squares = map(partial(repeat, times=1), squares)
    
    zipped = zip(org, squares)

    combined = starmap(chain, zipped)

    return combined

    

combo = squares(iter([(1, 2), (2, 3), (2, 4), (3, 0)]))

for i in combo: print(*i)
