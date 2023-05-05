"""社会救助"""
import pytest

from middle_ware.pages.index import IndexPage

@pytest.mark.inquire
def test_assistance_inquire(login):
    """
    页面查询
    测试步骤：
        1、前置条件：登录
        2、首页：点击服务，点击社会救助
        3、救助详情页,输入查询数据，
        4、救助详情页，点击查询按钮，获取结果

    :return:
    """
    drive = login
    actual = IndexPage(drive).click_assistance_btn().write("测试").putdomn_button().get_page_number()

    #断言
    assert actual == '1'



