import numpy
import statistics
import matplotlib.pyplot as plt
import numpy as np
from itertools import chain
from statistics import mean

x = []
y = []

with open('ran6.txt') as infile:
    for line in infile:
        # if line.split()[0] == '1':
        fields_x = line.split()[0]
        x.append(float(fields_x))
        fields_y = line.split()[1]
        y.append(float(fields_y))

x = [round(l) for l in x]
x = list(set(x))
x = np.array(x)

print(x)

y1 = y[:2000]
e1 = statistics.stdev(y1)
y1 = statistics.mean(y1)
print(e1)
print(y1)

y2 = y[2000:4000]
e2 = statistics.stdev(y2)
y2 = statistics.mean(y2)
print(e2)
print(y2)


y3 = y[4000:6000]
e3 = statistics.stdev(y3)
y3 = statistics.mean(y3)
print(e3)
print(y3)


y4 = y[6000:8000]
e4 = statistics.stdev(y4)
y4 = statistics.mean(y4)
print(e4)
print(y4)


y5 = y[8000:10000]
e5 = statistics.stdev(y5)
y5 = statistics.mean(y5)
print(e5)
print(y5)


y6 = y[10000:12000]
e6 = statistics.stdev(y6)
y6 = statistics.mean(y6)
print(e6)
print(y6)


y7 = y[12000:14000]
e7 = statistics.stdev(y7)
y7 = statistics.mean(y7)
print(e7)
print(y7)


y8 = y[14000:16000]
e8 = statistics.stdev(y8)
y8 = statistics.mean(y8)
print(e8)
print(y8)


y9 = y[16000:18000]
e9 = statistics.stdev(y9)
y9 = statistics.mean(y9)
print(e9)
print(y9)


y = np.array([y1, y2, y3, y4, y5, y6, y7, y8, y8])
e = np.array([e1, e2, e3, e4, e5, e6, e7, e8, e8])
x = np.array(x)

# n = 5
# y = np.mean(np.array(y).reshape(-1, n), axis=1)
# print(y)


fig = plt.figure()
plt.errorbar(x, y, e, linestyle='None', marker='o')
plt.show()

fig.savefig('temp2.pdf', dpi=fig.dpi)



