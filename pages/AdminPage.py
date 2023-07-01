from pages.HomePage import HomePage
from selenium.webdriver.common.by import By
from time import sleep


class AdminPage(HomePage):

    def login(self):
        self.find_element(By.CSS_SELECTOR, "#input-username").click()
        self.find_element(By.CSS_SELECTOR, "#input-username").send_keys('user')
        self.find_element(By.CSS_SELECTOR, "#input-password").click()
        self.find_element(By.CSS_SELECTOR, "#input-password").send_keys('bitnami')
        self.find_element(By.XPATH, "//button").click()

    def open_catalog_list(self):
        self.find_element(By.XPATH, '//*[@id="menu-catalog"]').click()
        elements = self.find_elements(By.XPATH, '//*[@id="collapse1"]/li')
        return elements

    def go_to_products(self):
        a = AdminPage.open_catalog_list(self)
        sleep(1)
        a[1].click()

    def add_product(self):
        self.find_element(By.XPATH, '//i[@class="fa fa-plus"]').click()
        self.find_element(By.XPATH, '//input[@id="input-name1"]').send_keys('Test')
        self.find_element(By.XPATH, '//input[@id="input-meta-title1"]').send_keys('Test')
        self.find_elements(By.CSS_SELECTOR, 'a[data-toggle="tab"]')[1].click()
        self.find_elements(By.CSS_SELECTOR, 'input[id="input-model"]')[0].send_keys('Test')
        self.find_element(By.CSS_SELECTOR, 'button[data-original-title="Save"]').click()
