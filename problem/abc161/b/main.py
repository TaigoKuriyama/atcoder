#!/usr/bin/env python3
n, m = map(int, input().split())
a = sorted(list(map(int, input().split())), reverse=True)
for i in range(m):
    if a[i] < sum(a) * (1 / (4 * m)):
        print("No")
        exit()
print("Yes")
