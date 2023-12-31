from pages.RegistrationPage import RegistrationPage


def test_header(browser):
    path = 'index.php?route=account/register'
    browser.get(browser.current_url + path)
    header = RegistrationPage.find_header(browser)
    assert header.text == "Register Account"


def test_account_form(browser):
    path = 'index.php?route=account/register'
    browser.get(browser.current_url + path)
    account_form = RegistrationPage.find_account_form(browser)
    form = account_form.text.split(sep='\n')
    assert 'Your Personal Details' == form[0]
    assert 'First Name' == form[1]
    assert 'Last Name' == form[2]
    assert 'E-Mail' == form[3]
    assert 'Telephone' == form[4]


def test_account_form_password(browser):
    path = 'index.php?route=account/register'
    browser.get(browser.current_url + path)
    account_form_password = RegistrationPage.find_account_form_password(browser)
    form = account_form_password.text.split(sep='\n')
    assert 'Your Password' == form[0]
    assert 'Password' == form[1]
    assert 'Password Confirm' == form[2]


def test_radio_button(browser):
    path = 'index.php?route=account/register'
    browser.get(browser.current_url + path)
    radio_button = RegistrationPage.find_radio_button(browser)
    assert radio_button[0].text == "Yes"
    assert radio_button[1].text == "No"


def test_continue_button(browser):
    path = 'index.php?route=account/register'
    browser.get(browser.current_url + path)
    continue_button = RegistrationPage.find_continue_button(browser)
    assert continue_button.tag_name == "input"


def test_registration_new(browser):
    path = 'index.php?route=account/register'
    browser.get(browser.current_url + path)
    RegistrationPage.fill_personal(browser)
    access = RegistrationPage.notification_check(browser)
    assert access == 'Your Account Has Been Created!'