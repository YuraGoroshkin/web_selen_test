from pages.Application import Application
from selenium.webdriver.common.by import By
from faker import Faker
import allure
fake = Faker()


class ProductCardPage(Application):
    @allure.step('Выбрать  макбук')
    def go_to_mac(self):
        mac_book = self.find_element(By.CSS_SELECTOR, ".image")
        mac_book.click()

    @allure.step('Проверка цены')
    def mac_book_price(self):
        return self.find_element(By.XPATH, '//*[@id="content"]/div/div[2]/ul[2]/li[1]/h2')

    @allure.step('Проверка картинки на превью')
    def find_title_picture(self):
        return self.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/ul[1]/li[1]/a')

    @allure.step('Проверка описания')
    def find_description(self):
        return self.find_element(By.CSS_SELECTOR, "li.active")

    @allure.step('Переход на specification')
    def go_to_specification(self):
        specification = self.find_element(By.CSS_SELECTOR, 'a[href = "#tab-specification"]')
        specification.click()
        return self.find_element(By.CSS_SELECTOR, "td strong")

    @allure.step('Переход на reviews forms')
    def go_to_reviews_forms(self):
        self.find_element(By.CSS_SELECTOR, 'a[href = "#tab-review"]').click()
        return len(self.find_elements(By.XPATH, '//div[@class="form-group required"]/*'))