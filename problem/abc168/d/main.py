#!/usr/bin/env python3
from collections import deque
n, m = map(int, input().split())
x = [[] for i in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    x[a] += [b]
    x[b] += [a]
ans = [0] * (n + 1)
ans[1] = 1
que = deque([1])
while que:
    q = que.popleft()
    for i in x[q]:
        if ans[i] == 0:
            ans[i] = q
            que.append(i)
print("Yes")
print(*ans[2:], sep="\n")