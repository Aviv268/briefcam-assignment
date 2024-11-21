from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
import os
import allure
from datetime import datetime


class ImagePage:
    def __init__(self, driver):
        self.driver = driver
        # self.image_locator = (By.XPATH, "//div[@data-q]//img")
        self.image_locator = (By.XPATH, "//img[contains(@src, '')]")

    def capture_screenshot(self, character_name, character_id):
        timestamp = datetime.now().strftime('%d%m%Y-%H%M%S')

        filename = f"{character_name.replace(' ', '')}{character_id}-{timestamp}.jpg"
        filepath = os.path.join('screenshots', filename)
        os.makedirs(os.path.dirname(filepath), exist_ok=True)

        wait = WebDriverWait(self.driver, 10)
        try:
            image_element = wait.until(EC.visibility_of_element_located(self.image_locator))
            location = image_element.location_once_scrolled_into_view
            size = image_element.size

            self.driver.save_screenshot('full_screenshot.png')

            image = Image.open('full_screenshot.png')
            left = location['x']
            top = location['y']
            right = left + size['width']
            bottom = top + size['height']
            image = image.crop((left, top, right, bottom))
            image.save(filepath)

            # Remove the full page screenshot
            os.remove('full_screenshot.png')

        except TimeoutException:
            # If the image element cant be found it captures the full page
            print("Image element not found, capturing the full page instead")
            self.driver.save_screenshot(filepath)

        with open(filepath, 'rb') as f:
            allure.attach(f.read(), name=filename, attachment_type=allure.attachment_type.JPG)

