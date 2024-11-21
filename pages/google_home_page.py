from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GoogleHomePage:
    def __init__(self, driver):
        self.driver = driver
        self.images_link = (By.XPATH, "//a[text()='Images' or text()='חיפוש תמונות']")

    def navigate_to_google(self):
        self.driver.get('https://www.google.com')

    def click_images_link(self):
        wait = WebDriverWait(self.driver, 10)
        images_link = wait.until(EC.element_to_be_clickable(self.images_link))
        images_link.click()
