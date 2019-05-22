#!/usr/bin/python3


w = [1,2,3,4,5,6,7,8,9,10]
e = [1,2,3,4,5,6,7,8,9]

def a(olist, nlist):
    for i in olist:
        for j in nlist:
            if i == j:
                break
        else:
            yield i

for i in a(w, e):
    print('执行for')
    print('打印i',i)
