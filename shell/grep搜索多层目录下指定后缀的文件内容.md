# grep搜索多层目录下指定后缀的文件内容
使用 `grep`搜索多级嵌套目录下的文件内容，一般可以这样写

```bash
$ grep -R "search word" */*
```
但是这样搜索有个缺点，无法限定指定的文件后缀名，如果目录下有很多无关文件的话，搜索效率就会很低

此时可以使用 `shopt` 打开globstar参数以后，`**`匹配零个或多个子目录。因此，`**/*.txt`就可以得到想要的结果。

```bash
$ shopt -s globstar
$ grep -R "search word" **/*.txt
```
