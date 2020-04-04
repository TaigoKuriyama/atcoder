#!/usr/bin/env python3
n, k = map(int, input().split())
if n == k:
    print(0)
else:
    ans = n % k
    while (True):
        if ans < abs(ans - k):
            print(ans)
            exit()
        ans = abs(ans - k)
