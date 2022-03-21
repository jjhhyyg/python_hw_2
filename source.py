# -*- coding: UTF-8 -*-

import pandas as pd
import codecs
from xpinyin import Pinyin


file_path = ''
file_name = 'chengyu_utf8.txt'


def get_idiom_pron_set(txt_path, txt_name, encoding_type='utf-8'):
    # dict的键为成语，值为(begin_pron,end_pron)形式，分别是首字的拼音和末字的拼音（无音节）
    dict = {}
    p = Pinyin()
    with codecs.open(txt_path + txt_name, 'r', encoding=encoding_type) as raw_txt:
        for line in raw_txt:
            # 去掉前后空格
            normal_line = line.strip()
            # 转换为[成语,拼音]列表
            normal_list = normal_line.split(" ==> ")
            # 得到对应成语的无音节发音
            pron = p.get_pinyin(normal_list[0], ' ').split(' ')
            dict[normal_list[0]] = (pron[0],pron[-1])
    return dict


if __name__ == '__main__':
    dict = get_idiom_pron_set(file_path,file_name)
    for key,value in dict.items():
        print(f"{key}: {value}")
