from pages.Application import Application
from selenium.webdriver.common.by import By
from faker import Faker
import allure
fake = Faker()


class RegistrationPage(Application):
    @allure.step('Регистрация нового пользователя')
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

    @allure.step('Генерация email')
    def random_email(self):
        first_name = (fake.name()).replace(' ', '')
        return first_name.lower() + '@' + fake.domain_name()

    @allure.step('Проверка header')
    def find_header(self):
        return self.find_element(By.XPATH, '//*[@id="content"]/h1')

    @allure.step('Проверка полей account form ')
    def find_account_form(self):
        return self.find_element(By.CSS_SELECTOR, 'fieldset#account')

    @allure.step('Проверка полей account form password')
    def find_account_form_password(self):
        return self.find_element(By.CSS_SELECTOR, 'fieldset:nth-of-type(2)')

    @allure.step('Проверка radio button YES/NO')
    def find_radio_button(self):
        return self.find_elements(By.XPATH, '//div[@class="col-sm-10"]/label')

    @allure.step('Проверка continue button')
    def find_continue_button(self):
        return self.find_element(By.XPATH, '//input[@value="Continue"]')

    @allure.step('Проверка сообщения - Your Account Has Been Created!')
    def notification_check(self):
        return self.find_element(By.XPATH, '//div/h1').text
