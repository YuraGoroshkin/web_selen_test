from pages.Application import Application
from selenium.webdriver.common.by import By
from faker import Faker

fake = Faker()


class ProductCardPage(Application):
    def go_to_mac(self):
        mac_book = self.find_element(By.CSS_SELECTOR, ".image")
        mac_book.click()

    def mac_book_price(self):
        return self.find_element(By.XPATH, '//*[@id="content"]/div/div[2]/ul[2]/li[1]/h2')

    def find_title_picture(self):
        return self.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/ul[1]/li[1]/a')

    def find_description(self):
        return self.find_element(By.CSS_SELECTOR, "li.active")

    def go_to_specification(self):
        specification = self.find_element(By.CSS_SELECTOR, 'a[href = "#tab-specification"]')
        specification.click()
        return self.find_element(By.CSS_SELECTOR, "td strong")

    def go_to_reviews_forms(self):
        self.find_element(By.CSS_SELECTOR, 'a[href = "#tab-review"]').click()
        return len(self.find_elements(By.XPATH, '//div[@class="form-group required"]/*'))