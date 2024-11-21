import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json
import os


@pytest.fixture(scope='session')
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--lang=en")

    driver = webdriver.Chrome(options=chrome_options)

    yield driver

    driver.quit()


@pytest.fixture(scope='session')
def character_data():
    # This fixture loads data from the JSON file character_data made at api_interaction.py
    json_file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'character_data.json')
    with open(json_file_path, 'r') as f:
        data = json.load(f)
    return data
