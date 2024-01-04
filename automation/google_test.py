# test_example_website.py
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


@pytest.fixture
def browser():
    # Initialize the Chrome WebDriver (you can use other drivers like Firefox)
    driver = webdriver.Chrome()
    yield driver
    # Quit the browser after the test
    driver.quit()


def test_search_on_google(browser):
    # Open Google in the browser
    browser.get("https://www.google.com")

    # Find the search box element and enter a search query
    search_box = browser.find_element("id", "APjFqb")
    search_box.send_keys("YouTube")
    browser.implicitly_wait(5)

    link = browser.find_element("link text", "YouTube: Home")

    # link.click()
    # Submit the search query
    # search_box.send_keys(Keys.RETURN)

    # Wait for the results page to load
    browser.implicitly_wait(5)

    # Assert that the search results contain the expected text
    assert "raja" in browser.page_source


def test_navigation(browser):

    # Open a sample website
    browser.get("https://www.example.com")

    # Find a link element and click on it
    link = browser.find_element("link text", "More information...")
    link.click()

    # Wait for the new page to load
    browser.implicitly_wait(5)

    # Assert that the new page title contains the expected text
    assert "Example" in browser.title
