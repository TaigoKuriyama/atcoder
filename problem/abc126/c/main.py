#!/usr/bin/env python3
n, k = map(int, input().split())
ans = 0
for p in range(1, n + 1):
    c = 0
    while (True):
        if p >= k:
            ans += (1 / n) * (1 / 2) ** c
            break
        p *= 2
        c += 1
print(ans)
