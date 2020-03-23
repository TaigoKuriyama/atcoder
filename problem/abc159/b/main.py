#!/usr/bin/env python3
import sys
s = input()
for i in range(len(s)//2):
    if s[i] != s[-1-i]:
        print("No")
        sys.exit()
s2 = s[:(len(s)-1)//2]
for i in range((len(s)-1)//2):
    if s2[i] != s2[-1-i]:
        print("No")
        sys.exit()
s3 = s[(len(s)+3)//2-1:]
for i in range((len(s)-1)//2):
    if s3[i] != s3[-1-i]:
        print("No")
        sys.exit()
print("Yes")