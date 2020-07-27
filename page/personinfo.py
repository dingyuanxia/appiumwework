from selenium.webdriver.common.by import By

from appiumwework.page.base_page import BasePage
from appiumwework.page.editormember import EditorMember


class PersonInfo(BasePage):
    def person_info(self):
        #点击三个按钮
        self.find(By.ID, "com.tencent.wework:id/gvd").click()
        return EditorMember(self._driver)