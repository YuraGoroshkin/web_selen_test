from pages.HomePage import HomePage
from selenium.webdriver.common.by import By


class AdminPage(HomePage):

    def login(self):
        self.find_element(By.CSS_SELECTOR, "#input-username").click()
        self.find_element(By.CSS_SELECTOR, "#input-username").send_keys('user')
        self.find_element(By.CSS_SELECTOR, "#input-password").click()
        self.find_element(By.CSS_SELECTOR, "#input-password").send_keys('bitnami')
        self.find_element(By.XPATH, "//button").click()

