#!/usr/bin/env python3
k, n = map(int, input().split())
a = list(map(int, input().split()))
l = []
for i in range(n-1):
    l.append(a[i+1] - a[i])
l.append(k-a[-1]+a[0])
print(k-max(l))