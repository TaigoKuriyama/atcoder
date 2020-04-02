#!/usr/bin/env python3
n = int(input())
l = list(map(int, input().split()))
ans = 1
min = l[0]
for i in range(1, n):
    if min > l[i]:
        ans += 1
        min = l[i]
print(ans)
