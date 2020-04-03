#!/usr/bin/env python3
n, k, m = map(int, input().split())
a = list(map(int, input().split()))
if n * m <= sum(a):
    print(0)
else:
    ans = n * m - sum(a)
    print(ans)if ans <= k else print(-1)
