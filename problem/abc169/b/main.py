#!/usr/bin/env python3
n = int(input()) 
A = list(map(int, input().split()))
b = 1
i = 10**18
A = sorted(A)
for a in A:
  if b > i:
    break
  b *= a
print(-1 if b > i else b)