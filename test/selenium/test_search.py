from selenium import webdriver
from selenium.webdriver.common.by import By


class TestSearch:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_search(self):
        self.driver.get("https://www.lagou.com/")
        self.driver.find_element(By.ID,"search_input").send_keys("华为")
        self.driver.find_element(By.ID, "search_button").clear()
        ele = self.driver.find_element(By.CSS_SELECTOR,".cl-right-top__1cCMk h3")
        print(ele.text)