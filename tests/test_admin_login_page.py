from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.AdminPage import AdminPage


def test_catalog_accessible_name(browser):
    browser.get('http://192.168.31.208:8081/admin/')
    WebDriverWait(browser, 3).until(EC.url_contains("http://192.168.31.208:8081/admin/"))
    username_form = browser.find_element(By.CSS_SELECTOR, "#input-username")
    AdminPage.login(browser)
    assert username_form.accessible_name == "Username"


def test_catalog_accessible_password(browser):
    browser.get('http://192.168.31.208:8081/admin/')
    password_form = browser.find_element(By.CSS_SELECTOR, "#input-password")
    assert password_form.accessible_name == "Password"


def test_button_login(browser):
    browser.get('http://192.168.31.208:8081/admin/')
    button = browser.find_element(By.CSS_SELECTOR, "button")
    assert button.aria_role == "button"


def test_header(browser):
    browser.get('http://192.168.31.208:8081/admin/')
    header = browser.find_element(By.CSS_SELECTOR, 'h1.panel-title')
    assert header.text == "Please enter your login details."


def test_link_forgot(browser):
    browser.get('http://192.168.31.208:8081/admin/')
    link_forgot = browser.find_element(By.XPATH, '//span[@class="help-block"]/*')
    assert link_forgot.get_attribute('href') == "http://192.168.31.208:8081/admin/index.php?route=common/forgotten"
