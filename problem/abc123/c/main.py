#!/usr/bin/env python3
import math
n = int(input()) 
l = [int(input()) for _ in range(5)]
m = min(l)
print(math.ceil(n / m) + 4)