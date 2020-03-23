#!/usr/bin/env python3
import math
def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
base = comb(5,3)
m, n = map(int, input().split())
if m > 1 and n > 1:
    ans = comb(n, 2) + comb(m, 2)
elif n > 1:
    ans = comb(n, 2) 
elif m > 1:
    ans = comb(m, 2)
else:
    ans = 0
print(ans)