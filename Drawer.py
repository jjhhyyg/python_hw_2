# -*- coding: UTF-8 -*-

import turtle

import cv2

from Picture import Picture


class Drawer(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.screenWidth = 800
        self.screenHeight = 600
        self.ht()
        self.speed(5)
        self.font = ("宋体", 12, "normal")
        turtle.screensize(self.screenWidth, self.screenHeight)
        turtle.setup(1920, 1080)
        turtle.colormode(255)

    def set_font(self, font):
        """
        设置字体格式
        :param font: 三元组
        :return: None
        """
        self.font = font

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
        self.write(text, move=False, align="left", font=self.font)

    def draw_pic(self, pic_path, pos_x, pos_y, scale=1):
        """
        在指定位置打印图片
        :param pic_path: 需要打印的图片的路径
        :param pos_x: 起始x坐标
        :param pos_y: 起始y坐标
        :param scale: 缩放因子，默认为1
        :return: None
        """
        self.move(pos_x, pos_y)
        # 创建图像对象
        picture = Picture(pic_path)
        image_info = picture.get_img_info()
        # 等比例缩放图片
        picture.img = cv2.resize(picture.img, (int(image_info[1] * scale), int(image_info[0] * scale)))
        # 获取图片信息（height, width, dimension）
        image_info = picture.get_img_info()
        # 设置画笔属性
        self.pensize(1)
        self.speed(0)
        turtle.delay(0)

        for y in range(image_info[0]):
            # 将笔刷移到画布最左边并更新其纵坐标
            self.penup()
            self.setpos(pos_x, pos_y - y)
            self.pendown()
            # 一行一行地更新图片，加快速度
            turtle.tracer(False)
            for x in range(image_info[1]):
                # 设置画笔颜色
                self.pencolor(picture.img[y, x, 2], picture.img[y, x, 1], picture.img[y, x, 0])
                self.forward(1)
            # 图片更新
            turtle.update()

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

    def draw_text_with_line_wrap(self, text, pos_x, pos_y, word_num=10, line_spacing=30):
        """
        带自动换行的文本绘制
        :param text: 待绘制的文本
        :param pos_x: 起始横坐标
        :param pos_y: 起始纵坐标
        :param word_num: 每行文字数目，默认为10
        :param line_spacing: 行间距，默认为30
        :return: None
        """

        text_list = []
        i = 0
        # 将一行text按每行word_num个字添加到text_list中
        while (i + 1) * word_num < len(text):
            text_list.append(text[i * word_num: (i + 1) * word_num])
            i += 1
        # 添加不足word_num的剩余部分
        if i != len(text) - 1:
            text_list.append(text[i * word_num:])
        # 按行输出文字
        self.draw_list(text_list, pos_x, pos_y, line_spacing)
