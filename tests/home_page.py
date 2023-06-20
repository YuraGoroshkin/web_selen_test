from selenium.webdriver.common.by import By
import time


def test_click_logo_home_page(browser):
    logo = browser.find_element(By.CSS_SELECTOR, "#logo")
    old = browser.current_url
    logo.click()
    new = browser.current_url
    assert old == "http://192.168.31.208:8081/"
    assert new == old + "index.php?route=common/home"


def test_featured_space(browser):
    featured = len(browser.find_elements(By.CSS_SELECTOR, ".image"))
    assert 4 == featured


def test_carousel_swiper_viewport_bottom(browser):
    carousel = len(browser.find_elements(By.XPATH,
                                         '//div[@class="swiper-pagination carousel0 swiper-pagination-clickable swiper-pagination-bullets"]/*'))
    assert 11 == carousel


def test_carousel_swiper_viewport_top(browser):
    carousel = len(browser.find_elements(By.XPATH,
                                         '//div[@class="swiper-pagination slideshow0 swiper-pagination-clickable swiper-pagination-bullets"]/*'))
    assert 2 == carousel


def test_featured_text(browser):
    text = "Featured"
    featured = browser.find_elements(By.XPATH, '//*[@id="content"]/h3')
    assert text == featured[0].text
