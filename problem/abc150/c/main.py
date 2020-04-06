#!/usr/bin/env python3
import itertools
l = list(range(1, int(input()) + 1))
p = list(map(int, input().split()))
q = list(map(int, input().split()))
cnt_a = 1
cnt_b = 1
for i in itertools.permutations(l):
    if list(i) == p:
        a = cnt_a
    if list(i) == q:
        b = cnt_b
    cnt_a += 1
    cnt_b += 1
print(abs(a - b))
