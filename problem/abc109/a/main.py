#!/usr/bin/env python3
a, b = map(int, input().split())
print("No") if a * b % 2 == 0 else print("Yes")