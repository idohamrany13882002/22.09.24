# START
# create an empty list, run from 1 to 10 append random choice [1, 4, 9, -2]
# print mean

import statistics
import random

x: list [int] = []
for _ in range (11):
    x.append(random.choice([1, 4, 9, -2]))
print(x)
print(statistics.mean(x))
# END