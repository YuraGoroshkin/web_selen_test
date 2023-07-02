from pages.HomePage import HomePage
from selenium.webdriver.common.by import By
from faker import Faker

fake = Faker()


class RegistrationPage(HomePage):

    def fill_personal(self):
        self.find_element(By.CSS_SELECTOR, 'input[id = "input-firstname"]').send_keys('Test')
        self.find_element(By.CSS_SELECTOR, 'input[id = "input-lastname"]').send_keys('Test')
        email = RegistrationPage.random_email(self)
        self.find_element(By.CSS_SELECTOR, 'input[id = "input-email"]').send_keys(email)
        self.find_element(By.CSS_SELECTOR, 'input[id = "input-telephone"]').send_keys('88005553225')
        self.find_element(By.CSS_SELECTOR, 'input[id = "input-password"]').send_keys('12345678')
        self.find_element(By.CSS_SELECTOR, 'input[id = "input-confirm"]').send_keys('12345678')
        self.find_element(By.CSS_SELECTOR, 'input[name="agree"]').click()
        self.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()
        pass

    def random_email(self):
        first_name = (fake.name()).replace(' ', '')
        return first_name.lower() + '@' + fake.domain_name()