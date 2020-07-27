import time

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

from appiumwework.page.base_page import BasePage


class DelMem(BasePage):
    def del_mem(self):
        time.sleep(2)
        wind_size = self._driver.get_window_size()
        width = wind_size['width']
        height = wind_size['height']
        x = int(width * 0.5)
        y_end = int(height * 0.1)
        y_start = int(height * 0.9)
        TouchAction(self._driver).press(x=x, y=y_start).wait(100).move_to(x=x, y=y_end).release().perform()
        # 点击删除成员
        self.find(By.ID, "com.tencent.wework:id/dve").click()
        # 点击确定删除按钮
        self.find(By.ID, "com.tencent.wework:id/b_a").click()


