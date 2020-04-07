#!/usr/bin/env python3
x = int(input())
n = 10 ** 10
for i in range(x, n):
    for k in range(2, x):
        if i % k == 0:
            break
    else:
        print(i)
        exit()
