#!/usr/bin/env python3
n, m = map(int, input().split())
h = list(map(int, input().split()))
ans = []
for _ in range(m):
    a, b = map(int, input().split())
    if h[a-1] > h[b-1]:
        ans.append(b-1)
    elif h[a-1] < h[b-1]:
        ans.append(a-1)
    else:
        ans.append(a-1)
        ans.append(b-1)
print(n - len(set(ans)))