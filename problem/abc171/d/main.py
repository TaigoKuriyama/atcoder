#!/usr/bin/env python3
from collections import Counter
N = int(input())
A = list(map(int, input().split()))
d = Counter(A)
Q = int(input())
ans = sum(A)
for i in range(Q):
    b, c = map(int, input().split())
    ans += (c-b) * d[b]
    d[c] += d[b]
    d[b] = 0
    print(ans)