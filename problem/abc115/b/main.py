#!/usr/bin/env python3
n = int(input()) 
p = sorted([int(input()) for _ in range(n)])
print(int(sum(p[:-1]) + p[-1] / 2))