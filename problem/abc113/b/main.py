#!/usr/bin/env python3
n = int(input()) 
t, a = map(int, input().split())
h = [abs(t - x * 0.006 - a) for x in map(int, input().split())]
print(h.index(min(h)) + 1)