import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="module")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument(r"user-data-dir=C:/Users/LENOVO/AppData/Local/Google/Chrome/User Data")
    options.add_argument("--profile-directory=Profile 1")

    service = Service('chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=options)
 
    driver.get("https://web.whatsapp.com")
    assert "web.whatsapp.com" in driver.current_url

    yield driver
    driver.quit()
def test_validate_encryption(driver):
    time.sleep(5)
    search_box = driver.find_element(By.XPATH, '//div[@title="Search input textbox"]')
    search_box.click()
    search_box.send_keys("Kontak Uji")  # Ganti dengan nama kontak valid
    time.sleep(2)

    contact = driver.find_element(By.XPATH, '//span[@title="Kontak Uji"]')
    contact.click()
    time.sleep(2)

    contact_info = driver.find_element(By.XPATH, '//header//div[@title="Menu"]')
    contact_info.click()
    time.sleep(1)

    info_option = driver.find_element(By.XPATH, '//div[contains(text(), "Contact info")]')
    info_option.click()
    time.sleep(3)

    assert "Messages are end-to-end encrypted" in driver.page_source
