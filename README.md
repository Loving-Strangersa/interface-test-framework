# 接口测试框架

#### 介绍

支持数据驱动，关键字驱动

#### 软件架构

python +request+ pytest +pymysql

#### 安装教程

1. 项目下载到本地后 终端执行安装第三方库 pip install  -r requirements.txt

#### 使用说明

~~~tex
规范说明:

1、路由层进行接口定义，定义接口路径，接口传参方式，json/params/data... 
	KeywordDriven/api/api.py

2、base层进行数据处理，数据过滤，逻辑判断。如果是必须填写的参数使用字典中的[]进行获取,不是必填参数使用config.get("params","params_xxx") 使用默认参数站位
	KeywordDriven/ApiHandle/base.py

3、pp层进行接口返回数据处理 使用静态方法对返回值的code码校验，逻辑尽量写到base层中进行处理
	KeywordDriven/ApiHandle/handle_user.py

4、init中暴露 KeywordDriven/ApiHandle/handle_user.py里的方法
	KeywordDriven/ApiHandle/__init__.py

5、step层不能出现逻辑判断，只能进行传递参数，控制要出现的参数返回到test层

6、编写测试用例，进行数据的更新，数据引用
~~~

