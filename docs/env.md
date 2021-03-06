# AtCoder

AtCoder

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

# Login to AtCoder by oj
$ oj login https://atcoder.jp/
```

## Settings

```sh
# 全部の問題ディレクトリが作られるようにする
$ acc config default-task-choice all
```

```sh
# display config directory
$ acc config-dir

# setting for template
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

# make default template py
$ acc config default-template py
$ acc templates
search template directories in /Users/taigokuriyama/Library/Preferences/atcoder-cli-nodejs
NAME  SUBMIT-PROGRAM
py    main.py
```

## create problem directory

```sh
$ acc new abc154
```

## testing

```sh
$ ls
main.py	tests
$ test
```

テストケース以外でマニュアルでテストする場合

```sh
$ python main.py
87 # 入力
667 # 出力
```

alias setting：https://github.com/TaigoKuriyama/atcoder/issues/3

## submit

```sh
$ acc s
```

## Link

- [AtCoder](https://atcoder.jp/)
- [AtCoder Problems](https://kenkoooo.com/atcoder/#/table/taigok)
- [online-judge-tools](https://github.com/kmyk/online-judge-tools)
- [atcoder-cli](https://github.com/Tatamo/atcoder-cli)
  - [コマンドラインツール atcoder-cli を公開しました](http://tatamo.81.la/blog/2018/12/07/atcoder-cli/)
