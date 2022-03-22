# 成语接龙程序

## 代码组成部分
### 1. source.py
> 主代码，主要实现了以下功能：
+ **成语接龙的随机展示**：可自定义接龙次数和第一个成语，对TypeError进行了异常处理；引入random模块，相同的成语和接龙次数每次运行产生的结果不同
+ **成语释义显示**：利用爬虫实现了在接龙的列表内查找一个成语的释义和出处的功能，对HTTPError、IndexError等进行了异常处理
+ **条形码和二维码显示**：结合作业一的图片打印程序和qrcode、barcode两个模块，实现了学号条形码和github仓库URL二维码的显示
+ **签名**：调用继承于turtle.Turtle类的Drawer类中的函数实现个人签名

### 2. Drawer.py
> 包含继承于turtle.Turtle类的Drawer类，主要实现了以下功能：
+ **画笔的相关属性设置**（屏幕大小、画笔颜色、画笔粗细）
+ **打印的文字的字体设置**（字体、大小、斜体/下划线/正常）
+ **主界面的绘制**
+ **在指定位置绘制字符串**
+ **在指定位置对字符串列表进行分行绘制**
+ **在指定位置对长字符串进行分行绘制**
+ **在指定位置绘制图片**

### IdiomSet.py
> 包含IdiomSet类，主要实现了以下功能：
+ **将特定形式的txt文件转换为格式化文件存储在DataFrame对象中**
+ **进行成语接龙并将结果存储在对应列表中**
+ **返回含接龙结果的列表**
+ **在控制台输出接龙过程**

### IdiomDetail.py
> 包含IdiomDetail类，主要实现了以下功能：
+ **返回带需要搜索的成语的、编码后用于访问指定页面的URL**
+ **返回URL对应的BeautifulSoup对象**
+ **通过源代码解析获取成语释义及出处，返回对应字符串**

### Picture.py
> 包含Picture类，主要实现了以下功能：
+ **通过指定路径用opencv以三原色格式读取图片**
+ **返回由图片的高度、宽度和维度三者组成的元组**
+ **显示图片**

### CodeGenerator.py
> 包含CodeGenerator类，主要实现了以下功能：
+ 基于给定文本创建条形码并以png形式保存至other文件夹中，名为barcode.png
+ 基于给定文本创建二维码并以png形式保存至other文件夹中，名为QRcode.png

## 优点
1. 有许多供用户调节的地方，如行间距、字体样式、接龙次数等
2. 通过爬虫的方法实现了成语释义查询，避免了建立容量较大的本地数据库
3. 面向对象编程，将许多功能模块化，便于代码的维护和改良

## 缺点
1. 没有用户交互界面，对显示结果的修改需要直接修改源码，可以考虑使用tkinter或pyQt来实现界面的交互
2. 不能复制输出结果（当然要是想也可以改改源码在控制台输出，留了相关的接口），同上，用GUI界面来进行设计即可

---
如有错误欢迎指正！感觉不错的话rate一下，感谢~