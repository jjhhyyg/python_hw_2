# -*- coding: UTF-8 -*-

import pandas as pd
import codecs
from xpinyin import Pinyin
import random
import datetime
import copy

random.seed(datetime.datetime.now())


class IdiomSet:
    def __init__(self):
        self.df = None
        self.file_path = ''
        self.file_name = './other/chengyu_utf8.txt'
        self.solitaire_list = []

    def set_idiom_df(self, encoding_type='utf-8'):
        """
        创建DataFrame对象，该对象存储了格式化的成语及拼音信息
        :param encoding_type: 通过encoding_type方式打开
        :return: None
        """

        # l是用来保存列表的列表，每个小列表中包含三个元素[<成语>,<成语首字拼音>,<成语末字拼音>]
        l = []
        p = Pinyin()
        with open(self.file_path + self.file_name, 'r', encoding=encoding_type) as raw_txt:
            for line in raw_txt:
                # 去掉前后空格
                normal_line = line.strip()
                # 转换为[成语,拼音]列表
                normal_list = normal_line.split(" ==> ")
                # 得到对应成语的无音节发音
                pron = p.get_pinyin(normal_list[0], ' ').split(' ')
                l.append([normal_list[0], pron[0], pron[-1]])
        # 创建DataFrame对象
        self.df = pd.DataFrame(l, columns=['idiom', 'first', 'last'])

    def set_solitaire_list(self, first_idiom, solitaire_time=10):
        """
        获取成语接龙后的结果，可指定第一个成语和接龙次数
        :param first_idiom: 第一个成语
        :param solitaire_time: 成语接龙次数（不包含第一个成语）
        :return: None
        """

        p = Pinyin()
        pron = p.get_pinyin(first_idiom, ' ').split(' ')
        first_pinyin = ''
        last_pinyin = pron[-1]

        # 结果列表
        self.solitaire_list = [first_idiom]

        # 深复制DataFrame，保证成语集的完整性
        tmp_df = copy.deepcopy(self.df)

        for i in range(solitaire_time):
            # 更新当前接龙单词的首字拼音
            first_pinyin = last_pinyin
            # 在满足要求的成语中随机选择一个
            indexs = tmp_df[tmp_df['first'] == first_pinyin]['idiom'].index
            if not indexs:
                self.solitaire_list.append('接龙完成')
                break
            index = random.choice(indexs)
            # 获取当前单词
            idiom = tmp_df[index:index + 1]['idiom'].values[0]
            # 更新当前单词的末字拼音
            last_pinyin = tmp_df[index:index + 1]['last'].values[0]
            # 将成语添加到结果列表中
            self.solitaire_list.append(idiom)
            # 删除暂存的DataFrame中的项
            tmp_df.drop(index)

    def show_solitaire_list(self):
        """
        打印接龙结果
        :return: None
        """

        print(f"共接龙{len(self.solitaire_list) - 1}次，接龙次序如下：\n")

        for idiom in self.solitaire_list:
            print(f"{idiom}", end="")
            if idiom != self.solitaire_list[-1]:
                print('---->', end="")

    def get_solitaire_list(self):
        return self.solitaire_list.copy()
