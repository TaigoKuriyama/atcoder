#!/usr/bin/env python3
n = int(input()) 
def divisors(n):
    div = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            div.append(i)
            if i != n // i:
                div.append(n//i)
    return div
ans = 0
for i in range(1, n + 1):
    if i % 2 != 0:
        div = divisors(i)
        if len(div) == 8:
            ans += 1
print(ans)