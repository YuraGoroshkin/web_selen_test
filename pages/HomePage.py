from selenium.webdriver.common.by import By
from pages.Application import Application


class HomePage(Application):

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def change_currency(self, num):
        self.find_element(By.CSS_SELECTOR,  'i[class="fa fa-caret-down"]').click()
        # евро = 0 / стерлинг = 1 / доллар = 2
        self.find_elements(By.XPATH, '//*[@id="form-currency"]/div/ul/li')[num].click()

    def find_logo(self):
        return self.find_element(By.CSS_SELECTOR, "#logo")

    def count_featured(self):
        return len(self.find_elements(By.CSS_SELECTOR, ".image"))

    def count_carousel_bottom(self):
        return len(self.find_elements(By.XPATH, '//div[@class="swiper-pagination carousel0 swiper-pagination-clickable swiper-pagination-bullets"]/*'))

    def count_carousel_top(self):
        return len(self.find_elements(By.XPATH, '//div[@class="swiper-pagination slideshow0 swiper-pagination-clickable swiper-pagination-bullets"]/*'))

    def get_featured(self):
        return self.find_elements(By.XPATH, '//*[@id="content"]/h3')

    def get_valuta_in_price(self):
        return self.find_elements(By.CSS_SELECTOR, 'p[class="price"]')[0].text