#!/usr/bin/env python3
s = input()
ans = len(s)
for i in range(0, 2):
    cnt = 0
    for j in range(0, len(s)):
        if j % 2 == 0 and s[j] != str(i): cnt += 1
        if j % 2 == 1 and s[j] == str(i): cnt += 1
    ans = min(ans, cnt)
print(ans)