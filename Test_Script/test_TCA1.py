import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

@pytest.fixture(scope="module")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument(r"user-data-dir=C:/Users/LENOVO/AppData/Local/Google/Chrome/User Data")
    options.add_argument("--profile-directory=Profile 1")

    service = Service('chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=options)

    time.sleep(5) 
    driver.get("https://web.whatsapp.com")
    assert "web.whatsapp.com" in driver.current_url

    yield driver
    driver.quit()


def test_create_group(driver):
    time.sleep(5)

    new_chat_btn = driver.find_element(By.XPATH, '//div[@title="New chat"]')
    new_chat_btn.click()
    time.sleep(1)

    new_group_btn = driver.find_element(By.XPATH, '//div[@title="New group"]')
    new_group_btn.click()
    time.sleep(1)

    # Tambahkan peserta (pastikan ada minimal 1 kontak tersimpan)
    contact = driver.find_element(By.XPATH, '//div[@role="option"]')
    contact.click()
    next_btn = driver.find_element(By.XPATH, '//span[@data-icon="arrow-forward"]')
    next_btn.click()
    time.sleep(1)

    group_name_input = driver.find_element(By.XPATH, '//div[@title="Group subject"]')
    group_name_input.send_keys("Grup Otomatis")
    create_btn = driver.find_element(By.XPATH, '//span[@data-icon="checkmark"]')
    create_btn.click()
    time.sleep(3)

    assert "Grup Otomatis" in driver.page_source