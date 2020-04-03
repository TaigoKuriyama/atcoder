#!/usr/bin/env python3
n, m = map(int, input().split())
ac = 0
wa = 0
tmp = {}
d = set()
for _ in range(m):
    p, s = map(str, input().split())
    if p not in tmp:
        tmp[p] = 0
    if p not in d and s == "AC":
        d.add(p)
        ac += 1
        if p in tmp:
            wa += tmp[p]
    if p not in d and s == "WA":
        tmp[p] += 1
print(ac, wa)
