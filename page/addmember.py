import time

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from appiumwework.page.base_page import BasePage
from appiumwework.page.manual import Manual1
from appiumwework.page.personinfo import PersonInfo


class AddMember2(BasePage):
    def add_member(self):
        # 点击添加成员
        locator = (By.XPATH, "//*[@text='添加成员']")
        WebDriverWait(self._driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        self.find(By.XPATH, "//*[@text='添加成员']").click()
        return Manual1(self._driver)


    def find_del_mem(self,name):
        #点击要删除的成员
        # locator = (By.XPATH, f"//*[@text='{value}']")
        # WebDriverWait(self._driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        # self.find(locator).click()
        self.scroll_find(name).click()
        return PersonInfo(self._driver)

