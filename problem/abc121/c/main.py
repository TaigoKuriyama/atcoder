#!/usr/bin/env python3
n, m = map(int, input().split())
a = [0] * n
b = [0] * n
s = 0
ans = 0
for i in range(n): a[i], b[i] = map(int, input().split())
D = sorted(dict(zip(a, b)).items(), key=lambda x: x)
for d in D:
    s += d[1]
    if s >= m:
        ans += d[0] * (m - (s - d[1]))
        print(ans)
        exit()
    else:
        ans += d[0] * d[1]
