#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:10607
@file: index_page.py
@time: 2022/10/03
"""
from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage
from page_objects.goods_list_page import GoodsListPage
from page_objects.goods_shelves_page import GoodsShelvesPage


class IndexPage(BasePage):
    _MENU_COMMODITY_MANAGEMENT = (By.XPATH, "//span[contains(text(), '商品管理')]")
    _MENU_GOODS_SHELVES = (By.XPATH, "//span[contains(text(), '商品上架')]")
    _MENU_GOODS_LIST = (By.XPATH, "//span[contains(text(), '商品列表')]")

    def goto_goods_shelves(self):
        """
        点击 [商品管理]
        点击 [商品上架]
        :return:商品上架页
        """
        self.do_click(*self._MENU_COMMODITY_MANAGEMENT)
        self.do_click(*self._MENU_GOODS_SHELVES)
        return GoodsShelvesPage(self.driver)

    def goto_search_list(self):
        """
        点击 [商品管理]
        点击 [商品列表]
        :return:商品列表页
        """
        self.do_click(*self._MENU_COMMODITY_MANAGEMENT)
        self.do_click(*self._MENU_GOODS_LIST)
        return GoodsListPage(self.driver)




