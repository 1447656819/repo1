"""固定文件名
存储所有的测试夹具
"""
import pytest
from config.config import WAIT_TIME
from data.login_data import login_success
from middle_ware.pages.login import LoginPage


@pytest.fixture(scope="class")
def driver():
    """管理浏览器"""
    #前置条件
    #打开浏览器
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(WAIT_TIME)

    #返回前置中的driver参数
    yield driver

    #后置条件
    driver.quit()

@pytest.fixture()
def login(driver):
    """登录"""
    user_info = login_success[0]
    LoginPage(driver).get().login_success(
        username=user_info["username"],
        password=user_info["password"]
    )
    yield driver