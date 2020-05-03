#!/usr/bin/env python3
a = [int(input()) for _ in range(5)]
b = [-(-x // 10) * 10 - x for x in a]
print(b)
print(sum(b) + sum(a) - max(b))