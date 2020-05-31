#!/usr/bin/env python3
from decimal import Decimal
a, b = input().split()
a = Decimal(int(a))
b = Decimal(b)
print(int(a * b))