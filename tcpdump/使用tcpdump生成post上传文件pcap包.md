# 使用tcpdump生成post上传文件pcap包

当我们需要构造一个包含文件的pcap数据包的时候，可以这样操作

打开两个`shell`窗口，在第一个窗口中执行抓包命令

```bash
tcpdump -i eth1 port 80 -w test.pcap
```

在另一个窗口中执行上传文件的操作
```bash
curl -X POST http://www.baidu.com/xxx -F "file=@/data/sample.exe"
```

当curl返回之后，切换到第一个`shell`窗口，用`ctrl + c`停止抓包，然后下载test.pcap就可以看到流量中包含了sample.exe文件了
