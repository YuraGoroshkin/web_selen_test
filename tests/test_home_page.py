from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.HomePage import HomePage


# def test_click_logo_home_page(browser):
#     browser.implicitly_wait(2)
#     WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#logo')))
#     logo = browser.find_element(By.CSS_SELECTOR, "#logo")
#     old = browser.current_url
#     logo.click()
#     new = browser.current_url
#     assert old == "http://192.168.31.208:8081/"
#     assert new == old + "index.php?route=common/home"
#
#
# def test_featured_space(browser):
#     featured = len(browser.find_elements(By.CSS_SELECTOR, ".image"))
#     assert 4 == featured
#
#
# def test_carousel_swiper_viewport_bottom(browser):
#     carousel = len(browser.find_elements(By.XPATH,
#                                          '//div[@class="swiper-pagination carousel0 swiper-pagination-clickable swiper-pagination-bullets"]/*'))
#     assert 11 == carousel
#
#
# def test_carousel_swiper_viewport_top(browser):
#     carousel = len(browser.find_elements(By.XPATH,
#                                          '//div[@class="swiper-pagination slideshow0 swiper-pagination-clickable swiper-pagination-bullets"]/*'))
#     assert 2 == carousel
#
#
# def test_featured_text(browser):
#     text = "Featured"
#     featured = browser.find_elements(By.XPATH, '//*[@id="content"]/h3')
#     assert text == featured[0].text

def test_change_currency_euro(browser):
    browser.implicitly_wait(2)
    num = 0
    # евро = 0 / стерлинг = 1 / доллар = 2
    HomePage.change_currency(browser, num)
    valuta = browser.find_elements(By.CSS_SELECTOR, 'p[class="price"]')[0].text
    assert '€' in valuta


def test_change_currency_sterling(browser):
    browser.implicitly_wait(2)
    num = 1
    # евро = 0 / стерлинг = 1 / доллар = 2
    HomePage.change_currency(browser, num)
    valuta = browser.find_elements(By.CSS_SELECTOR, 'p[class="price"]')[0].text
    assert '£' in valuta


def test_change_currency_dollar(browser):
    browser.implicitly_wait(2)
    num = 2
    # евро = 0 / стерлинг = 1 / доллар = 2
    HomePage.change_currency(browser, num)
    valuta = browser.find_elements(By.CSS_SELECTOR, 'p[class="price"]')[0].text
    assert '$' in valuta
