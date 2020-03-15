# atcoder

## Login

Prepare
```sh
$ pip3 install online-judge-tools
$ npm install -g atcoder-cli
$ pip3 install selenium
```
Update
```sh
$ pip3 install -U online-judge-tools
```

Login
```sh
# Login to AtCoder by acc
$ acc login
? username: xxxxx
? password: [hidden]
OK

# Login to AtCoder by oj
$ oj login https://atcoder.jp/
[!] update available: 7.2.2 -> 9.0.0
[*] run: $ pip3 install -U online-judge-tools
[*] see: https://github.com/kmyk/online-judge-tools/blob/master/CHANGELOG.md
[x] service recognized: AtCoderService.from_url('https://atcoder.jp/'): https://atcoder.jp/
[x] load cookie from: /Users/taigokuriyama/Library/Application Support/online-judge-tools/cookie.jar
[x] GET: https://atcoder.jp/contests/practice/submit
[x] 302 Found
[!] You are not signed in.
[ERROR] Selenium is not installed: try $ pip3 install selenium
[!] use CUI login since Selenium fails
[x] GET: https://atcoder.jp/contests/practice/submit
[x] 302 Found
[x] GET: https://atcoder.jp/login
[x] 200 OK
Username: xxxxx1
Password: 
[x] POST: https://atcoder.jp/login
[x] redirected: https://atcoder.jp/home
[x] 200 OK
[!] AtCoder says: × Welcome, taigok.
[+] Welcome,
[x] GET: https://atcoder.jp/contests/practice/submit
[x] 200 OK
[*] You have already signed in.
[x] save cookie to: /Users/taigokuriyama/Library/Application Support/online-judge-tools/cookie.jar
```


```sh
# 
$ acc new abc153
? select tasks A Serval vs Monster
[!] update available: 7.2.2 -> 9.0.0
[*] run: $ pip3 install -U online-judge-tools
[*] see: https://github.com/kmyk/online-judge-tools/blob/master/CHANGELOG.md
[x] problem recognized: AtCoderProblem.from_url('https://atcoder.jp/contests/abc153/tasks/abc153_a'): https://atcoder.jp/contests/abc153/tasks/abc153_a
[x] load cookie from: /Users/taigokuriyama/Library/Application Support/online-judge-tools/cookie.jar
[x] GET: https://atcoder.jp/contests/abc153/tasks/abc153_a
[x] 200 OK
[x] save cookie to: /Users/taigokuriyama/Library/Application Support/online-judge-tools/cookie.jar

[*] sample 0
[x] input: sample-1
10 4

[+] saved to: tests/sample-1.in
[x] output: sample-1
3

[+] saved to: tests/sample-1.out

[*] sample 1
[x] input: sample-2
1 10000

[+] saved to: tests/sample-2.in
[x] output: sample-2
1

[+] saved to: tests/sample-2.out

[*] sample 2
[x] input: sample-3
10000 1

[+] saved to: tests/sample-3.in
[x] output: sample-3
10000

$ tree abc153/
abc153/
├── a
│   └── tests
│       ├── sample-1.in
│       ├── sample-1.out
│       ├── sample-2.in
│       ├── sample-2.out
│       ├── sample-3.in
│       └── sample-3.out
└── contest.acc.json

2 directories, 7 files

```

```sh
$ touch a.py
$ vim a.py
$ oj t -c "python3 a.py" -d ./tests/
[*] 3 cases found
time: illegal option -- f
usage: time [-lp] command.
[!] GNU time is not available: time

[*] sample-1
[x] time: 0.074724 sec
[+] AC

[*] sample-2
[x] time: 0.060065 sec
[+] AC

[*] sample-3
[x] time: 0.058510 sec
[+] AC

[x] slowest: 0.074724 sec  (for sample-1)
[+] test success: 3 cases
```

## Link
- [AtCoder](https://atcoder.jp/)
- [AtCoder Problems](https://kenkoooo.com/atcoder/#/table/taigok)
- [online-judge-tools](https://github.com/kmyk/online-judge-tools)