# -*- coding: UTF-8 -*-

import IdiomSet
import Drawer

if __name__ == '__main__':
    # 创建成语集对象
    idiom_set = IdiomSet.IdiomSet()
    # 设置成语集对象中的格式化数据（导入chengyu_utf8.txt后转化而得）
    idiom_set.set_idiom_df()

    # 第一个成语
    first_idiom = '侯阳洋'
    # 接龙次数
    solitaire_time = 10

    # 进行成语接龙，将接龙结果保存到了成语集对象的solitaire_set列表中
    idiom_set.set_solitaire_list(first_idiom, solitaire_time)

    # 输出接龙结果
    idiom_set.show_solitaire_list()

    # 获取接龙结果
    res_list = idiom_set.get_solitaire_list()

