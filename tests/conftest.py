import pytest

from utils.driver_factory import DriverFactory
from config.settings import Settings


def pytest_addoption(parser):
    parser.addoption('--browser_name',
                     action='store',
                     default="chrome",
                     help="Choose one: '--browser_name=chrome', '--browser_name=firefox'")


@pytest.fixture(scope='function')
def username():
    return Settings.USERNAME


@pytest.fixture(scope='function')
def password():
    return Settings.PASSWORD


@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption("browser_name")

    if browser_name not in ("chrome", "firefox"):
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    browser = DriverFactory.get_driver(browser_name, Settings)
    browser.implicitly_wait(Settings.TIMEOUT)

    yield browser
    browser.close()
    browser.quit()
