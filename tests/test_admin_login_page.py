from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.AdminPage import AdminPage


def test_catalog_accessible_name(browser):
    path = 'admin/'
    browser.get(browser.current_url + path)
    WebDriverWait(browser, 3).until(EC.url_contains(browser.current_url))
    username_form = browser.find_element(By.CSS_SELECTOR, "#input-username")
    assert username_form.accessible_name == "Username"


def test_catalog_accessible_password(browser):
    path = 'admin/'
    browser.get(browser.current_url + path)
    password_form = browser.find_element(By.CSS_SELECTOR, "#input-password")
    assert password_form.accessible_name == "Password"


def test_button_login(browser):
    path = 'admin/'
    browser.get(browser.current_url + path)
    button = browser.find_element(By.CSS_SELECTOR, "button")
    assert button.aria_role == "button"


def test_header(browser):
    path = 'admin/'
    browser.get(browser.current_url + path)
    header = browser.find_element(By.CSS_SELECTOR, 'h1.panel-title')
    assert header.text == "Please enter your login details."


def test_link_forgot(browser):
    path = 'admin/'
    browser.get(browser.current_url + path)
    link_forgot = browser.find_element(By.XPATH, '//span[@class="help-block"]/*')
    assert link_forgot.get_attribute('href') == browser.current_url + "index.php?route=common/forgotten"


def test_add_and_delet_product(browser):
    path = 'admin/'
    browser.get(browser.current_url + path)
    AdminPage.login(browser)
    AdminPage.go_to_products(browser)
    old = len(browser.find_elements(By.XPATH, '//tbody/tr'))
    AdminPage.add_product(browser)
    new = len(browser.find_elements(By.XPATH, '//tbody/tr'))
    AdminPage.delet_product(browser)
    after_delet = len(browser.find_elements(By.XPATH, '//tbody/tr'))
    assert old < new
    assert old == after_delet
