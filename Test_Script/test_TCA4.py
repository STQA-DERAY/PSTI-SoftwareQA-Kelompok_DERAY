import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from selenium.webdriver.chrome.service import Service

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

def test_send_text_and_media(driver):
    time.sleep(5)
    search_box = driver.find_element(By.XPATH, '//div[@title="Search input textbox"]')
    search_box.click()
    search_box.send_keys("reyg")  # Ganti dengan nama kontak valid
    time.sleep(2)

    contact = driver.find_element(By.XPATH, '//span[@title="reyg"]')
    contact.click()
    time.sleep(2)

    # Send text message
    msg_box = driver.find_element(By.XPATH, '//div[@title="Type a message"]')
    msg_box.send_keys("Pesan otomatis dari Selenium!")
    msg_box.send_keys("\n")
    time.sleep(1)

    # Send media
    attach_btn = driver.find_element(By.XPATH, '//div[@title="Attach"]')
    attach_btn.click()
    time.sleep(1)

    file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
    file_path = os.path.abspath("test-image.jpg")  # Ganti dengan path file valid
    file_input.send_keys(file_path)
    time.sleep(3)

    send_btn = driver.find_element(By.XPATH, '//span[@data-icon="send"]')
    send_btn.click()
    time.sleep(3)

    assert "Pesan otomatis dari Selenium!" in driver.page_source
