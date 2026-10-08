import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

@pytest.fixture 
def setup_teardown():
    # Setup: Initialize the Chrome WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()  # Replace with your application's URL
    yield driver  # This will be used in the test function
    driver.quit()

def test_addition(setup_teardown):
    driver = setup_teardown
    driver.get("http://localhost:8000/index.html") 
    driver.find_element(By.ID, "num1").send_keys("10")
    driver.find_element(By.ID, "num2").send_keys("20")
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(1) 

    result = driver.find_element(By.ID, "result").text
    assert "30" in result, "Expected 30, but got: {result}"
    print("Test passed")