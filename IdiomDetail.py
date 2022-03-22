# -*- coding: UTF-8 -*-
import urllib.request

from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
from urllib.error import HTTPError
from urllib.parse import urlencode


class IdiomDetail:
    """
    通过爬虫获取成语释义的类，提供相关接口
    """

    def __init__(self):
        # 请求头
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/99.0.4844.74 Safari/537.36"
        }

    def get_url(self, idiom):
        """
        返回带成语的URL
        :param idiom: 成语
        :return: 带成语的URL
        """

        wd = {'q': idiom}
        return 'https://www.123cha.com/chengyu/?' + urlencode(wd)

    def get_bs(self, url):
        """
        获取成语对应百度百科的BeautifulSoup对象
        :param url: 访问的URL
        :return: 访问出错返回None，正常访问返回BeautifulSoup对象
        """

        try:
            req = Request(url=url, headers=self.headers, method='GET')
            html = urlopen(req)
        except HTTPError as e:
            print(e.reason)
        else:
            bs = BeautifulSoup(html.read(), 'html.parser')
            return bs

    def get_content(self, bs):
        """
        获取成语释义
        :param bs: 成语对应的BeautifulSoup对象
        :return: 成语释义的字符串
        """
        # 基于网页源代码结构找到成语释义
        if bs is not None:
            try:
                # 获取释义
                content1 = bs.findAll('td', {'align': 'left'})[2].string
                # 获取来源
                content2 = bs.findAll('td', {'align': 'left'})[3].string
                # 首行缩进2ch
                content1 = "    " + content1
                # 补句号
                if not content1.endswith('。'):
                    content1 = content1 + '。'
                return content1 + content2
            except IndexError:
                return '未查询到成语释义'
            except TypeError:
                return '未查询到成语释义'
        else:
            return '未查询到成语释义'
