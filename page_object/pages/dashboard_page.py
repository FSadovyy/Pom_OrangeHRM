from page_object.pages.main_page import MainPage
from page_object.locators.locators import DashboardPageLocators


class DashboardPage(MainPage):
    PAGE = '/dashboard/index'

    def check_dashboard_page_is_load(self):
        self.wait_element_enabled(DashboardPageLocators.DASHBOARD_HEADER)
