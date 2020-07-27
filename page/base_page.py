from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BasePage:
    _black_list = [
        (By.XPATH, "//*[@text='确认']"),
        (By.XPATH, "//*[@text='下次再说']"),
        (By.XPATH, "//*[@text='确定']"),
    ]
    _err_num = 0
    _max_num = 3

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def find(self, locator, value: str = None):
        element: WebElement
        try:
            if isinstance(locator, tuple):
                element = self._driver.find_element(*locator)
            else:
                element = self._driver.find_element(locator, value)
            self._driver.implicitly_wait(10)
            self._err_num = 0
            return element

        except Exception as e:
            self._driver.implicitly_wait(1)
            if self._err_num > self._max_num:
                raise e
            self._err_num += 1
            for ele in self._black_list:
                # 定位弹框元素
                elelist = self._driver.find_elements(*ele)
                print(elelist)
                if len(elelist) > 0:
                    elelist[0].click()
                    return self.find(locator, value)
        raise e

    def scroll_find(self, value):
        return self._driver.find_element_by_android_uiautomator(
            f'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text(' + '"' + value + '"' + ').instance(0));')
