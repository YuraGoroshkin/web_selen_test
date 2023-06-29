from pages.HomePage import HomePage
from selenium.webdriver.common.by import By


class AdminPage(HomePage):

    def login(self):
        self.find_element(By.CSS_SELECTOR, "#input-password")
        user = self.find_element(By.CSS_SELECTOR, "#input-username")
        user.click()
