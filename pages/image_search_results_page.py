from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ImageSearchResultsPage:
    def __init__(self, driver):
        self.driver = driver
        self.image_locator = (By.XPATH, "//div[@data-q]//img")

    def click_image_by_position(self, position):
        wait = WebDriverWait(self.driver, 10)
        images = wait.until(EC.presence_of_all_elements_located(self.image_locator))
        if position >= len(images):
            position = len(images) - 1
        images[position].click()
