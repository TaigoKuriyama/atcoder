#!/usr/bin/env python3
import collections
n, m = map(int, input().split())
l = []
ans = 0
for _ in range(n):
    l.extend(list(map(int, input().split()))[1:])
c = collections.Counter(l)
for k in c:
    if c[k] == n: ans += 1
print(ans)