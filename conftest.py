import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from utilities.test_data import TestData

@pytest.fixture(params=["chrome", "firefox", "edge"])
def initialize_driver(request):
    if request.param == "chrome":
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options)
    elif request.param == "firefox":        
        driver = webdriver.Firefox()
    elif request.param == "edge":
        options = webdriver.EdgeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Edge(options=options)
    request.cls.driver = driver
    print("Browser: ", request.param)
    driver.get(TestData.url)
    driver.maximize_window()    
    yield
    print("Close Driver")
    driver.close()