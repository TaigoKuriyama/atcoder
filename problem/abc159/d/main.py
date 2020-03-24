#!/usr/bin/env python3
import math
import numpy as np
import collections
def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
n = int(input()) 
a = np.array(list(map(int, input().split())))
ans = {}
for i in range(n):   
    if a[i] in ans.keys():
        print(ans[a[i]])
        continue
    ans[a[i]] = 0
    ind = np.ones(n, dtype=bool)
    ind[i] = False
    c = collections.Counter(a[ind])
    for k in c.keys():
        if c[k] >= 2:
            ans[a[i]] += comb(c[k], 2)
    print(ans[a[i]])