#!/usr/bin/env python3
a, b, x = map(int, input().split())
l = 0
r = 10**9+1
while(r - l > 1):
    c = (r + l) // 2
    if a * c + b * len(str(c)) > x:
        r = c
    else:
        l = c
print(l)