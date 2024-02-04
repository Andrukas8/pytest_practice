import softest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_SoftAssertionsTest(softest.TestCase):

    def test_SoftAssertion_radio_button_demo_value(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.get(
            "https://www.lambdatest.com/selenium-playground/radiobutton-demo")

        driver.find_element(
            By.XPATH, "//div[@class='w-8/12 smtablet:w-full left-input mr-20 pr-30 smtablet:mr-0 smtablet:pr-0']//div//label[@class='text-size-16 mt-10 text-black mr-20'][normalize-space()='Male']").click()
        driver.find_element(
            By.XPATH, "//label[normalize-space()='0 to 5']").click()
        driver.find_element(By.XPATH, "//button[text()='Get values']").click()
        gender = driver.find_element(By.CSS_SELECTOR, ".genderbutton").text
        age_group = driver.find_element(
            By.CSS_SELECTOR, ".groupradiobutton").text

        self.soft_assert(self.assertTrue, gender.__contains__("Male"))
        self.soft_assert(
            self.assertTrue, driver.title.__contains__("Selenium"))
        self.soft_assert(self.assertIn, "5", age_group,
                         "Age Group Is Not Correct")

        self.assert_all("Verity Genter, Title, Age Group")

        driver.quit()
