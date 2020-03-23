#!/usr/bin/env python3
s = input()
n = len(s)
a = s[:(n-1)//2]
d = s[(n+3)//2-1:]
print("Yes") if s == s[::-1] and a == a[::-1] and d[::-1] == d else print("No")