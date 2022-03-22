# -*- coding: UTF-8 -*-

from IdiomDetail import IdiomDetail

idiom_detail = IdiomDetail()

url = idiom_detail.get_url('叶公好龙')
bs = idiom_detail.get_bs(url)
print(bs)

bs.find()