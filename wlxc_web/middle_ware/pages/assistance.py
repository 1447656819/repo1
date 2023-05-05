"""社会救助"""
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from common.selenium_handler import BasePage
from middle_ware.handler import Handler

class AssistancePage(BasePage):

    title = "社会救助"

    #查询输入框
    inquire_input_locator = (By.ID,'name')
    #查询按钮
    inquire_button_locator = (By.XPATH,'//button[@class = "search-btn ant-btn ant-btn-primary"]')
    #页码
    page_number_locator = (By.XPATH,'//li[@class = "ant-pagination-item ant-pagination-item-1 ant-pagination-item-active"]/a')


    def write(self,data):
        """查询输入框"""
        js = 'document.getElementById("name").autocomplete=false'
        self.driver.execute_script(js)

        self.driver.find_element(*self.inquire_input_locator).send_keys(data)
        action = ActionChains(self.driver)
        action.move_by_offset(1000,250).click().perform()

        return self

    def putdomn_button(self):
        """按下查询按钮"""
        self.driver.find_element(*self.inquire_button_locator).click()
        time.sleep(3)
        return self
    def get_page_number(self):
        """获取页码"""
        el = self.driver.find_element(*self.page_number_locator)
        return el.text


