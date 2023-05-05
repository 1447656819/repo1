import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from common.selenium_handler import BasePage
from middle_ware.handler import Handler
from middle_ware.pages.assistance import AssistancePage


class IndexPage(BasePage):

    title  ="个人设置"

    URL = Handler.yaml["host"] + "/account/center"

    #获取用户信息
    user_locator = (By.XPATH,"//span[@class='action ant-dropdown-link user-dropdown-menu ant-dropdown-trigger']/span[2]")
    #点击服务
    serve_locator = (By.XPATH,'//i[@class="anticon anticon-solution"]/../span')
    #点击社会救助
    assistance_locator = (By.XPATH,'//li[@class="ant-menu-item"]/a[@href="/village/assistance"]')

    def get(self):
        self.driver.get(self.URL)
        return self



    def get_account_name(self):
        """获取用户名"""
        return self.driver.find_element(*self.user_locator).text

    def click_assistance_btn(self):
        """点击社会救助"""
        #点击服务
        self.driver.find_element(*self.serve_locator).click()
        time.sleep(1)
        #点击社会救助
        self.driver.find_element(*self.assistance_locator).click()
        time.sleep(3)

        return AssistancePage(self.driver)
