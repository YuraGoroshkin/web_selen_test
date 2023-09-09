from pages.Application import Application
from selenium.webdriver.common.by import By
import allure


class CatalogPage(Application):
    @allure.step('Переход с главной страницы в каталог Phones & PDAs')
    def go_to_phone(self):
        catalog_via_phones = self.find_element(By.CSS_SELECTOR, "li:nth-child(6)")
        catalog_via_phones.click()

    @allure.step('Подсчёт выставленных телефонов')
    def count_the_numbers_phones(self):
        return len(self.find_elements(By.XPATH, '// *[ @ id = "content"] / div[2]/*'))

    @allure.step('Переход из каталога Phones & PDAs в Desktops')
    def flip_to_desktops(self):
        bookmark = CatalogPage.find_all_bookmarks(self)
        bookmark[0].click()
        name_catalog = self.find_elements(By.XPATH, '// *[ @ id = "content"] / h2')
        return name_catalog

    @allure.step('Переход из каталога Phones & PDAs в Laptops and Notebooks')
    def flip_to_laptops_and_notebooks(self):
        bookmark = CatalogPage.find_all_bookmarks(self)
        bookmark[1].click()
        name_catalog = self.find_elements(By.XPATH, '// *[ @ id = "content"] / h2')
        return name_catalog

    @allure.step('Переход из каталога Phones & PDAs в Components')
    def flip_to_components(self):
        bookmark = CatalogPage.find_all_bookmarks(self)
        bookmark[2].click()
        name_catalog = self.find_elements(By.XPATH, '// *[ @ id = "content"] / h2')
        return name_catalog

    @allure.step('Переход из каталога Phones & PDAs в Tablets')
    def flip_to_tablets(self):
        bookmark = CatalogPage.find_all_bookmarks(self)
        bookmark[3].click()
        name_catalog = self.find_elements(By.XPATH, '// *[ @ id = "content"] / h2')
        return name_catalog

    @allure.step('Переход из каталога Phones & PDAs в Software')
    def flip_to_software(self):
        bookmark = CatalogPage.find_all_bookmarks(self)
        bookmark[4].click()
        name_catalog = self.find_elements(By.XPATH, '// *[ @ id = "content"] / h2')
        return name_catalog

    @allure.step('Переход из каталога Phones & PDAs в Cameras')
    def flip_to_cameras(self):
        bookmark = CatalogPage.find_all_bookmarks(self)
        bookmark[6].click()
        name_catalog = self.find_elements(By.XPATH, '// *[ @ id = "content"] / h2')
        return name_catalog

    @allure.step('Переход из каталога Phones & PDAs в mp3 players')
    def flip_to_mp3_players(self):
        bookmark = CatalogPage.find_all_bookmarks(self)
        bookmark[7].click()
        name_catalog = self.find_elements(By.XPATH, '// *[ @ id = "content"] / h2')
        return name_catalog

    @allure.step('Выбрать весь список категорий')
    def find_all_bookmarks(self):
        return self.find_elements(By.CSS_SELECTOR, "a.list-group-item")
