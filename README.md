# Steam\_Review

调用steamAPI收集某款游戏的评价数据的爬虫



新内容（以下）

**修改了一些东西
储存进txt文件修改为储存进表格
并且原本如果没有内容了他还会继续循环拼接URL，修改后就不会了！直接退出并且保存**

## **`使用方法：`**

1.  你得有**python**，并且安装了**requests**，**pandas**
2.  双击运行脚本（如果闪退，请使用cmd运行，即可查看为啥报错）
3.  **game\_id** 指的是  **<https://store.steampowered.com/app/730/CounterStrike_Global_Offensive/>** 里面的**730**，其他游戏也是一样的

    **具体获取URL流程：打开商店->复制URL->找到game\_id->填入命令行->回车运行！**
4.  等待运行结束并且保存，保存格式为**game\_id.cvs**  如果之前已经运行过，那么会继续添加进去，所以有需要的，可以删除原表格再运行


#给个Star呗！！！
