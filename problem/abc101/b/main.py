#!/usr/bin/env python3
n = input()
s = 0
for i in n:
    s += int(i)
print("Yes") if int(n) % s == 0 else print("No")