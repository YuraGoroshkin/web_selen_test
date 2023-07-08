from pages.AdminPage import AdminPage


def test_catalog_accessible_name(browser):
    path = 'admin/'
    browser.get(browser.current_url + path)
    username_form = AdminPage.find_username_form(browser)
    assert username_form.accessible_name == "Username"


def test_catalog_accessible_password(browser):
    path = 'admin/'
    browser.get(browser.current_url + path)
    password_form = AdminPage.find_password_form(browser)
    assert password_form.accessible_name == "Password"


def test_button_login(browser):
    path = 'admin/'
    browser.get(browser.current_url + path)
    button = AdminPage.find_button(browser)
    assert button.aria_role == "button"


def test_header(browser):
    path = 'admin/'
    browser.get(browser.current_url + path)
    header = AdminPage.find_header(browser)
    assert header.text == "Please enter your login details."


def test_link_forgot(browser):
    path = 'admin/'
    browser.get(browser.current_url + path)
    link_forgot = AdminPage.find_link_forgot(browser)
    assert link_forgot.get_attribute('href') == browser.current_url + "index.php?route=common/forgotten"


def test_add_and_delet_product(browser):
    path = 'admin/'
    browser.get(browser.current_url + path)
    AdminPage.login(browser)
    AdminPage.go_to_products(browser)
    old = AdminPage.count_the_number_of_products(browser)
    AdminPage.add_product(browser)
    new = AdminPage.count_the_number_of_products(browser)
    AdminPage.delet_product(browser)
    after_delet = AdminPage.count_the_number_of_products(browser)
    assert old < new
    assert old == after_delet
