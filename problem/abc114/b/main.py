#!/usr/bin/env python3
s = input()
ans = 753
for i in range(len(s)-2):
    d = abs(753 - int(s[i: i + 3]))
    if d < ans: ans = d
print(ans)