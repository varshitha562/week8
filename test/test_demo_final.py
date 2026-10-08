import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def setup_teardown():
    # Setup: launch browser
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )

    yield driver

    driver.quit()


def test_demo(setup_teardown):
    driver = setup_teardown
    driver.get("https://www.google.com")

    print("Page title:", driver.title)

    assert "Google" in driver.title, "Test Failed: Title mismatch"