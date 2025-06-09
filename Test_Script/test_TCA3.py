import pytest
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="module")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument(r"user-data-dir=C:/Users/LENOVO/AppData/Local/Google/Chrome/User Data/Default") # Ganti dengan path user data Chrome Anda
    options.add_argument(r"--profile-directory=Default") # Ganti dengan nama profil yang sesuai
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

def test_check_responsive_ui(driver):
    time.sleep(5)

    sizes = [(1200, 800), (800, 600), (500, 700)]
    for width, height in sizes:
        driver.set_window_size(width, height)
        time.sleep(2)
        assert driver.find_element("tag name", "body") is not None
