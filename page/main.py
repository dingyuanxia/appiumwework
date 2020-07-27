from time import sleep

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

from appiumwework.page.addmember import AddMember2
from appiumwework.page.base_page import BasePage


class Main(BasePage):
    def goto_contact(self):
        #点击通讯录
        self.find(By.XPATH, "//*[@text='通讯录']").click()
        sleep(2)
        size = self._driver.get_window_size()
        print(size)
        # 屏幕的宽度 width
        x = size['width']
        # 屏幕的高度 height
        y = size['height']
        x1 = int(x * 0.5)
        y1 = int(y * 0.1)
        y2 = int(y * 0.9)
        for i in range(1, 5):
            TouchAction(self._driver).press(x=x1, y=y2).move_to(x=x1, y=y1).release().perform()
        return AddMember2(self._driver)