#!/usr/bin/env python3
n, k = map(int, input().split())
ans = []
for _ in range(k):
    d = int(input())
    a = list(map(int, input().split()))
    ans.extend(a)
print(n - len(set(ans)))