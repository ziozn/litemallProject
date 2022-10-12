#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:10607
@file: base_page.py 基类
@time: 2022/10/03
"""
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    _BASE_URL = "https://litemall.hogwarts.ceshiren.com/"
    def __init__(self, driver:WebDriver = None):
        if driver is None:
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(10)
            self.driver.maximize_window()
            # 打开litemall网站
            self.driver.get(self._BASE_URL)
        else:
            # 复用driver
            self.driver = driver

    def do_click(self, by:By, locator:str):
        """查找并点击元素"""
        self.driver.find_element(by, locator).click()

    def do_send_keys(self, value, by:By, locator:str):
        """查找并输入元素"""
        self.driver.find_element(by, locator).send_keys(value)

    def do_clear_send_keys(self, value, by:By, locator:str):
        """先清空再输入元素"""
        element = self.driver.find_element(by, locator)
        element.clear()
        element.send_keys(value)

    def script_slide_base(self):
        """使用JS滑动到底部"""
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    def get_element_text(self, element):
        """获取元素的文本"""
        elm = WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(element))
        return elm.text

