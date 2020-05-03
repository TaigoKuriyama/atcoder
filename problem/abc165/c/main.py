#!/usr/bin/env python3
n, m, q = map(int, input().split())
dic = {}
for _ in range(q):
    a, b, c, d = map(int, input().split())
    dic[(a, b), c] = d
dic = dict(sorted(dic.items(), key=lambda x: x[1], reverse=True))
ans = 0
tmp = {}
print(dic)
for k in dic:
    print("k[0]: ", k[0])
    print("k[1]: ", k[1])
    print("tmo", tmp)
    if k[0] not in tmp:
        print("1", k)
        ans += dic[k]
        tmp[k[0]] = k[1]
    elif k[0] in tmp and k[0][0] == tmp[k[0]]:
        print("2", k)
        ans += dic[k]
print(ans)