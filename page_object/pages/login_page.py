from page_object.pages.base_page import BasePage
from page_object.locators.locators import LoginPageLocators


class LoginPage(BasePage):

    PAGE = '/auth/login'

    def enter_username(self, username):
        self.wait_element_enabled(LoginPageLocators.USERNAME).send_keys(username)

    def enter_password(self, password):
        self.wait_element_enabled(LoginPageLocators.PASSWORD).send_keys(password)

    def click_in(self):
        self.wait_element_enabled(LoginPageLocators.LOGIN_BUTTON).click()

    def check_login_page_is_load(self):
        self.wait_element_enabled(LoginPageLocators.LOGIN_TITLE)

    def check_credentials_alert(self):
        alert = self.wait_element_enabled(LoginPageLocators.CREDENTIALS_ALERT)
        assert alert.text == 'Invalid credentials', \
            f'Некорректный текст credentials alert: {alert.text}'

    def log_in(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_in()






