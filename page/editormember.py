from selenium.webdriver.common.by import By

from appiumwework.page.base_page import BasePage
from appiumwework.page.del_mem import DelMem


class EditorMember(BasePage):
    def editor_memmber(self):
        #点击编辑成员
        self.find(By.ID, 'com.tencent.wework:id/azk').click()

        return DelMem(self._driver)
