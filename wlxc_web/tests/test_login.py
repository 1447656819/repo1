"""登录功能的测试"""
from data.login_data import login_error, login_success,login_invalid
from middle_ware.handler import Handler
import pytest
from middle_ware.pages.login import LoginPage


class TestLogin():
    """登录功能的测试类"""

    @pytest.mark.error
    @pytest.mark.parametrize("test_info",login_error)
    def test_login_error(self,test_info,driver):
        """
        1、打开浏览器
        2、访问登录页面
        3、元素定位+元素操作（输入用户名和密码，点击登录）
        4、通过获取页面内容得到实际结果进行断言
        :return:
        """
        #先初始化页面，测试用到的页面
        login_page = LoginPage(driver)

        #测试步骤,页面行为，PO当中的方法
        actual1 = login_page.get().login_fail(
            username= test_info["username"],
            password= test_info["password"]
        ).get_error_message()[0].get_attribute("textContent")

        actual2  = login_page.get().login_fail(
            username= test_info["username"],
            password= test_info["password"]
        ).get_error_message()[1].get_attribute("textContent")

        #获取实际结果，断言
        # actual1 = login_page.get_error_message()[0].get_attribute("textContent")
        # actual2 = login_page.get_error_message()[1].get_attribute("textContent")
        try:
            assert actual1 == test_info["expected"]["first"]
            assert actual2 == test_info["expected"]["second"]
        except AssertionError as e:
            Handler.logger.error("测试用例不通过")
            raise e

    @pytest.mark.invalid
    @pytest.mark.parametrize("test_info", login_invalid)
    def test_login_invalid(self, test_info, driver):
        """登录未授权"""
        login_page = LoginPage(driver)
        actual = login_page.get().login_fail(
            username=test_info["username"],
            password=test_info["password"]
        ).get_invalid_message()
        try:
            assert actual == test_info["expected"]
        except AssertionError as e:
            Handler.logger.error("测试用例不通过")
            raise e

    @pytest.mark.success
    @pytest.mark.parametrize("test_info",login_success)
    def test_login_success(self,test_info,driver):
        """登录成功用例"""
        # 先初始化页面，测试用到的页面
        login_page = LoginPage(driver)

        # 测试步骤,页面行为，PO当中的方法
        actual = login_page.get().login_success(
            username=test_info["username"],
            password=test_info["password"]
        ).get_account_name()

        #断言
        # actual = index_page.get_account_name()
        try:
            assert test_info["expected"] in actual
        except AssertionError as e:
            Handler.logger.error("测试用例不通过")
            raise e


