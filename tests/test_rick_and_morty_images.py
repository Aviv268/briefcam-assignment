import pytest
import allure

from pages.google_home_page import GoogleHomePage
from pages.google_images_page import GoogleImagesPage
from pages.image_page import ImagePage
from pages.image_search_results_page import ImageSearchResultsPage


@allure.step("Test Rick and Morty Character Images")
def test_rick_and_morty_character_images(driver, character_data):

    first_character = character_data[0]
    second_character = character_data[1]

    google_home = GoogleHomePage(driver)
    google_images = GoogleImagesPage(driver)
    image_results = ImageSearchResultsPage(driver)
    image_page = ImagePage(driver)

    google_home.navigate_to_google()
    google_home.click_images_link()

    search_query = f"Rick and Morty {first_character['name']}"
    google_images.search(search_query)

    first_id_str = str(first_character['id']).zfill(2)
    if len(first_id_str) >= 3:
        position = int(first_id_str[-3]) + int(first_id_str[-1])
    else:
        position = int(first_id_str[-2]) + int(first_id_str[-1])

    image_results.click_image_by_position(position)

    image_page.capture_screenshot(first_character['name'], first_character['id'])

    driver.get(second_character['image'])

    image_page.capture_screenshot(second_character['name'], second_character['id'])

    if first_character['location'] == second_character['location']:
        print(f"Both characters are from {first_character['location']}.")
    else:
        print(f"{first_character['name']} from {first_character['location']} and {second_character['name']} from {second_character['location']}.")
        assert False, "Characters are from different locations."
