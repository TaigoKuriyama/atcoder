#!/usr/bin/env python3
x = int(input())
a = x // 500
x = x - 500 * a
b = x // 5
print(a * 1000 + b * 5)