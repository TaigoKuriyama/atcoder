#!/usr/bin/env python3
x = int(input())
ans = 1
m = 100
while True:
    m = int(m * 1.01)
    if m >= x:
        print(ans)
        exit()
    else:
        ans += 1
    