from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.RegistrationPage import RegistrationPage


def test_header(browser):
    path = 'index.php?route=account/register'
    browser.get(browser.current_url + path)
    WebDriverWait(browser, 2).until(EC.url_contains("http://192.168.31.208:8081/index.php?route=account/register"))
    header = browser.find_element(By.XPATH, '//*[@id="content"]/h1')
    assert header.text == "Register Account"


def test_account_form(browser):
    path = 'index.php?route=account/register'
    browser.get(browser.current_url + path)
    WebDriverWait(browser, 3).until(EC.url_contains("http://192.168.31.208:8081/index.php?route=account/register"))
    account_form = browser.find_element(By.CSS_SELECTOR, 'fieldset#account')
    form = account_form.text.split(sep='\n')
    assert 'Your Personal Details' == form[0]
    assert 'First Name' == form[1]
    assert 'Last Name' == form[2]
    assert 'E-Mail' == form[3]
    assert 'Telephone' == form[4]


def test_account_form_password(browser):
    path = 'index.php?route=account/register'
    browser.get(browser.current_url + path)
    WebDriverWait(browser, 3).until(EC.url_contains("http://192.168.31.208:8081/index.php?route=account/register"))
    account_form_password = browser.find_element(By.CSS_SELECTOR, 'fieldset:nth-of-type(2)')
    form = account_form_password.text.split(sep='\n')
    assert 'Your Password' == form[0]
    assert 'Password' == form[1]
    assert 'Password Confirm' == form[2]


def test_radio_button(browser):
    path = 'index.php?route=account/register'
    browser.get(browser.current_url + path)
    WebDriverWait(browser, 3).until(EC.url_contains("http://192.168.31.208:8081/index.php?route=account/register"))
    radio_button = browser.find_elements(By.XPATH, '//div[@class="col-sm-10"]/label')
    assert radio_button[0].text == "Yes"
    assert radio_button[1].text == "No"


def test_continue_button(browser):
    path = 'index.php?route=account/register'
    browser.get(browser.current_url + path)
    WebDriverWait(browser, 3).until(EC.url_contains("http://192.168.31.208:8081/index.php?route=account/register"))
    continue_button = browser.find_element(By.XPATH, '//input[@value="Continue"]')
    assert continue_button.tag_name == "input"


def test_registration_new(browser):
    path = 'index.php?route=account/register'
    browser.get(browser.current_url + path)
    WebDriverWait(browser, 3).until(EC.url_contains("http://192.168.31.208:8081/index.php?route=account/register"))
    RegistrationPage.fill_personal(browser)
    access = browser.find_element(By.XPATH, '//div/h1').text
    assert access == 'Your Account Has Been Created!'