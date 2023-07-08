from pages.ProductCardPage import ProductCardPage


def test_mac_book_price(browser):
    ProductCardPage.go_to_mac(browser)
    price = "$602.00"
    mac_book_price = ProductCardPage.mac_book_price(browser)
    assert price == mac_book_price.text


def test_mac_book_photo_showcase(browser):
    ProductCardPage.go_to_mac(browser)
    title_picture = ProductCardPage.find_title_picture(browser)
    size = title_picture.size
    assert size["height"] > 0
    assert size["width"] > 0


def test_mac_description(browser):
    ProductCardPage.go_to_mac(browser)
    description = ProductCardPage.find_description(browser)
    assert "Description" == description.text


def test_mac_specification(browser):
    ProductCardPage.go_to_mac(browser)
    specification_element= ProductCardPage.go_to_specification(browser)
    assert specification_element.tag_name == "strong"


def test_mac_reviews_forms(browser):
    ProductCardPage.go_to_mac(browser)
    forms = ProductCardPage.go_to_reviews_forms(browser)
    assert 3 == forms
