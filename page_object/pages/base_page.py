from abc import ABC
from config.settings import Settings
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from page_object.locators.locators import BasePageLocators
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException


class BasePage(ABC):
    PAGE = str
    BASE_URL = Settings.BASE_URL

    def __init__(self, browser):
        self.url = self.BASE_URL + self.PAGE
        self.browser = browser
        self.wait = WebDriverWait(self.browser, Settings.TIMEOUT)

    def wait_element_enabled(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator), message=f'{locator} не найден по таймауту!')

    def wait_element_is_not_enabled(self, locator):
        return self.wait.until_not(EC.element_to_be_clickable(locator), message=f'{locator} найден по таймауту!')

    def wait_loader(self):

        """Предотвращает клик по спиннеру в Firefox"""

        self.wait.until(EC.invisibility_of_element(BasePageLocators.LOADER))

    def open(self) -> None:
        self.browser.get(self.url)
