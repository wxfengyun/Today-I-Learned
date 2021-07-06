# 修复innodb损坏的数据

## 服务器断电可能导致mysql数据损坏无法启动，此时可以参考如下方法修复

1、用忽略错误方式先将mysql启动

在mysql的配置文件my.cnf里找到 [mysqld]字段下，添加 innodb_force_recovery=1：

my.cnf代码如下：

```sql
[mysqld]
innodb_force_recovery = 1
```

innodb_force_recovery参数说明：

如果innodb_force_recovery = 1不生效，则可尝试2——6几个数字
然后重启mysql，重启成功。然后使用mysqldump或 pma 导出数据，执行修复操作等。修复完成后，把该参数注释掉，还原默认值0。
配置文件的参数：innodb_force_recovery
innodb_force_recovery影响整个InnoDB存储引擎的恢复状况。默认为0，表示当需要恢复时执行所有的恢复操作（即校验数据页/purge undo/insert buffer merge/rolling back&forward），当不能进行有效的恢复操作时，mysql有可能无法启动，并记录错误日志；
innodb_force_recovery可以设置为1-6,大的数字包含前面所有数字的影响。当设置参数值大于0后，可以对表进行select,create,drop操作,但insert,update或者delete这类操作是不允许的。

```
1(SRV_FORCE_IGNORE_CORRUPT):忽略检查到的corrupt页。
2(SRV_FORCE_NO_BACKGROUND):阻止主线程的运行，如主线程需要执行full purge操作，会导致crash。
3(SRV_FORCE_NO_TRX_UNDO):不执行事务回滚操作。
4(SRV_FORCE_NO_IBUF_MERGE):不执行插入缓冲的合并操作。
5(SRV_FORCE_NO_UNDO_LOG_SCAN):不查看重做日志，InnoDB存储引擎会将未提交的事务视为已提交。
6(SRV_FORCE_NO_LOG_REDO):不执行前滚的操作
```

在修改innodb_force_recovery并重启数据服务时，重启命令一直在等待，查看日志发现出现很多如下日志条目
```
InnoDB: Waiting for the background threads to start
InnoDB: Waiting for the background threads to start
InnoDB: Waiting for the background threads to start
．．．
```
修改配置文件my.cnf，添加`innodb_purge_threads = 0`可以解决



2、导出数据脚本

mysqldump -uroot -p123 test > test.sql
导出SQL脚本。或者用Navicat将所有数据库/表导入到其他服务器的数据库中。
注意：这里的数据一定要备份成功。然后删除原数据库中的数据。

3、删除ib_logfile0、ib_logfile1、ibdata1

备份MySQL数据目录下的ib_logfile0、ib_logfile1、ibdata1三个文件，然后将这三个文件删除

4、配置my.cnf

将my.cnf中innodb_force_recovery = 1或2——6几个数字这行配置删除或者配置为innodb_force_recovery = 0，重启MySQL服务

5、将数据导入MySQL数据库

mysql -uroot -p123 test < test.sql; 或者用Navicat将备份的数据导入到数据库中。
此种方法下要注意的问题：
1、ib_logfile0、ib_logfile1、ibdata1这三个文件一定要先备份后删除；
2、一定要确认原数据导出成功了
3、当数据导出成功后，删除原数据库中的数据时，如果提示不能删除，可在命令行进入MySQL的数据目录，手动删除相关数据库的文件夹或者数据库文件夹下的数据表文件，前提是数据一定导出或备份成功。
