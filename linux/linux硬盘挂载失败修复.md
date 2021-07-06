# linux硬盘挂载失败修复

## 如果linux服务器异常断电，导致mount命令失败，报如下错误
```
Internal error xfs XFS_WANT_CORRUPTED_GOTO at line 1662 of file fs/xfs/libxfs/xfs_alloc.c Caller xfs_free_extent+0x130 [xfs]
```

可以使用如下方法修复

* 先用`xfs_repair /dev/sdb` （这里假设挂载失败的硬盘是/dev/sdb）
* 如果上述方法失败，可以加上`-L`参数强制修复，但是这样可能会丢失部分数据