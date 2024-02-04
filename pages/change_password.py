from pages.base_page import BasePage
from utilities.locators import ChangePasswordLocatorsFields


class ChangePasswordPage(BasePage):
    def __init__(self):
        self.locate = ChangePasswordLocatorsFields
        super().__init__(driver)

    def change_password(self, password, confirm_password):
        self.set(self.locate.password_field, password)
        self.set(self.locate.confirmation_password_field, confirm_password)
        self.click(self.locate.continue_button)
        return MyAccountPage(self.driver)

    def get_confirmation_error_message(self):
        return self.get_text(self.locate.confirmation_error_message)
