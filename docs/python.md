## sorted()
- option 無しで昇順
- `reverse=True` で降順
```py
>>> org_list = [3, 1, 4, 5, 2]
>>> new_list = sorted(org_list)
>>> print(new_list)
[1, 2, 3, 4, 5]
>>> new_list = sorted(org_list, reverse=True)
>>> print(new_list)
[5, 4, 3, 2, 1]
```

## リストの取り出し
L =[3, 1, 4, 5, 2] のリストから、上から大きいN個をのぞいた数字の合計

```py
L = sorted([3, 1, 4, 5, 2], reverse=True)
N = 3
print(sum(L[N:]))
```
以下はよくない
```py
L = sorted([3, 1, 4, 5, 2], reverse=True)
N = 3
for i in range(N):
    L.pop(0)
print(sum(L))
```