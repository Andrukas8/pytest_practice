import pytest
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.parametrize("num1, num2, expected_total",
                          [
                              ("25", "25", "50"),
                              ("10", "20", "30"),
                              ("30", "40", "70"),
                              ("q", "3", "Entered value is not a number"),
                              ("5", "t", "Entered value is not a number"),
                              ("r", "g", "Entered value is not a number")                              
                          ])
def test_lambdatest_two_input_fields(num1, num2, expected_total):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")
    driver.implicitly_wait(10)
    
    num1_field = driver.find_element(By.ID, "sum1")
    num1_field.clear()
    num1_field.send_keys(num1)
    
    num2_field = driver.find_element(By.ID, "sum2")
    num2_field.clear()
    num2_field.send_keys(num2)
    
    driver.find_element(By.XPATH, "//button[text()='Get Sum']").click()
    actual_total = driver.find_element(By.ID, "addmessage").text
    
    assert actual_total == expected_total, \
        "Actual and Expected Results Do Not Match"
    
    driver.quit()

@pytest.mark.parametrize("base", [1, 2, 3])
@pytest.mark.parametrize("exponent", [4, 5, 6])
def test_raising_base_to_power(base, exponent):
    result = base ** exponent
    assert result == math.pow(base, exponent)
    




