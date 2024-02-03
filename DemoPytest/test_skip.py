from datetime import datetime
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLambdaTest:
    def test_sample_app_title(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options)
        driver.get("https://lambdatest.github.io/sample-todo-app/")
        pytest.skip()
        expected_title = "Sample page - lambdatest.com"
        assert expected_title == driver.title

    @pytest.mark.skip(reason="Code Has Not Been Deployed")
    def test_ecommerce_title(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options)
        driver.get(
            "https://ecommerce-playground.lambdatest.io/index.php?route=product/category&path=17")
        expected_title = "Software"
        assert expected_title == driver.title

    @pytest.mark.skip()
    def test_special_offers(self):
        options = webdriver.ChromeOptions() 
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options)
        driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=product/special")
        expected_title = "Spectial Offers"
        assert expected_title == driver.title

    @pytest.mark.skipif(
            datetime.now() >= datetime(2099, 12, 31),
            reason = "Repo Is Not Complete Untill After Finishing Tutorial"
            )
    def test_pytest_github_repo(self):
        options = webdriver.ChromeOptions() 
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options)
        driver.get("https://github.com/RexJonesII/PytestTutorials")
        expected_title = "RexJonesII"
        print(f"Title: {expected_title}")
        assert driver.title.__contains__(expected_title)
        
        
    
