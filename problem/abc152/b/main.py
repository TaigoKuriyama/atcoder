#!/usr/bin/env python3
a, b = map(int, input().split())
print(str(b) * a) if a > b else print(str(a) * b)
