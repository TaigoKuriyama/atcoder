#!/usr/bin/env python3
a, b = map(int, input().split())
print(a + b) if a == b else print(max(a, b) * 2 - 1)