#!/usr/bin/env python3
n = int(input())
l = []
for i in range(1, 10):
    x = int(str(i) + str(i) + str(i))
    if x >= n:
        print(x)
        exit()