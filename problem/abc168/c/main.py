#!/usr/bin/env python3
import math
a, b, h, m = map(int, input().split())
y = 360 * m / 60
x = 360 * (h * 60 + m) / 720
print(x)
if x == 0 and y >= 180:
    x = 360
if y == 0 and x >= 180:
    y = 360
ang = max(x, y) - min(x, y)
print(ang)
print(math.sqrt((a ** 2) + (b ** 2) - (2 * a * b * math.cos(math.radians(ang)))))