#!/usr/bin/env python3
k = int(input())
a = []
for i in range(1, 10):
    a.append(i)
while True:
    if k <= len(a):
        print(a[k - 1])
        exit()
    k -= len(a)
    old = []
    a, old = old, a
    for x in old:
        for i in range(-1, 2):
            d = x % 10 + i
            if d < 0 or d > 9:
                continue
            nx = x * 10 + d
            a.append(nx)
