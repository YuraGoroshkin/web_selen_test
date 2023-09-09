from pages.HomePage import HomePage
import pytest


def test_click_logo_home_page(browser):
    browser.implicitly_wait(2)
    logo = HomePage.find_logo(browser)
    old = browser.current_url
    logo.click()
    new = browser.current_url
    assert old == "http://192.168.31.208:8081/"
    assert new == old + "index.php?route=common/home"


def test_featured_space(browser):
    featured = HomePage.count_featured(browser)
    assert 4 == featured


def test_carousel_swiper_viewport_bottom(browser):
    carousel = HomePage.count_carousel_bottom(browser)
    assert 11 == carousel


def test_carousel_swiper_viewport_top(browser):
    carousel = HomePage.count_carousel_top(browser)
    assert 2 == carousel


def test_featured_text(browser):
    text = "Featured"
    featured = HomePage.get_featured(browser)
    assert text == featured[0].text


@pytest.mark.parametrize('num, description', [(0, 'euro'), (1, 'pound'), (2, 'dollar')])
def test_change_currency(browser, num, description):
    browser.implicitly_wait(2)
    valuta = ['€', '£', '$']
    # евро = 0 / стерлинг = 1 / доллар = 2
    HomePage.change_currency(browser, num)
    valuta_in_price = HomePage.get_valuta_in_price(browser)
    assert valuta[num] in valuta_in_price
