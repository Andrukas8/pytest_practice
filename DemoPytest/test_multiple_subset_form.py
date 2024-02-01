from selenium import webdriver
from selenium.webdriver.common.by import By


def test_search_lambdatest_simple_form_demo():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, "//input[@id='user-message']").send_keys("Pytest Is a Test Framework")
    driver.find_element(By.ID, "showInput").click()
    message = driver.find_element(By.ID, "message").text
    
    assert message == "Pytest Is a Test Framework"
    
    driver.quit()
    
    