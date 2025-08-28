import pytest

from page_object.pages.login_page import LoginPage
from page_object.pages.dashboard_page import DashboardPage
from utils.data_generator import wrong_username, wrong_password
from fixtures.auth import ui_login


@pytest.mark.positive
class TestLogin:

    def test_login(self, browser, ui_login):
        page = DashboardPage(browser)
        page.check_dashboard_page_is_load()

    def test_logout(self, browser, ui_login):
        page = DashboardPage(browser)
        page.logout()
        page = LoginPage(browser)
        page.check_login_page_is_load()


@pytest.mark.negative
class TestLoginNegative:

    def test_wrong_username(self, browser, password):
        page = LoginPage(browser)
        page.open()
        page.check_login_page_is_load()
        page.log_in(
            wrong_username(),
            password
        )
        page.check_credentials_alert()

    def test_wrong_password(self, browser, username):
        page = LoginPage(browser)
        page.open()
        page.check_login_page_is_load()
        page.log_in(
            username,
            wrong_password()
        )
        page.check_credentials_alert()

