#!/usr/bin/env python3
m, n = map(int, input().split())
print((m * (m-1) + n * (n - 1)) // 2)