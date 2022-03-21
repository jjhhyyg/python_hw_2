# -*- coding: UTF-8 -*-

import pandas as pd
import codecs
from random import choice
from xpinyin import Pinyin

file_path = ''
file_name = 'chengyu_utf8.txt'


def get_idiom_pron_set(txt_path, txt_name, encoding_type='utf-8'):
    # l是用来保存列表的列表，每个小列表中包含三个元素[<成语>,<成语首字拼音>,<成语末字拼音>]
    l = []
    p = Pinyin()
    with codecs.open(txt_path + txt_name, 'r', encoding=encoding_type) as raw_txt:
        for line in raw_txt:
            # 去掉前后空格
            normal_line = line.strip()
            # 转换为[成语,拼音]列表
            normal_list = normal_line.split(" ==> ")
            # 得到对应成语的无音节发音
            pron = p.get_pinyin(normal_list[0], ' ').split(' ')
            l.append([normal_list[0], pron[0], pron[-1]])
    # 创建DataFrame
    df = pd.DataFrame(l, columns=['idiom', 'first', 'last'])
    return df


if __name__ == '__main__':
    df = get_idiom_pron_set(file_path, file_name)
    print(df)

    # 结果列表
    res_list = ['侯阳洋']

    first_word = ''
    last_word = 'yang'

    # 记录接龙次数
    cnt = 0

    # 设置接龙次数
    times = 10

    for i in range(times):
        # 更新当前接龙单词的首字拼音
        first_word = last_word
        # 在满足要求的成语中随机选择一个
        indexs = df[df['first'] == first_word]['idiom'].index
        if indexs is []:
            print('No available idioms!')
            break
        index = choice(indexs)
        # 获取当前单词
        idiom = df[index:index + 1]['idiom'].values[0]
        # 更新当前单词的末字拼音
        last_word = df[index:index + 1]['last'].values[0]
        # 将成语添加到结果列表中
        res_list.append(idiom)
        cnt += 1

    # 输出结果
    print(f"共接龙{cnt}次，接龙次序如下：")

    for idiom in res_list:
        print(f"{idiom}")
        if idiom != res_list[-1]:
            print('|')
            print('↓')
