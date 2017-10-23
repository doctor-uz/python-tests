import numpy
import statistics
import matplotlib.pyplot as plt
import numpy as np

rowdata = []

with open('ran6.txt') as infile:
    for line in infile:
        #if line.split()[0] == '1':
        fields = line.split()[1]
        rowdata.append(float(fields))
                
print(statistics.mean(rowdata), statistics.stdev(rowdata))

x = 8
y = statistics.mean(rowdata)
e = statistics.stdev(rowdata)

                
print(statistics.mean(rowdata), statistics.stdev(rowdata))


##y = np.power(x, 2) # Effectively y = x**2
##e = np.array([1.5, 2.6, 3.7, 4.6, 5.5])
##x = np.array([1, 2, 3, 4, 5])


fig = plt.figure()
plt.errorbar(x, y, e, linestyle='None', marker='^')

plt.show()

fig.savefig('temp.pdf', dpi=fig.dpi)



