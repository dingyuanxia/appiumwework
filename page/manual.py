from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from appiumwework.page.base_page import BasePage



class Manual1(BasePage):
    def manual_input(self):
        from appiumwework.page.memberinfo import MemberInfo
        #点击手动输入添加
        self.find(By.XPATH, "//*[@text='手动输入添加']").click()
        return MemberInfo(self._driver)

    def get_toast(self):
        sleep(3)
        toast_text = self.find(By.XPATH, "//*[@class='android.widget.Toast']").text
        print(toast_text)
        return toast_text

    def back_button(self):
        #点击返回按钮
        #self.find(By.ID, "com.tencent.wework:id/gv3").click()
        locator = (By.ID, 'com.tencent.wework:id/gv3')
        WebDriverWait(self._driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        self.find(locator).click()
        from appiumwework.page.addmember import AddMember2
        return AddMember2(self._driver)

