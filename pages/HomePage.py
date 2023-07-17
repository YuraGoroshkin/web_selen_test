from selenium.webdriver.common.by import By
from pages.Application import Application
import allure


class HomePage(Application):
    @allure.step('Переход на главную')
    def go_to_site(self):
        return self.driver.get(self.base_url)

    @allure.step('Изменение валюты из выпадающего меню')
    def change_currency(self, num):
        self.find_element(By.CSS_SELECTOR,  'i[class="fa fa-caret-down"]').click()
        # евро = 0 / стерлинг = 1 / доллар = 2
        self.find_elements(By.XPATH, '//*[@id="form-currency"]/div/ul/li')[num].click()

    @allure.step('Проверка логотипа')
    def find_logo(self):
        return self.find_element(By.CSS_SELECTOR, "#logo")

    @allure.step('Количество featured')
    def count_featured(self):
        return len(self.find_elements(By.CSS_SELECTOR, ".image"))

    @allure.step('Количество carousel нижнего элемента')
    def count_carousel_bottom(self):
        return len(self.find_elements(By.XPATH, '//div[@class="swiper-pagination carousel0 swiper-pagination-clickable swiper-pagination-bullets"]/*'))

    @allure.step('Количество carousel верхнего элемента')
    def count_carousel_top(self):
        return len(self.find_elements(By.XPATH, '//div[@class="swiper-pagination slideshow0 swiper-pagination-clickable swiper-pagination-bullets"]/*'))

    @allure.step('Проверка текста Featured')
    def get_featured(self):
        return self.find_elements(By.XPATH, '//*[@id="content"]/h3')

    @allure.step('Проверка валюты')
    def get_valuta_in_price(self):
        return self.find_elements(By.CSS_SELECTOR, 'p[class="price"]')[0].text