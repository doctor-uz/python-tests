import math
import numpy as np
import sys
from random import randint

ls = [0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6]

e = 0.03
u = 0.75
l = 0.05
n = len(ls)
x = round(n / 9)
y = 2
z = 3
a = 4
b = 5
c = 6
d = 7
q = 8

last = []

#Simulatin of faults replacing to 0: 1 fault
for i in range(x):
    index = randint(0, n-1)
    while index in last :
        index = randint(0, n-1)
    last.append(index)
    del ls[index]
    ls.insert(index, randint(0, 0))
v = sum(ls)/n
sys.stdout = open('test.txt', 'w')
for j in range(10):
    g = 1-(abs(v - 0.6) - e)/(u-l)
    print(x, g)

