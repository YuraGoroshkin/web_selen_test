from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver, request):
        self.driver = driver
        self.base_url = request.config.getoption("--url")

    def find_element(self, locator, time=20):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=20):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def change_currency(self, num):
        self.find_element(By.CSS_SELECTOR,  'i[class="fa fa-caret-down"]').click()
        # евро = 0 / стерлинг = 1 / доллар = 2
        self.find_elements(By.XPATH, '//*[@id="form-currency"]/div/ul/li')[num].click()