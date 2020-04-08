#!/usr/bin/env python3
import fractions
a, b = map(int, input().split())
f = fractions.gcd(a, b)
ans = a * b // f
print(ans)
