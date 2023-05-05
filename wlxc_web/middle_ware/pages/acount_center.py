class AccountCenter:

    def __init__(self,driver):
        self.driver = driver

    def get_account_name(self):
        """获取用户名"""
        el = self.driver.find_element_by_path('//a[@href="/account/center"]')