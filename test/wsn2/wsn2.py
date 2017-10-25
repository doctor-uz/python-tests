import math
import numpy as np
import sys
from random import randint
 
ls1 = [0.6, 0.6, 0.6, 0.6] #4 nodes
ls2 = [0.6, 0.6, 0.6, 0.6, 0.6] #5 nodes
 
e = 0.03
u = 0.75
l = 0.05
n = len(ls)
x = round(n/9)
y = 2
z = 3
a = 4
b = 5
c = 6
d = 7
q = 8

#No faults
sys.stdout = open('wsn2.txt', 'w')
for h in range(2000):
    print(0, 1.0)


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
with open("wsn2.txt", "a") as f:
    for j in range(2000):
        g = 1-(abs(v - 0.6) - e)/(u-l)
        print(x, g)


#Simulatin of faults replacing to 0: 2 fault
last=[]
ls2 = [0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6]
for iiiiiii in range(y):
    index = randint(0, n-1)
    while index in last :
        index = randint(0, n-1)
    last.append(index)
    del ls2[index]
    ls2.insert(index, randint(0, 0))
v = sum(ls2)/n
with open("wsn2.txt", "a") as f:
    for j in range(2000):
        g2 = 1-(abs(v - 0.6) - e)/(u-l)
        print(y, g2)

#Simulatin of faults replacing to 0: 3 fault
last=[]
ls3 = [0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6]
for iiiiiiii in range(z):
    index = randint(0, n-1)
    while index in last :
        index = randint(0, n-1)
    last.append(index)
    del ls3[index]
    ls3.insert(index, randint(0, 0))
v = sum(ls3)/n
with open("wsn2.txt", "a") as f:
    for j in range(2000):
        g3 = 1-(abs(v - 0.6) - e)/(u-l)
        print(z, g3)


#Simulatin of faults replacing to 0: 4 fault
last=[]
ls4 = [0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6]
for ii in range(a):
    index = randint(0, n-1)
    while index in last :
        index = randint(0, n-1)
    last.append(index)
    del ls4[index]
    ls4.insert(index, randint(0, 0))
v = sum(ls4)/n
with open("wsn2.txt", "a") as f:
    for j in range(2000):
        g4 = 1-(abs(v - 0.6) - e)/(u-l)
        print(a, g4)


#Simulatin of faults replacing to 0: 5 fault
last=[]
ls5 = [0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6]
for iii in range(b):
    index = randint(0, n-1)
    while index in last :
        index = randint(0, n-1)
    last.append(index)
    del ls5[index]
    ls5.insert(index, randint(0, 0))
v = sum(ls5)/n
with open("wsn2.txt", "a") as f:
    for j in range(2000):
        g5 = 1-(abs(v - 0.6) - e)/(u-l)
        print(b, g5)


#Simulatin of faults replacing to 0: 6 fault
last=[]
ls6 = [0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6]
for iiii in range(c):
    index = randint(0, n-1)
    while index in last :
        index = randint(0, n-1)
    last.append(index)
    del ls6[index]
    ls6.insert(index, randint(0, 0))
v = sum(ls6)/n
with open("wsn2.txt", "a") as f:
    for j in range(2000):
        g6 = 1-(abs(v - 0.6) - e)/(u-l)
        print(c, g6)


#Simulatin of faults replacing to 0: 7 fault
last=[]
ls7 = [0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6]
for iiii in range(d):
    index = randint(0, n-1)
    while index in last :
        index = randint(0, n-1)
    last.append(index)
    del ls7[index]
    ls7.insert(index, randint(0, 0))
v = sum(ls7)/n
with open("wsn2.txt", "a") as f:
    for j in range(2000):
        g7 = 1-(abs(v - 0.6) - e)/(u-l)
        print(d, g7)


#Simulatin of faults replacing to 0: 8 fault
last=[]
ls8 = [0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6]
for iiiii in range(q):
    index = randint(0, n-1)
    while index in last :
        index = randint(0, n-1)
    last.append(index)
    del ls8[index]
    ls8.insert(index, randint(0, 0))
v = sum(ls8)/n
with open("wsn2.txt", "a") as f:
    for j in range(2000):
        g8 = 1-(abs(v - 0.6) - e)/(u-l)
        print(q, g8)


# 1 fault: mean; std; variance
# 2 fault: mean; std; variance
# ...
# ...



#
#reading txt file in order to calculate mean, std and variance
# data = []
# with open(r'ran6.txt') as f:
#     for line in f:
#         fields = line.split()
#         rowdata = map(float, fields)
#         data.extend(rowdata)
#
# mean = sum(data)*1.0/len(data)
#
# print('This is mean =', mean)
#
# length =len(data)
# m = mean
# total_sum = 0
# for i in range(length):
#     total_sum += (data[i] - m)**2
# under_root = total_sum*1.0/(length -1)
# print('This is std: ', math.sqrt(under_root))


#print('This is variance: ', gnu(np.var(data))