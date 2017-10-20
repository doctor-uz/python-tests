# # data = []
# # with open(r'test.txt') as f:
# #     for line in f:
# #         fields = line.split()
# #         rowdata = map(float, fields)
# #         data.extend(rowdata)
#
# #mean = sum(data)*1.0/len(data)
#
# #print('This is mean =', mean)
# #print(data)
# from math import log
# data = []
# with open('test.txt') as infile:
#     for line in infile:
#         fields = line.split()[1]
#         rowdata = map(float, fields)
#         data.extend(rowdata)
# #
# mean = sum(data) * 1.0 / len(data)
#
#
#
#        # print(line.split()[1])
#





import numpy
import statistics
import matplotlib.pyplot as plt
import numpy as np

data = []
rowdata = []
temp_sum = 0
counter = 0

with open('test.txt') as infile:
    for line in infile:
        # if line.split()[0] == '2':
        fields = line.split()[1]
        rowdata.append(float(fields))

        # temp_sum = temp_sum + rowdata
        # counter = counter + 1
        # rowdata = map(float, fields)
        # data.extend(rowdata)
        # print(rowdata)
#
# mean = sum(rowdata) * 1.0 / len(rowdata)
# print(temp_sum/counter)
print(statistics.mean(rowdata), statistics.stdev(rowdata))
# for i in len(rowdata):
#     print(rowdata[i])
# print(rowdata)

# print(line.split()[1])





y = statistics.mean(rowdata)
e = statistics.stdev(rowdata)
x = 8


fig = plt.figure()
plt.errorbar(x, y, e, linestyle='None', marker='^')

plt.show()

fig.savefig('temp.pdf', dpi=fig.dpi)

       # print(line.split()[1])

