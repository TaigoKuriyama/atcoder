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
L = [3, 1, 4, 5, 2] のリストから、上から大きいN個をのぞいた数字の合計

```py
l = sorted([3, 1, 4, 5, 2], reverse=True)
n = 3
print(sum(l[n:]))
```
以下はよくない
```py
l = sorted([3, 1, 4, 5, 2], reverse=True)
n = 3
for i in range(n):
    l.pop(0)
print(sum(l))
```

## リスト作成
0 ~ N まで１ずつ増加するリスト

```py
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

```py
>>> list(range(1, 11, 1))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

## リストを１行に表示する

```py
>>> ans = [1, 2, 3, 4,5 ]
>>> print(' '.join(ans))
1 2 3 4 5
```

## 文字列を後ろから取り出す
[147-b](https://atcoder.jp/contests/abc147/tasks/abc147_b)

```py
s = input() # ex."redcoder"
ans = 0
for i in range(len(s)//2):
    if s[i] != s[-1-i]:
        ans += 1
print(ans)
```
- `s[-1]`：文字列の一番後ろの文字。よってここから -1 ずつしていけば後ろから取り出せる

## 文字列を逆順にする
[159-b](https://atcoder.jp/contests/abc159/tasks/abc159_b)

```py
>>> a = 'abcdef'
>>> a[::-1]
'fedcba'
```
- `s[start:stop:step]`のステップに負数を指定することで`s`をリバースする


## スライスのインデックス

```py
>>> s = 'Python'
>>> s[2:5]
'tho'
```
- 先頭のインデックスは`0`から
- 終点のインデックスは含まない