#!/usr/bin/env python3
a, b, c, k = map(int, input().split())
if a + b <= k:
    print(a - (k - (a + b)))
    exit()
elif a <= k:
    print(a)
else:
    print(k)