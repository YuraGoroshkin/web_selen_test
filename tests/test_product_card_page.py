from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_mac_book_price(browser):
    if browser.current_url == "http://192.168.31.208:8081/":
        mac_book = browser.find_element(By.CSS_SELECTOR, ".image")
        mac_book.click()
    WebDriverWait(browser, 3).until(EC.url_contains("http://192.168.31.208:8081/macbook"))
    price = "$602.00"
    mac_book_price = browser.find_element(By.XPATH, '//*[@id="content"]/div/div[2]/ul[2]/li[1]/h2')
    assert price == mac_book_price.text


def test_mac_book_photo_showcase(browser):
    if browser.current_url == "http://192.168.31.208:8081/":
        mac_book = browser.find_element(By.CSS_SELECTOR, ".image")
        mac_book.click()
    title_picture = browser.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/ul[1]/li[1]/a')
    size = title_picture.size
    assert size["height"] > 0
    assert size["width"] > 0


def test_mac_description(browser):
    if browser.current_url == "http://192.168.31.208:8081/":
        mac_book = browser.find_element(By.CSS_SELECTOR, ".image")
        mac_book.click()
    description = browser.find_element(By.CSS_SELECTOR, "li.active")
    assert "Description" == description.text


def test_mac_specification(browser):
    if browser.current_url == "http://192.168.31.208:8081/":
        mac_book = browser.find_element(By.CSS_SELECTOR, ".image")
        mac_book.click()
    specification = browser.find_element(By.CSS_SELECTOR, 'a[href = "#tab-specification"]')
    specification.click()
    assert browser.find_element(By.CSS_SELECTOR, "td strong").tag_name == "strong"


def test_mac_reviews_forms(browser):
    if browser.current_url == "http://192.168.31.208:8081/":
        mac_book = browser.find_element(By.CSS_SELECTOR, ".image")
        mac_book.click()
    browser.find_element(By.CSS_SELECTOR, 'a[href = "#tab-review"]').click()
    forms = len(browser.find_elements(By.XPATH, '//div[@class="form-group required"]/*'))
    assert 3 == forms
