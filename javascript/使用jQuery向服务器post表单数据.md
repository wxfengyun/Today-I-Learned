# 使用jQuery向服务器post表单数据

使用`$.post`方法可以向服务器post数据，
`serializeArray()`函数可以将表单中的项全部整合到一个变量中，
可以通过`push`的方式将其他自定义的数据连通表单一起post给服务器。

```javascript
    var form_data = $('#my-form').serializeArray();
    form_data.push({name: 'other-value', value: "xxxx"});

    $.post("/test/api", form_data, function(data){

        if (data["status"] == 1){
            layer.msg("添加成功", {time: 2000}, function(){

            });
            
        }else{
            layer.msg("添加失败");
        }
            
    });
```

除了上面的post方法，还可以使用更加原生的`$.ajax`方法实现

```javascript
	$.ajax({
        url: "/test/api",
        method: "POST",
        async: true,   // 禁止异步查询
        data: {"password": password, "username": username},
        success: function (response){

        }
    });
```
