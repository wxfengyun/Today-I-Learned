# 修复es的red状态

## 编写如下脚本,删除变红的索引

#!/bin/bash

for index in $(curl  -s 'http://192.168.0.234:9200/_cat/indices' | grep red | awk '{print $3}' ); do

	curl -XDELETE "192.168.0.234:9200/$index"

done