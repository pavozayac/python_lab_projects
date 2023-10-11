import random

sum = 0

rands = [random.randint(0, 10) / random.randint(0, 10) + 1 for _ in range(10)]

for i in rands:
    if i.is_integer():
        sum += i

print(rands)
print(sum)
