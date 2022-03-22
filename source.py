# -*- coding: UTF-8 -*-
import random

from IdiomSet import IdiomSet
from IdiomDetail import IdiomDetail
from Drawer import Drawer
from CodeGenerator import CodeGenerator
import turtle

if __name__ == '__main__':
    # 创建成语集对象
    idiom_set = IdiomSet()
    # 设置成语集对象中的格式化数据（导入chengyu_utf8.txt后转化而得）
    idiom_set.set_idiom_df()

    # 第一个成语
    first_idiom = '侯阳洋'
    # 接龙次数
    solitaire_time = 10

    # 进行成语接龙，将接龙结果保存到了成语集对象的solitaire_set列表中
    idiom_set.set_solitaire_list(first_idiom, solitaire_time)

    """-----成语接龙结果显示-----"""

    # 获取接龙结果
    res_list = idiom_set.get_solitaire_list()

    # 创建画笔对象
    drawer = Drawer()

    # 画内外边框
    drawer.create_edge()

    drawer.set_font(('宋体', 15, 'normal'))

    # 绘制接龙结果
    drawer.draw_list(res_list, - drawer.screenWidth // 2 + 50, drawer.screenHeight // 2 - 50)

    """-----成语释义显示-----"""
    # 创建成语信息工具类
    idiom_detail = IdiomDetail()
    content = ''
    target_idiom = ''
    for idiom in res_list[1:]:
        # 获取url
        url = idiom_detail.get_url(idiom)
        # 获取soup
        bs = idiom_detail.get_bs(url)
        # 获取文本内容
        content = idiom_detail.get_content(bs)
        if content == '未查询到成语释义':
            continue
        else:
            target_idiom = idiom
            break
    # 打印文本内容
    # 绘制成语
    drawer.draw_text(target_idiom, 20, -40)
    drawer.set_font(('宋体', 12, 'normal'))
    # 绘制释义
    drawer.draw_text_with_line_wrap(content, 20, -60, line_spacing=20, word_num=20)

    """-----条形码和二维码显示-----"""
    # 学号设置
    number = '41904193'
    code_generator = CodeGenerator()
    pic_path = code_generator.create_barcode(number)
    # 画条形码
    drawer.draw_pic(pic_path, 40, 150, 0.5)
    # 创建二维码
    pic_path = code_generator.create_QRcode('https://github.com/jjhhyyg/python_hw_2')
    # 画二维码
    drawer.draw_pic(pic_path, 200, 150, 0.37)

    """-----签名显示-----"""
    drawer.set_font(('Segoe Script', 48, 'normal'))
    drawer.pencolor('black')
    drawer.draw_text('Hyy', 55, 170)

    turtle.done()
