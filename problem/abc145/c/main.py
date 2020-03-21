#!/usr/bin/env python3
import itertools
import math
n = int(input())
x = [0] * n
y = [0] * n
l = list(range(n))
ans = 0
for i in range(n):
    x[i], y[i] = map(int, input().split())
for v in itertools.permutations(l, 2):
    ans += math.sqrt((x[v[0]] - x[v[1]])**2 + (y[v[0]] - y[v[1]])**2)
print(ans/n)