from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GoogleImagesPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_box = (By.NAME, 'q')

    def search(self, query):
        wait = WebDriverWait(self.driver, 10)
        search_box = wait.until(EC.presence_of_element_located(self.search_box))
        search_box.clear()
        search_box.send_keys(query)
        search_box.submit()
