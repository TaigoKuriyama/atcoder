#!/usr/bin/env python3
s = input()
a = list(map(str, range(1, 10)))
b = list(map(str, range(0, 3)))
mm = 0
ba = 0
for i in [0, 2]:
    if s[i] == "0" and s[i+1] in a:
        mm += 1
        ba = i
    elif s[i] == "1" and s[i+1] in b:
        mm += 1
        ba = i
if mm == 0:
    print("NA")
elif mm == 1 and ba == 0:
    print("MMYY")
elif mm == 1 and ba == 2:
    print("YYMM")
elif mm == 2:
    print("AMBIGUOUS")
