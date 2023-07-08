from pages.CatalogPage import CatalogPage


def test_catalog_via_phones(browser):
    CatalogPage.go_to_phone(browser)
    phones = CatalogPage.count_the_numbers_phones(browser)
    assert 3 == phones


def test_desktops(browser):
    name = "Desktops"
    CatalogPage.go_to_phone(browser)
    name_catalog = CatalogPage.flip_to_desktops(browser)
    assert name == name_catalog[0].text


def test_laptops_notebooks(browser):
    name = "Laptops & Notebooks"
    CatalogPage.go_to_phone(browser)
    name_catalog = CatalogPage.flip_to_laptops_and_notebooks(browser)
    assert name == name_catalog[0].text


def test_components(browser):
    name = "Components"
    CatalogPage.go_to_phone(browser)
    name_catalog = CatalogPage.flip_to_components(browser)
    assert name == name_catalog[0].text


def test_tablets(browser):
    name = "Tablets"
    CatalogPage.go_to_phone(browser)
    name_catalog = CatalogPage.flip_to_tablets(browser)
    assert name == name_catalog[0].text


def test_software(browser):
    name = "Software"
    CatalogPage.go_to_phone(browser)
    name_catalog = CatalogPage.flip_to_software(browser)
    assert name == name_catalog[0].text


def test_cameras(browser):
    name = "Cameras"
    CatalogPage.go_to_phone(browser)
    name_catalog = CatalogPage.flip_to_cameras(browser)
    assert name == name_catalog[0].text


def test_mp3_players(browser):
    name = "MP3 Players"
    CatalogPage.go_to_phone(browser)
    name_catalog = CatalogPage.flip_to_mp3_players(browser)
    assert name == name_catalog[0].text
