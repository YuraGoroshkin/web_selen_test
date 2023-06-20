from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_header(browser):
    browser.get('http://192.168.31.208:8081/index.php?route=account/register')
    WebDriverWait(browser, 2).until(EC.url_contains("http://192.168.31.208:8081/index.php?route=account/register"))
    header = browser.find_element(By.XPATH, '//*[@id="content"]/h1')
    assert header.text == "Register Account"


def test_account_form(browser):
    browser.get('http://192.168.31.208:8081/index.php?route=account/register')
    WebDriverWait(browser, 3).until(EC.url_contains("http://192.168.31.208:8081/index.php?route=account/register"))
    account_form = browser.find_element(By.CSS_SELECTOR, 'fieldset#account')
    form = account_form.text.split(sep='\n')
    assert 'Your Personal Details' == form[0]
    assert 'First Name' == form[1]
    assert 'Last Name' == form[2]
    assert 'E-Mail' == form[3]
    assert 'Telephone' == form[4]


def test_account_form_password(browser):
    browser.get('http://192.168.31.208:8081/index.php?route=account/register')
    WebDriverWait(browser, 3).until(EC.url_contains("http://192.168.31.208:8081/index.php?route=account/register"))
    account_form_password = browser.find_element(By.CSS_SELECTOR, 'fieldset:nth-of-type(2)')
    form = account_form_password.text.split(sep='\n')
    assert 'Your Password' == form[0]
    assert 'Password' == form[1]
    assert 'Password Confirm' == form[2]


def test_radio_button(browser):
    browser.get('http://192.168.31.208:8081/index.php?route=account/register')
    WebDriverWait(browser, 3).until(EC.url_contains("http://192.168.31.208:8081/index.php?route=account/register"))
    radio_button = browser.find_elements(By.XPATH, '//div[@class="col-sm-10"]/label')
    assert radio_button[0].text == "Yes"
    assert radio_button[1].text == "No"


def test_continue_button(browser):
    browser.get('http://192.168.31.208:8081/index.php?route=account/register')
    WebDriverWait(browser, 3).until(EC.url_contains("http://192.168.31.208:8081/index.php?route=account/register"))
    continue_button = browser.find_element(By.XPATH, '//input[@value="Continue"]')
    assert continue_button.tag_name == "input"
