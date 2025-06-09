import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

@pytest.fixture(scope="module")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument(r"user-data-dir=C:/Users/LENOVO/AppData/Local/Google/Chrome/User Data") # Ganti dengan path user data Chrome Anda
    options.add_argument(r"--profile-directory=Profile 1") # Ganti dengan nama profil yang sesuai
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")

    # Setup ChromeDriver service
    service = Service('chromedriver.exe') # Pastikan chromedriver.exe ada di direktori yang sama atau ganti path sesuai lokasi
    driver = webdriver.Chrome(service=service, options=options)

    # Buka WhatsApp Web
    driver.get("https://web.whatsapp.com")
    time.sleep(10)  # waktu login manual jika belum login 10 detik

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

    # Tambahkan peserta
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