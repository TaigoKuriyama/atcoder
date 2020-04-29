#!/usr/bin/env python3
a, b = map(int, input().split())
print(a + b) if b % a == 0 else print(b - a)