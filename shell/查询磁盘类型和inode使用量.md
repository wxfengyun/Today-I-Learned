# 查询磁盘类型和inode使用量

使用命令可以查询磁盘类型和inode使用率
```bash
df -ihT
```

输出信息如下，第二列是磁盘类型，倒数第二列是inode使用率，
如果磁盘没有满，但是inode资源耗尽（小文件太多）磁盘会出现还有空间但是无法写入文件的问题。

```
Filesystem              Type     Inodes IUsed IFree IUse% Mounted on
/dev/mapper/centos-root xfs         94M  250K   93M    1% /
devtmpfs                devtmpfs   7.9M   507  7.9M    1% /dev
tmpfs                   tmpfs      7.9M     1  7.9M    1% /dev/shm

```

如果需要查看具体哪个目录使用的inode资源最大，可以执行

```
find / -xdev -printf '%h\n' | sort | uniq -c | sort -k 1 -n

```

这个命令输出量比较大，执行完，只看最后几行就行