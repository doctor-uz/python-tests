import math
import numpy as np
import sys
from random import randint
 
ls = [0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6]
 
e = 0.03
u = 0.75
l = 0.05
n = len(ls)
x = round(n/9)
y = 2
z = 3
last = []
for i in range(y):
    index = randint(0, n-1)
    while index in last :
        index = randint(0, n-1)
    last.append(index)
    del ls[index]
    ls.insert(index, randint(0, 0))
 
#print(ls)
#print(last)
#print('Number of faults', y)
v = sum(ls)/n
#print(v)

sys.stdout = open('ran6.txt', 'w')
for j in range(2000):
    g = 1-(abs(v - 0.6) - e)/(u-l)
    print(g)



data = []
with open(r'ran6.txt') as f:
    for line in f:
        fields = line.split()
        rowdata = map(float, fields)
        data.extend(rowdata)

mean = sum(data)*1.0/len(data)

print('This is mean =', mean)

length =len(data)
m = mean
total_sum = 0
for i in range(length):
    total_sum += (data[i] - m)**2
under_root = total_sum*1.0/(length -1)
print('This is std: ', math.sqrt(under_root))



print('This is variance: ', gnu np.var(data))