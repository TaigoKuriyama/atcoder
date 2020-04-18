#!/usr/bin/env python3
s = input()
l = ["A", "C", "G", "T"]
ans = 0
tmp = 0
for i in range(len(s)):
    if s[i] in l:
        tmp += 1
        if ans <= tmp:
            ans = tmp
    else:
        tmp = 0
print(ans)