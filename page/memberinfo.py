from selenium.webdriver.common.by import By

from appiumwework.page.base_page import BasePage


class MemberInfo(BasePage):
    def name_input(self):
        self.find(By.XPATH, "//*[@text='姓名　']/..//*[@text='必填']").send_keys("test33")
        return self

    def phone_numer(self):
        self.find(By.XPATH, "//*[@text='手机号']").send_keys("13831126752")
        return self

    def gender_select(self):
        self.find(By.XPATH, "//*[@text='性别']/..//*[@text='男']").click()
        self.find(By.XPATH, "//*[@text='女']").click()
        return self

    def click_save(self):
        self.find(By.ID, "com.tencent.wework:id/gvk").click()
        from appiumwework.page.manual import Manual1
        return Manual1(self._driver)