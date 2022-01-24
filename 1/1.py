from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class WebScreenFormGoogle(object):
    def __init__(self):
        self._url = 'https://docs.google.com/forms/d/e/1FAIpQLScLhHgD5pMnwxl8JyRfXXsJekF8_pDG36XtSEwaGsFdU2egyw/viewform?usp=sf_link'
        self._options = ChromeOptions()
        self._options.add_argument('--disable-notifications')
        self._options.add_argument("disable-infobars")
        self._options.add_argument("--disable-extensions")
        self._options.add_argument("--disable-dev-shm-usage")
        self._options.add_argument("--no-sandbox")

    def init_driver(self):
        self._driver = Chrome(options=self._options)
        self._wait_s = WebDriverWait(self._driver, 10)


    def start_google_web(self):
        self._driver.get(url=self._url)
        text_input = self._wait_s.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='text']")))
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
    wd = WebScreenFormGoogle()
    try:
        wd.init_driver()
        wd.start_google_web()
        wd.close_wd()

    except Exception as err:
        print(f"error -> {err}")
    finally:
        wd.quit_wb()
