# mysql查看最大连接数的配置

## 查看当前mysql的最大连接数限制
```sql
mysql> show variables like 'max_connections';
+-----------------+-------+
| Variable_name  | Value  |
+-----------------+-------+
| max_connections | 151   |
+-----------------+-------+
```

## 查看服务器开启至今曾经响应过的最大连接数
```sql
mysql> show global status like 'Max_used_connections';
+----------------------+-------+
| Variable_name    | Value     |
+----------------------+-------+
| Max_used_connections | 5   |
+----------------------+-------+
```

## 修改最大连接数
```sql
set global max_connections=1000;
```

## 查看数据库当前运行的线程数量
```sql
 mysql> show status like 'Threads%';
 +-------------------+-------+
 | Variable_name     | Value |
 +-------------------+-------+
 | Threads_cached    | 58    |
 | Threads_connected | 57    |   ###这个数值指的是打开的连接数
 | Threads_created   | 3676  |
 | Threads_running   | 4     |   ###这个数值指的是激活的连接数，这个数值一般远低于connected数值
 +-------------------+-------+
```

## 查看数据库当前运行的线程具体细节(包括正在执行的sql语句)
```sql
show processlist;
```