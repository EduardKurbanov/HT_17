"""
Завдання: за допомогою браузера (Selenium) відкрити форму за наступним посиланням:
https://docs.google.com/forms/d/e/1FAIpQLScLhHgD5pMnwxl8JyRfXXsJekF8_pDG36XtSEwaGsFdU2egyw/viewform?usp=sf_link
заповнити і відправити її.
Зберегти два скріншоти: заповненої форми і повідомлення про відправлення форми.
В репозиторії скріншоти зберегти.
Корисні посилання:
https://www.selenium.dev/documentation/
https://chromedriver.chromium.org/downloads
"""

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class WebScreenFormGoogle(object):
    _url = 'https://docs.google.com/forms/d/e/1FAIpQLScLhHgD5pMnwxl8JyRfXXsJekF8_pDG36XtSEwaGsFdU2egyw/viewform?usp=sf_link'
    _options = ChromeOptions()
    _options.add_argument('--disable-notifications')
    _options.add_argument("disable-infobars")
    _options.add_argument("--disable-extensions")
    _options.add_argument("--disable-dev-shm-usage")
    _options.add_argument("--no-sandbox")
    _driver = Chrome(options=_options)

    def start_google_web(self):
        self.wait_s = WebDriverWait(self._driver, 10)
        self._driver.get(url=self._url)
        text_input = self.wait_s.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='text']")))
        text_input.clear()
        text_input.send_keys("Eduard")
        self._driver.save_screenshot("1.png")
        time.sleep(1)
        enter_button = self._driver.find_element(By.XPATH, "//div[@role='button']")
        enter_button.click()
        self._driver.save_screenshot("2.png")
        time.sleep(1)

    def close_wd(self):
        self._driver.close()

    def quit_wb(self):
        self._driver.quit()


if __name__ in '__main__':
    try:
        wd = WebScreenFormGoogle()
        wd.start_google_web()
        wd.close_wd()

    except Exception as err:
        print(f"error -> {err}")
    finally:
        wd = WebScreenFormGoogle()
        wd.quit_wb()
