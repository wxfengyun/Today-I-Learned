# 将python源代码编译成elf文件
`pyinstaller`可以帮助我们将`python`源代码打包成`exe`或者`elf`使用，防止源代码泄露

使用`pip`安装`pyinstaller`  
```
pip install pyinstaller
```

或者去[pyinstaller官网](http://www.pyinstaller.org/downloads.html)下载安装

安装完成后，执行如下命令
```python
pyinstaller --onefile xxx.py (你的源代码)
```
然后在`dict`目录下就是编译好的`elf`可执行文件了



