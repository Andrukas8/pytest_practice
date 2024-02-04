from selenium import webdriver
from selenium.webdriver.common.by import By


class ChangePasswordLocatorsFields:
    password_field = (By.ID, "input-password")
    confirmation_password_field = (By.ID, "input-confirm")
    continue_button = (
        By.XPATH, "//div[@id='content']//input[@value='continue']")
    confirmation_error_message = (By.CSS_SELECTOR, "#content .text-danger")
