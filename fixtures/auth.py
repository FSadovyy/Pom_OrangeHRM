import pytest
from page_object.pages.login_page import LoginPage


@pytest.fixture(scope='function')
def ui_login(browser, username, password):
    page = LoginPage(browser)
    page.open()
    page.check_login_page_is_load()
    page.log_in(
        username,
        password
    )
    yield
