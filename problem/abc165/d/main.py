#!/usr/bin/env python3
import math
a, b, n = map(int, input().split())
if n >= b:
    print(math.floor((a * (b - 1)) / b) - a * math.floor((b - 1) / b))
else:
    print(math.floor((a * n / b) - a * math.floor(n / b)))