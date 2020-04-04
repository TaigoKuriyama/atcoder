#!/usr/bin/env python3
n, k = map(int, input().split())
a = n % k
b = abs(k - a)
print(a) if a <= b else print(b)
