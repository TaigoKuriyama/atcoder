#!/usr/bin/env python3
a, b, k = map(int, input().split())
if a > k:
    a = a - k
else:
    tmp = a
    a = 0
    if b < k - tmp:
        b = 0
    else:
        b = b - (k - tmp)
print(a, b)
