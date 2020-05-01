#!/usr/bin/env python3
s = int(input())
l = []
for i in range(2, 1000000):
    l.append(s)
    if s % 2 == 0:
        s = int(s / 2)
    else:
        s = int(3 * s + 1)
    if s in l:
        print(i)
        exit()
    