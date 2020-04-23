#!/usr/bin/env python3
n, m = map(int, input().split())
a = [0] * n
b = [0] * n
arr = []
s = 0
ans = 0
for i in range(n):
    a, b = map(int, input().split())
    arr.append((a,  b))
arr.sort()
for d in arr:
    s += d[1]
    if s >= m:
        ans += d[0] * (m - (s - d[1]))
        print(ans)
        exit()
    else:
        ans += d[0] * d[1]
