# jcl_health_declaration

## 简介

jcl语言学校用健康申报自动脚本

## 部署

### 1. Fork 仓库

* 项目地址：[github/jcl_health_declaration](https://github.com/yyz788634/jcl_health_declaration)
* 点击右上角`Fork`到自己的账号下

> ![image.png](https://i.loli.net/2020/10/28/qpXowZmIWeEUyrJ.png)

### 2.修改个人信息
* 打开jiaoben.py，将自己的学生証番号、名前、クラス按照格式替换（クラス一定要与选项完全一致）

> ![image.png](https://i.loli.net/2020/12/07/3ZerPKGSHcJbkAQ.png)
> ![image.png](https://i.loli.net/2020/12/07/Sj9LKuzlJaqQEos.png)

### 3.启用 Actions

> Actions 默认为关闭状态，Fork 之后需要手动执行一次，若成功运行其才会激活。

返回项目主页面，点击上方的`Actions`，再点击左侧的`jcl health declaration`，再点击`Run workflow`
    
![image.png](https://i.loli.net/2020/12/07/fNgYHqbksrPBAeQ.png)

至此，部署完毕。

## 结果

当你完成上述流程，可以在`Actions`页面点击`jcl health declaration`-->`build`-->`run sign`查看结果。

如果成功，会输出类似`"result": "Success"`的信息：

如果失败，会输出类似`"result": "Failed"`的信息：

## 注意

1. 程序会在每天中午自动执行申报流程，也可以随时通过上述`步骤3`手动触发
