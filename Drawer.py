# -*- coding: UTF-8 -*-

import turtle


class Drawer(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.screenWidth = 800
        self.screenHeight = 600
        self.ht()
        self.speed("fast")
        turtle.setup(self.screenWidth, self.screenHeight, 0, 0)
        turtle.colormode(255)

    def create_edge(self):
        """
        将画面划为三个区域
        :return: None
        """
        # 画外边框
        self.pensize(4)
        edge_size = 4
        self.move(-self.screenWidth // 2 + edge_size, self.screenHeight // 2 - edge_size)
        self.begin_fill()
        self.fillcolor(232, 221, 203)
        self.goto(self.screenWidth // 2 - edge_size, self.screenHeight // 2 - edge_size)
        self.goto(self.screenWidth // 2 - edge_size, -self.screenHeight // 2 + edge_size)
        self.goto(-self.screenWidth // 2 + edge_size, -self.screenHeight // 2 + edge_size)
        self.goto(-self.screenWidth // 2 + edge_size, self.screenHeight // 2 - edge_size)
        self.end_fill()

        # 画内边框
        self.pensize(2)
        self.move(0, self.screenHeight // 2 - edge_size)
        self.goto(0, -self.screenHeight // 2 + edge_size)

        self.move(0, 0)
        self.goto(self.screenWidth // 2 - edge_size, 0)

    def draw_text(self, text, pos_x, pos_y):
        """
        在指定位置输入文字
        :param text: 需要打印的文字
        :param pos_x: 起始x坐标
        :param pos_y: 起始y坐标
        :return: None
        """
        self.penup()
        self.goto(pos_x, pos_y)
        self.pendown()
        self.write(text, move=False, align="left", font=("宋体", 15, "normal"))

    def draw_pic(self, pic_path, pos_x, pos_y):
        """
        在指定位置打印图片
        :param pic_path: 需要打印的图片的路径
        :param pos_x: 起始x坐标
        :param pos_y: 起始y坐标
        :return: None
        """
        self.penup()
        self.goto(pos_x, pos_y)
        self.pendown()
        self.getscreen().bgpic(pic_path)

    def move(self, pos_x, pos_y):
        """
        不带痕迹的goto
        """

        self.penup()
        self.goto(pos_x, pos_y)
        self.pendown()

    def draw_list(self, res_list, pos_x, pos_y, line_spacing=30):
        """
        从指定位置开始，以行的形式输出列表内容
        :param res_list: 待输出的列表
        :param pos_x: 初始横坐标
        :param pos_y: 初始纵坐标
        :param line_spacing: 行间距，默认为30
        :return: None
        """

        self.move(pos_x, pos_y)
        cnt = 0
        for line in res_list:
            pos_y -= line_spacing
            # 边界检测
            if pos_x > self.screenWidth // 2 or pos_x < -self.screenWidth // 2 or \
                    pos_y > self.screenHeight // 2 or pos_y < -self.screenHeight // 2:
                break
            self.draw_text(line, pos_x, pos_y)
