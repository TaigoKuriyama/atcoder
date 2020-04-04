#!/usr/bin/env python3
k = int(input())
n = 10 ** 10000
s = 0
for i in range(1, n):
    i = str(i)
    if len(i) == 1:
        s += 1
    if s == k:
        print(i)
        exit()
    for t in range(0, len(i) - 1):
        if abs(int(i[t]) - int(i[t + 1])) > 1:
            break
    else:
        s += 1
        if s == k:
            print(i)
            exit()
