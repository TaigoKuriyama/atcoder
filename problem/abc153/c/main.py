#!/usr/bin/env python3
import sys
N, K = map(int, input().split())
H = sorted(list(map(int, input().split())), reverse=True)
if K != 0:
    if len(H) <= K:
        print(0)
    else:
        print(sum(H[K:]))
else:
    print(sum(H))