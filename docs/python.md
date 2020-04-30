# python

## タプル

変更不可なシーケンス

```py
>>> t = (0, 1, 2)
>>> t
(0, 1, 2)
>>> type(t)
<class 'tuple'>
>>> t[0]
0
>>> t[2]
2
>>> t[0] = 100
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> t + (3, 4, 5)
(0, 1, 2, 3, 4, 5)
```

## キャスト

```py
>>> int(1.01)
1
>>> float(1.01)
1.01
```

## 四則演算

- 割り算
  - `//`
    - 整数の商
    - 除算値を超えない最大の整数
    - マイナスに注意

```py
>>> 10 / 3
3.3333333333333335
>>> 10 // 3
3
>>> -10 // 3
-4
>>> 10 % 3
1
```

- 余り
  - `%`

```py
>>> 10 % 3
1
```

## リスト基礎

- range(1, 10) の場合、1 ~ 9 までの繰り返し

```py
>>> for i in range(1, 10):
...     print(i)
...
1
2
3
4
5
6
7
8
9

```

## スライス

```py
>>> l = list(range(10))
>>> l
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> l[:5]
[0, 1, 2, 3, 4]
>>> l[:0]
[]
```

## set()

```py
# set型は重複しない要素（同じ値ではない要素、ユニークな要素）のコレクション
>>> s = {1, 1, 2, 2, 3, 4, 5}
>>> s
set([1, 2, 3, 4, 5])
>>> type(s)
<type 'set'>

# 空の場合は辞書
>>> d = {}
>>> type(d)
<type 'dict'>

# 要素の追加
>>> s = {0, 1, 2}
>>> s.add(3)
>>> s
set([0, 1, 2, 3])

```

- https://note.nkmk.me/python-set/

## アルファベット

```py
>>> ord("a")
97
>>> chr(ord(a))
'a'
>>> chr(ord(a)+1)
'b'
```

- ord(s)
  - 1 文字の Unicode 文字を表す文字列に対し、その文字の Unicode コードポイントを表す整数を返す
  - https://docs.python.org/ja/3/library/functions.html#ord
- chr(i)
  - Unicode コードポイントが整数 i である文字を表す文字列を返す
  - https://docs.python.org/ja/3/library/functions.html#chr

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

L = [3, 1, 4, 5, 2] のリストから、上から大きい N 個をのぞいた数字の合計

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
>>> ans = [1, 2, 3, 4, 5]
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

## 特定のインデックス以外のリストを取得

```py
>>> import numpy as np
>>> v = np.arange(10)
>>> v
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> rm = [5, 7]
>>> i = np.ones(10, dtype=bool)
>>> i[rm] = False
>>> v[i]
array([0, 1, 2, 3, 4, 6, 8, 9])
```

## プログラムを終了

どれでも良い。

```py
import sys
sys.exit()
```

```py
exit()
```

```py
quit()
```

## 最大公約数

`math` は　 AtCoder の Python のバージョンの関係上使用できないので、`fractions`を使う

```py
>>> import fractions
>>> ans = fractions.gcd(123, 456)
>>> ans
3
```

## 最小公倍数

```py
>>> import fractions
>>> f = fractions.gcd(123, 456)
>>> ans = (123 * 456) // f
>>> ans
18696
```

## 文字列はイミュータブル

```py
>>> s = "abc"
>>> s[1] = "b"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
```

## 入力

```py
>>> l = [int(input()) for i in range(5)]
1
2
3
4
5
>>> l
[1, 2, 3, 4, 5]
```

```py
>>> a, b, c, d, e = [int(input()) for i in range(5)]
1
2
3
4
5
>>> a
1
>>> b
2
>>> c
3
>>> d
4
>>> e
5
```

一行で文字列と数値の入力をする場合は、とりあえず両方とも string で受け取って、 `float()` で変換する。

```py
>>> input().split()
1000 JPY
['1000', 'JPY']
>>> x, s = input().split()
1000 JPY
>>> xs, s = input().split()
1000 JPY
>>> x = float(xs)
>>> x
1000.0
>>> type(x)
<class 'float'>

```

## 切り上げまでの数

- 例えば、28 を 30 にするのに必要な数は 2

```
>>> l = [101, 86, 119, 108]
>>> ans = [-(-a // 10) * 10 - a for a in l]
>>> ans
[9, 4, 1, 2]
```

## 数え上げ

- counter が早い(はず)

  - 下記は pypy でも可

- [abc163 c](https://atcoder.jp/contests/abc163/tasks/abc163_c)

```py
# 2206 ms
n = int(input())
l = list(map(int, input().split()))
for i in range(1, n+1):
    print(l.count(i))
```

```py
# 200 ms
import collections
n = int(input())
l = sorted(list(map(int, input().split())))
c = collections.Counter(l)
[print(c[i]) for i in range(1, n+1)]
```

```py
# 206 ms
import collections
n = int(input())
l = list(map(int, input().split()))
c = collections.Counter()
c.update(l)
[print(c[i]) for i in range(1, n+1)]
```
