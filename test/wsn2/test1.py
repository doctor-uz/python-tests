import math
import numpy as np
import sys
import math
import numpy as np
import sys
from random import randint

ls1 = [0.6, 0.6, 0.6, 0.6]  # 4 nodes
ls2 = [0.6, 0.6, 0.6, 0.6, 0.6]  # 5 nodes

e = 0.03
u = 0.75
l = 0.05
n1 = len(ls1)
x1 = round(n1 / 4)
n2 = len(ls2)
x2 = round(n2 / 5)


# No faults
sys.stdout = open('wsn2.txt', 'w')
for h in range(2000):
    print(0, 1.0)

last = []

# Simulatin of faults replacing to 0: 1 fault
for i in range(x):
    index = randint(0, n - 1)
    while index in last:
        index = randint(0, n - 1)
    last.append(index)
    del ls[index]
    ls.insert(index, randint(0, 0))
v = sum(ls) / n
with open("wsn2.txt", "a") as f:
    for j in range(2000):
        g = 1 - (abs(v - 0.6) - e) / (u - l)
        print(x, g)