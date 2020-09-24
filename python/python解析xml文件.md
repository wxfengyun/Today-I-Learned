# python解析xml文件

`python`解析`xml`文件的常规方法可以参见此文[Python XML 解析](https://www.runoob.com/python/python-xml.html)


其中`dom`的方式比较清晰易懂，但是有个弊端，就是这个库会现将xml加载到内存建立`dom`树之后处理，如果`xml`文件比较大的话（几十MB以上），内存消耗非常严重，而且速度很慢。

使用`sas`的方式会比较快，但是代码不太好理解，用到了回调的方式处理`xml`文件，上面文章中给的`sas`的示例代码是遇到一个标签就直接打印，但是如果想将每个标签组里面的信息存储到列表中，后续统一再处理的话，这个示例代码就不好使了。

于是又找了另外一个示例代码[Python中使用SAX解析XML](https://blog.csdn.net/xiaohao0724/article/details/81317757)，其中的用法二可供参考

```
from xml.parsers.expat import ParserCreate


class Student:
    def __init__(self, name=None, age=None, sex=None, score=None):
        self.name = name
        self.age = age
        self.sex = sex
        self.score = score

    def __str__(self):
        return "姓名：{0}，年龄：{1}，性别：{2}，成绩：{3}".format(self.name, self.age, self.sex, self.score)


students = []


class MySaxHandler(object):
    def __init__(self):
        self.tag = None
        self.student = None

    def start_element(self, name, attrs):
        print('start_element: %s---attrs: %s' % (name, str(attrs)))
        self.tag = name
        if name == "student":
            self.student = Student()

    def char_data(self, text):
        print('content: %s' % text)
        if self.tag == "name":
            self.student.name = text
        if self.tag == "age":
            self.student.age = text
        if self.tag == "sex":
            self.student.sex = text
        if self.tag == "score":
            self.student.score = text

    def end_element(self, name):
        print('end_element: %s' % name)
        if name == "student":
            students.append(self.student)
            self.student = None
        self.tag = None


with open("students.xml", "r", encoding="utf-8") as stu:
    content = stu.read()

handler = MySaxHandler()
parser = ParserCreate()

parser.StartElementHandler = handler.start_element
parser.CharacterDataHandler = handler.char_data
parser.EndElementHandler = handler.end_element
parser.Parse(content)
for student in students:
    print(student)
```


