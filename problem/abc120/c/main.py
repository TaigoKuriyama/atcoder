#!/usr/bin/env python3
s = input()
n = len(s)
n_0 = s.count("0")
n_1 = s.count("1")
d = abs(n_0 - n_1)
print(n - d)