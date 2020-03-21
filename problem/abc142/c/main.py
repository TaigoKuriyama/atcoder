#!/usr/bin/env python3
n = int(input()) 
a = list(map(int, input().split()))
l = list(range(1, len(a)+1, 1))
d = dict(zip(a, l))
ans = [str(d[x]) for x in l]
print(' '.join(ans))