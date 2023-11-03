import random

i = 0
n = 0
N = 10000000
while i < N:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x*x+y*y<1:
        n = n + 1
    i = i + 1

print(4*n/N)
