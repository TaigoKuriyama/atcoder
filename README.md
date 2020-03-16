# atcoder

## Prepare
```sh
$ pip3 install online-judge-tools
$ npm install -g atcoder-cli
$ pip3 install selenium
```
## Update
```sh
$ pip3 install -U online-judge-tools
```

## Login
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
## Settings
```sh
# 全部の問題ディレクトリが作られるようにする
$ acc config default-task-choice all
default-task-choice = all
```

```sh
# config ディレクトリの場所を表示
$ acc config-dir
/Users/taigokuriyama/Library/Preferences/atcoder-cli-nodejs

# テンプレート設定
$ cd /Users/taigokuriyama/Library/Preferences/atcoder-cli-nodejs
$ mkdir py
$ cd py
$ touch main.py template.json
$ cat template.json 
{
  "task":{
    "program": ["main.py"],
    "submit": "main.py"
  }
}
$ acc templates
search template directories in /Users/taigokuriyama/Library/Preferences/atcoder-cli-nodejs
NAME  SUBMIT-PROGRAM
py    main.py
```

## ディレクトリ作成
```sh
$ acc new abc154 --template py
$ tree abc154
abc154
├── a
│   ├── main.py
│   └── tests
│       ├── sample-1.in
│       ├── sample-1.out
│       ├── sample-2.in
│       └── sample-2.out
├── b
│   ├── main.py
│   └── tests
│       ├── sample-1.in
│       ├── sample-1.out
│       ├── sample-2.in
│       ├── sample-2.out
│       ├── sample-3.in
│       └── sample-3.out
├── c
│   ├── main.py
│   └── tests
│       ├── sample-1.in
│       ├── sample-1.out
│       ├── sample-2.in
│       ├── sample-2.out
│       ├── sample-3.in
│       └── sample-3.out
├── contest.acc.json
├── d
│   ├── main.py
│   └── tests
│       ├── sample-1.in
│       ├── sample-1.out
│       ├── sample-2.in
│       ├── sample-2.out
│       ├── sample-3.in
│       └── sample-3.out
├── e
│   ├── main.py
│   └── tests
│       ├── sample-1.in
│       ├── sample-1.out
│       ├── sample-2.in
│       ├── sample-2.out
│       ├── sample-3.in
│       ├── sample-3.out
│       ├── sample-4.in
│       └── sample-4.out
└── f
    ├── main.py
    └── tests
        ├── sample-1.in
        ├── sample-1.out
        ├── sample-2.in
        └── sample-2.out

12 directories, 41 files
```

## coding and testing
```sh
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

## submit

```sh
$ acc sub
Invalid command: sub
Use `acc --help` for a list of available commands.
TK2:b taigokuriyama$ acc s
submit to: https://atcoder.jp/contests/abc153/tasks/abc153_b
[x] read history from: /Users/taigokuriyama/Library/Caches/online-judge-tools/download-history.jsonl
[x] found urls in history:

[x] problem recognized: AtCoderProblem.from_url('https://atcoder.jp/contests/abc153/tasks/abc153_b'): https://atcoder.jp/contests/abc153/tasks/abc153_b
[*] code (146 byte):
#!/usr/bin/env python3
H, N = map(int, input().split())
A = list(map(int, input().split()))
if H <= sum(A):
    print("Yes")
else:
    print("No")
[x] load cookie from: /Users/taigokuriyama/Library/Application Support/online-judge-tools/cookie.jar
[x] GET: https://atcoder.jp/contests/abc153/tasks/abc153_b
[x] 200 OK
[x] PyPy is available for Python interpreter
[x] both Python2 and Python3 are available for version of Python
[x] use: 3
[*] chosen language: 3023 (Python3 (3.4.3))
[!] the problem "https://atcoder.jp/contests/abc153/tasks/abc153_b" is specified to submit, but no samples were downloaded in this directory. this may be mis-operation
[x] sleep(3.00)
Are you sure? Please type "abcb" abcb
[x] GET: https://atcoder.jp/contests/abc153/tasks/abc153_b
[x] 200 OK
[x] GET: https://atcoder.jp/contests/abc153/submit
[x] 200 OK
[x] POST: https://atcoder.jp/contests/abc153/submit
[x] redirected: https://atcoder.jp/contests/abc153/submissions/me
[x] 200 OK
[+] success: result: https://atcoder.jp/contests/abc153/submissions/10941930
[x] open the submission page with browser
[x] save cookie to: /Users/taigokuriyama/Library/Application Support/online-judge-tools/cookie.jar
```


## Link
- [AtCoder](https://atcoder.jp/)
- [AtCoder Problems](https://kenkoooo.com/atcoder/#/table/taigok)
- [online-judge-tools](https://github.com/kmyk/online-judge-tools)
- [atcoder-cli](https://github.com/Tatamo/atcoder-cli)
   - [コマンドラインツールatcoder-cliを公開しました](http://tatamo.81.la/blog/2018/12/07/atcoder-cli/)