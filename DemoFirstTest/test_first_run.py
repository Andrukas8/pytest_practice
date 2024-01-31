from selenium import webdriver


def test_lambdatest_playground():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://www.lambdatest.com/selenium-playground/")
    print(f"Page Title: {driver.title}")
    driver.quit()

def test2_lambdatest_ecommerce():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://ecommerce-playground.lambdatest.io/")
    print(f"Page Title: {driver.title}")
    driver.quit()

def testRexWebsite():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://rexjones2.com")
    print(f"Page Title: {driver.title}")
    driver.quit()
