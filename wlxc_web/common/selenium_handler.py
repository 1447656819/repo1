"""浏览器的通用操作"""
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    title = None

    def __init__(self,driver):
        self.driver = driver
        # 等待某个页面加载完成，显示等待
        # title_contains:页面标题包含什么内容
        try:
            WebDriverWait(self.driver, 10).until(
                expected_conditions.title_contains(self.title)
            )
        except:
            print("你的操作没有进入对应的页面，可能会引发异常：{}".format(self.title))

    def wait_element_visible(self,locator,timeout=20,poll=0.5):
        """等待某个元素可见
        封装显性等待
        """
        el = WebDriverWait(self.driver,timeout=timeout,poll_frequency=poll).until(
            expected_conditions.visibility_of_element_located(locator)
        )
        return el

    def wait_element_clickable(self,locator,timeout,poll):
        """等待某个元素可以被点击"""
        el = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(
            expected_conditions.element_to_be_clickable(locator)
        )
        return el

    def wait_element_presence(self,locator,timeout,poll):
        """判断某个元素是否被加载出来"""
        el = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(
            expected_conditions.presence_of_element_located(locator)
        )
        return el

    def click(self,locator):
        """点击某个元素"""
        self.wait_element_clickable(locator).click()
        return self

    def write(self,locator,value):
        """输入信息"""
        self.wait_element_presence(locator).send_keys(value)
        return self

    def scoll(self,height=None,width=None):
        """窗口滚动"""
        if not height:
            height = 0
        if not width:
            width = 0
        js_code = "window.scrollTo({},{});".format(height,width)
        self.driver.execute_script(js_code)
        return self

    def move_to(self,locator):
        """移动到某个元素"""
        el = self.driver.find_element(*locator)
        ActionChains(self.driver).move_to_element(el).perform()
        return self

    def switch_iframe(self,locator,timeout):
        """切换到iframe"""
        WebDriverWait(self.driver,timeout=timeout).until(
            expected_conditions.frame_to_be_available_and_switch_to_it(locator)
        )
        return self

