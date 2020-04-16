#!/usr/bin/env python3
l = [input() for _ in range(5)]
m = 11
ans = 0
for i in range(len(l)):
    n = int(l[i][-1])
    if n == 0: n = 10
    if n < m:
        m = n
        ind = i
for t in range(len(l)):
    if t == ind:
        ans += int(l[t])
    else:
        n = int(l[t][-1])
        if n == 0: n = 10
        ans += (int(l[t]) + 10 - n)
print(ans)
