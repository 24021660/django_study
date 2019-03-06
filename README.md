# django_study
django_learn
数据库连接：
sqlserver请安装：pip install django-pyodbc-azure

DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'sql_server.pyodbc',
        'NAME': 'MyDjango',#数据库名
        'USER': 'sa',#数据库登录用户
        'PASSWORD': '123456',#数据库密码
        'HOST': '127.0.0.1',#数据库服务器
        'PORT': '',#端口，默认1433
        'OPTIONS': {#odbc驱动
            'driver': 'SQL Server Native Client 11.0',
            'MARS_Connection': True,
        },
    }
 }

 连接已经有数据表数据库
 新建app模型：django-admin startapp 模型名称
 然后：python manage.py inspectdb
 运行完毕之后：python manage.py inspectdb >TestModel/models2.py（你的模型文件夹/模型文件）
 templates中html找不到：settings的templates中的dir=[BASE_DIR+"/templates",],  

关于前端：
静态文件的设置：在根目录建立static文件夹，在settings里面设置
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
然后网页中记得输入{% load staticfiles %}
在引用静态文件时：例如,以layui举例，<link ref="sytlesheet" href="{% static 'layui/css/layui.css' %}">
<script src="{% static 'layui/layui.js' %}"
1.关于layui
  table中数据接口的使用：
  首先，用layui在html页中进行添加<table>,以及
  <script>
  table.render({
   elem: '#test'
   ,url:'/test/'       // 数据接口，后续讲解
   ,cellMinWidth: 80 //全局定义常规单元格的最小宽度，layui 2.2.1 新增
   ,cols: [[
       {field:'username', width:80, title: '用户名', sort: true}
     ,{field:'password', width:80, title: '密码'}
     ,{field:'email', width:160, title: '邮箱'}
     ,{field:'phonecode', width:160, title: '电话'}
     ,{field:'realname', width:160,title:'姓名'}
   ]]
 });
});
</script>
其次，在后台.py文件中进行数据库操作
    db = TbMember.objects.all()
    ajax_testvalue = serializers.serialize("json", db)
    m=json.loads(ajax_testvalue)
    data_db=[x['fields'] for x in m]
    data = {"code": 0, "msg": "", "count": 10, "data": data_db}
    return HttpResponse(json.dumps(data), content_type="application/json")
最后，urls.py 里面添上网址：例如test
然后回到HTML中的<script>里面的url：下改成关联的网页test
