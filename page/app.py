from appium import webdriver

from appiumwework.page.base_page import BasePage
from appiumwework.page.main import Main


class App(BasePage):
    def start_app(self):
        if self._driver == None:
            desired_caps = {}
            desired_caps["platformName"] = 'Android'
            desired_caps['platformVersion'] = '7.0'
            desired_caps['deviceName'] = 'emulator-5554'
            desired_caps['appPackage'] = 'com.tencent.wework'
            desired_caps['appActivity'] = '.launch.LaunchSplashActivity'
            desired_caps['noReset'] = 'true'
            desired_caps['skipDeviceInitialization'] = 'true'
            # desired_caps['unicodeKeyBoard'] = 'true'
            # desired_caps['resetKeyboard'] = 'true'
            desired_caps['skipServerInstallation'] = True
            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)


        else:
            self._driver.launch_app()

        self._driver.implicitly_wait(10)
        return self

    def restart_app(self):
        pass

    def stop_app(self):
        pass

    def main(self) -> Main:
        return Main(self._driver)
