#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:10607
@file: goods_shelves_page.py
@time: 2022/10/03
"""
from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage
from page_objects.goods_list_page import GoodsListPage


class GoodsShelvesPage(BasePage):
    _INPUT_GOODS_NUM = (By.XPATH, "//label[@for='goodsSn']/../div/div/input")
    _INPUT_GOODS_NAME = (By.XPATH, "//label[@for='name']/../div/div/input")
    _INPUT_GOODS_PRICE = (By.XPATH, "//label[@for='counterPrice']/../div/div/input")
    _RADIO_HOT = (By.XPATH, "//span[contains(text(), '热卖')]")
    _BNT_GOUNDING = (By.XPATH, "//div[@class='app-container']//span[text()='上架']")

    def new_goods_shelves(self):
        """
        输入 【商品编号】
        输入 【商品名称】
        输入 【商品价格】
        选择 【热卖】 按钮
        滑动
        点击 【上架】 按钮
        :return: 商品列表页
        """
        self.do_send_keys("122222", *self._INPUT_GOODS_NUM)
        self.do_send_keys('内裤', *self._INPUT_GOODS_NAME)
        self.do_send_keys("50", *self._INPUT_GOODS_PRICE)
        self.do_click(*self._RADIO_HOT)
        self.script_slide_base()
        self.do_click(*self._BNT_GOUNDING)
        return GoodsListPage(self.driver)

