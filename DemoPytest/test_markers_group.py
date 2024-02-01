import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

pytestmark = [pytest.mark.regression, pytest.mark.sanity] # this marks all tests in this file as regression and sanity

@pytest.mark.integration
@pytest.mark.smoke
def test_lambdatest_ajax_form():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get(
        "https://www.lambdatest.com/selenium-playground/ajax-form-submit-demo")
    driver.implicitly_wait(10)
    driver.find_element(By.ID, "title").send_keys("Pytest Tutorial")
    driver.find_element(By.ID, "description").send_keys(
        "LamdaTest Selenium Playground")
    driver.find_element(By.ID, "btn-submit").click()
    request = driver.find_element(By.ID, "submit-control").text
    assert request.__contains__("Processing")
    driver.quit()


def test_e2e():
    print("End to End Test")

@pytest.mark.smoke
def test_login():
    print("Log Into Application")

@pytest.mark.smoke
def test_logout():
    print("Log Out Application")
