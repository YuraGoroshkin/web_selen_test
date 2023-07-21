from pages.Application import Application
from selenium.webdriver.common.by import By
from time import sleep
import allure


class AdminPage(Application):

    @allure.step('Авторизовался под администратором сайта')
    def login(self, user, password):
        self.find_element(By.CSS_SELECTOR, "#input-username").click()
        self.find_element(By.CSS_SELECTOR, "#input-username").send_keys(user)
        self.find_element(By.CSS_SELECTOR, "#input-password").click()
        self.find_element(By.CSS_SELECTOR, "#input-password").send_keys(password)
        self.find_element(By.XPATH, "//button").click()

    @allure.step('Раскрыть меню Catalog')
    def open_catalog_list(self):
        self.find_element(By.XPATH, '//*[@id="menu-catalog"]').click()
        elements = self.find_elements(By.XPATH, '//*[@id="collapse1"]/li')
        return elements

    @allure.step('Переход в products')
    def go_to_products(self):
        a = AdminPage.open_catalog_list(self)
        sleep(1)
        a[1].click()

    @allure.step('Добавить продукт')
    def add_product(self):
        self.find_element(By.XPATH, '//i[@class="fa fa-plus"]').click()
        self.find_element(By.XPATH, '//input[@id="input-name1"]').send_keys('Test')
        self.find_element(By.XPATH, '//input[@id="input-meta-title1"]').send_keys('Test')
        self.find_elements(By.CSS_SELECTOR, 'a[data-toggle="tab"]')[1].click()
        self.find_elements(By.CSS_SELECTOR, 'input[id="input-model"]')[0].send_keys('Test')
        self.find_element(By.CSS_SELECTOR, 'button[data-original-title="Save"]').click()

    @allure.step('Удалить продукт')
    def delet_product(self):
        self.find_element(By.XPATH, '//tbody/tr[20]/td/input').click()
        self.find_element(By.CSS_SELECTOR, 'button[class="btn btn-danger"]').click()
        sleep(0.2)
        alert = self.switch_to.alert
        alert.accept()
        sleep(0.1)

    @allure.step('Проверка нахождения поля username')
    def find_username_form(self):
        return self.find_element(By.CSS_SELECTOR, "#input-username")

    @allure.step('Проверка нахождения поля password')
    def find_password_form(self):
        return self.find_element(By.CSS_SELECTOR, "#input-password")

    @allure.step('Проверка нахождения поля кнопки')
    def find_button(self):
        return self.find_element(By.CSS_SELECTOR, "button")

    @allure.step('Проверка нахождения надписи  Please enter your login details.')
    def find_header(self):
        return self.find_element(By.CSS_SELECTOR, 'h1.panel-title')

    @allure.step('Проверка нахождения Forgotten Password link')
    def find_link_forgot(self):
        return self.find_element(By.XPATH, '//span[@class="help-block"]/*')

    @allure.step('Подсчёт всех продуктов')
    def count_the_number_of_products(self):
        return len(self.find_elements(By.XPATH, '//tbody/tr'))