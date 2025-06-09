import pytest
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service

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

def test_check_responsive_ui(driver):
    time.sleep(5)

    sizes = [(1200, 800), (800, 600), (500, 700)]
    for width, height in sizes:
        driver.set_window_size(width, height)
        time.sleep(2)
        assert driver.find_element("tag name", "body") is not None
