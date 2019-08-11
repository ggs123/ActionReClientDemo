# ActionReDemo
行为识别可视化系统的客户端

## mvc模式
本客户端采用MVC模式，其中view通知controllor；controller接到通知，对应的处理函数会去调用model的方法；model完成对数据的操作之后，会通知view，view再来到model里面取数据，然后更新ui。

mvc之中，view只负责到model里面取数据然后显示出来，model里面只负责存放数据，目前不涉及到对数据的增删改，controller来控制所有的逻辑，比如播放的逻辑，比如对原始数据的相关处理操作等。


## signal与slot(信号与槽)
这三个模块间的通信是靠pyqt5的signal与slot来实现的。当前有两对信号与槽，第一对是view与controller，当view初始化完成之后，通知controller，controller来开启计时器。
；第二对是model与view之间的。

