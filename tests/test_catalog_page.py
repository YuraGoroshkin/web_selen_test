from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_catalog_via_phones(browser):
    catalog_via_phones = browser.find_element(By.CSS_SELECTOR, "li:nth-child(6)")
    catalog_via_phones.click()
    phones = len(browser.find_elements(By.XPATH, '// *[ @ id = "content"] / div[2]/*'))
    assert 3 == phones


def test_desktops(browser):
    name = "Desktops"
    catalog_via_phones = browser.find_element(By.CSS_SELECTOR, "li:nth-child(6)")
    catalog_via_phones.click()
    WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.list-group-item")))
    desktops = browser.find_elements(By.CSS_SELECTOR, "a.list-group-item")
    desktops[0].click()
    name_catalog = browser.find_elements(By.XPATH, '// *[ @ id = "content"] / h2')
    assert name == name_catalog[0].text


def test_laptops_notebooks(browser):
    name = "Laptops & Notebooks"
    catalog_via_phones = browser.find_element(By.CSS_SELECTOR, "li:nth-child(6)")
    catalog_via_phones.click()
    WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.list-group-item")))
    desktops = browser.find_elements(By.CSS_SELECTOR, "a.list-group-item")
    desktops[1].click()
    name_catalog = browser.find_elements(By.XPATH, '// *[ @ id = "content"] / h2')
    assert name == name_catalog[0].text


def test_components(browser):
    name = "Components"
    catalog_via_phones = browser.find_element(By.CSS_SELECTOR, "li:nth-child(6)")
    catalog_via_phones.click()
    WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.list-group-item")))
    desktops = browser.find_elements(By.CSS_SELECTOR, "a.list-group-item")
    desktops[2].click()
    name_catalog = browser.find_elements(By.XPATH, '// *[ @ id = "content"] / h2')
    assert name == name_catalog[0].text


def test_tablets(browser):
    name = "Tablets"
    catalog_via_phones = browser.find_element(By.CSS_SELECTOR, "li:nth-child(6)")
    catalog_via_phones.click()
    WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.list-group-item")))
    desktops = browser.find_elements(By.CSS_SELECTOR, "a.list-group-item")
    desktops[3].click()
    name_catalog = browser.find_elements(By.XPATH, '// *[ @ id = "content"] / h2')
    assert name == name_catalog[0].text


def test_software(browser):
    name = "Software"
    catalog_via_phones = browser.find_element(By.CSS_SELECTOR, "li:nth-child(6)")
    catalog_via_phones.click()
    WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.list-group-item")))
    desktops = browser.find_elements(By.CSS_SELECTOR, "a.list-group-item")
    desktops[4].click()
    name_catalog = browser.find_elements(By.XPATH, '// *[ @ id = "content"] / h2')
    assert name == name_catalog[0].text


def test_cameras(browser):
    name = "Cameras"
    catalog_via_phones = browser.find_element(By.CSS_SELECTOR, "li:nth-child(6)")
    catalog_via_phones.click()
    WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.list-group-item")))
    desktops = browser.find_elements(By.CSS_SELECTOR, "a.list-group-item")
    desktops[6].click()
    name_catalog = browser.find_elements(By.XPATH, '// *[ @ id = "content"] / h2')
    assert name == name_catalog[0].text


def test_mp3_players(browser):
    name = "MP3 Players"
    catalog_via_phones = browser.find_element(By.CSS_SELECTOR, "li:nth-child(6)")
    catalog_via_phones.click()
    WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.list-group-item")))
    desktops = browser.find_elements(By.CSS_SELECTOR, "a.list-group-item")
    desktops[7].click()
    name_catalog = browser.find_elements(By.XPATH, '// *[ @ id = "content"] / h2')
    assert name == name_catalog[0].text
