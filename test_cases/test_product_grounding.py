#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:10607
@file: test_product_grounding.py
@time: 2022/10/03
"""
from page_objects.login_page import LoginPage


class TestProductManage:
    def test_product_grounding(self):
        """新增商品"""
        self.login = LoginPage()
        name = self.login.login().goto_goods_shelves().new_goods_shelves().get_product_name()
        assert name == "内裤"

    def test_product_search(self):
        """搜索商品"""
        self.login = LoginPage()
        self.login.login().goto_search_list().search_product_name()


