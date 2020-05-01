#!/usr/bin/env python3
import numpy as np
n = int(input()) 
t, a = map(int, input().split())
h = list(map(int, input().split()))
a_t = []
for i in h:
    a_t.append(t - i * 0.006)
print(np.abs(np.asarray(a_t) - a).argmin() + 1)