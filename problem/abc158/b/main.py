#!/usr/bin/env python3
n, a, b = map(int, input().split())
x = n // (a + b)
r = n % (a + b)
print(a * x + r) if r < a else print((a * (x + 1)))
