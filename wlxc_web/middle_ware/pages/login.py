"""登录页面"""
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from common.selenium_handler import BasePage
from middle_ware.pages.index import IndexPage
from middle_ware.handler import Handler
from selenium.webdriver.common.by import By

class LoginPage(BasePage):

    title = "未来乡村管理平台"

    URL = Handler.yaml["host"] + "/user/login"

    #locator
    login_button_btn = (By.CSS_SELECTOR,"[class = 'login-button ant-btn ant-btn-primary ant-btn-lg']")
    error_msg_locator = (By.CLASS_NAME,"ant-form-explain")

    #没有通过授权的定位方式
    invalid_msg_locator = (By.CLASS_NAME,"ant-notification-notice-description")


    def get(self):
        """访问页面"""
        self.driver.get(self.URL)
        return self


    def login_fail(self,username,password):

        # 输入用户名，密码提交
        self.driver.find_element_by_id("username").send_keys(username)
        self.driver.find_element_by_id("password").send_keys(password)
        self.driver.find_element(*self.login_button_btn).click()
        return self

    def login_success(self,username,password):

        # 输入用户名，密码提交
        self.driver.find_element_by_id("username").send_keys(username)
        self.driver.find_element_by_id("password").send_keys(password)
        self.driver.find_element(*self.login_button_btn).click()
        return IndexPage(self.driver)

    def get_error_message(self):

        """获取登录不成功的错误信息"""
        return self.driver.find_elements(*self.error_msg_locator)

    def get_invalid_message(self):
        """获取登录未授权的信息

        注意事项：通过隐式等待是可以等待元素被加载。
        但是并不代表里面的动态文本能被获取到，因为一般的动态页面，会先去获取它的属性值而不是文本信息
        1、通过显示等待：visible
        2、text文本定位，显示等待
        3、强制等待，把握好时间（因为是动态的）
        """
        #显示等待进行元素定位
        el = self.wait_element_visible(self.invalid_msg_locator)
        return el.text





