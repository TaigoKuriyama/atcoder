#!/usr/bin/env python3
N, T = map(int, input().split())
c = [0] * N
t = [0] * N
for i in range(N): c[i], t[i] = map(int, input().split())
idx = []
ans = 1000
for i in t:
    if i <= T:
        idx.append(t.index(i))
if len(idx) == 0:
    print("TLE")
    exit()
else:
    for i in idx:
        if ans > c[i]:
            ans = c[i]
print(ans)