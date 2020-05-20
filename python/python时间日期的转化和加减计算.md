# python时间日期的转化和加减计算

## 获取当前日期和时间
```python
>>> from datetime import datetime
>>> now = datetime.now() # 获取当前datetime
>>> print(now)
2015-05-18 16:28:07.198690
```

## 时间转化为字符串
```python
>>> from datetime import datetime
>>> now = datetime.now()
>>> print now.strftime('%Y-%m-%d %H:%M:%S')
2020-05-20 15:29:10
```

## 时间加减
```python
>>> from datetime import datetime, timedelta
>>> now = datetime.now()
>>> now + timedelta(hours=10)
>>> now - timedelta(days=1)
>>> now + timedelta(days=2, hours=12)
```