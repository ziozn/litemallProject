#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:10607
@file: login_page.py
@time: 2022/10/03
"""
from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage
from page_objects.index_page import IndexPage


class LoginPage(BasePage):
    _INPUT_USERNAME = (By.XPATH, "//*[@name='username']")
    _INPUT_PASSWORD = (By.XPATH, "//*[@name='password']")
    _LOGIN_BUTTON = (By.CSS_SELECTOR, "button.el-button")

    def login(self):
        """
        输入 [用户名]
        输入 [密码]
        点击 [登录]
        :return: Index_Page
        """
        self.do_clear_send_keys("admin123", *self._INPUT_USERNAME)
        self.do_clear_send_keys("admin123", *self._INPUT_PASSWORD)
        self.do_click(*self._LOGIN_BUTTON)
        return IndexPage(self.driver)
