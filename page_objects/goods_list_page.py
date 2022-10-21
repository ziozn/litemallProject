#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:10607
@file: goods_shelves_page.py
@time: 2022/10/03
"""
from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class GoodsListPage(BasePage):
    _TEXT_PRODUCT_NAME = (By.XPATH, "//tbody/tr[1]/td[3]/div")
    _TEXT_PRODUCT_SEARCH_NAME = (By.XPATH, "//div[@class='filter-container']/div[3]/input")
    _BUTTON_PRODUCT_NAME = (By.XPATH, "//span[contains(text(), '查找')]")

    def get_product_name(self):
        """获取商品名称"""
        return self.get_element_text(self._TEXT_PRODUCT_NAME)

    def search_product_name(self):
        """搜索商品名称"""
        self.do_send_keys("AD钙奶", *self._TEXT_PRODUCT_SEARCH_NAME)
        self.do_click(*self._BUTTON_PRODUCT_NAME)
