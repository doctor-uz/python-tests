from random import randint

ls = [0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6]
n = len(ls)

x = round(n/9)


  
# for i in range(x):
#     index = randint(0, n)
#     del ls[index]
#     ls.insert(index, randint(0, 0))
#
# g = (ls[0]+ls[1]+ls[2]+ls[3]+ls[4]+ls[5]+ls[6]+ls[7]+ls[8])/9
#
# print(g)

for i in range(x):
    index = randint(0, n)
    del ls[index]
    ls.insert(index, randint(0, 0))

    print(ls)


    
