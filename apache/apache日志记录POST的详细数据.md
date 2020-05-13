# apache日志记录POST的详细数据

修改httpd.conf文件，加载mod_dumpio模块
```
LoadModule dumpio_module modules/mod_dumpio.so
```

同时将日志级别从`warn`改为`dumpio:trace7`，具体编辑和添加的信息如下
```
LogLevel dumpio:trace7
DumpIOInput On
DumpIOOutput On
```

重启apache加载模块，使用如下命令可以查看apache已经加载的模块
```
apachectl -t -D DUMP_MODULES
```

完成后，POST数据的信息就会记录在 `/var/log/httpd/error_log` 里面了

