# apache默认日志加入耗时统计
找到apache的log所在位置，我这里是/etc/httpd/conf/httpd.conf
默认记录的访问日志是没有耗时统计的，比如下面这样
```
LogFormat "%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\" "  combined
```

改成这样就可以统计耗时了
```
LogFormat "%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\" time=%D(us)"  combined
```

%D - 官方解释：Time taken to process the request, in millis，处理请求的时间，以微秒为单位

%T - 官方解释：Time taken to process the request, in seconds，处理请求的时间，以秒为单位

%{ms}T - 官方解释：Time taken to commit the response, in millis，提交响应的时间，以毫秒为单位

如果需要增加其他的统计信息，可以访问[apache的官方文档](http://httpd.apache.org/docs/current/mod/mod_log_config.html)
