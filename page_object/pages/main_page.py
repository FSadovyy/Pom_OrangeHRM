from page_object.locators.locators import MainPageLocators
from page_object.pages.base_page import BasePage


class MainPage(BasePage):

    def click_user(self):
        self.wait_element_enabled(MainPageLocators.USER_DROPDOWN).click()

    def click_logout(self):
        self.wait_element_enabled(MainPageLocators.LOGOUT).click()

    def go_to_pim_page(self):
        self.wait_element_enabled(MainPageLocators.MENU_PIM).click()

    def check_success_popup(self, text):
        popup = self.wait_element_enabled(MainPageLocators.SUCCESS_POPUP)
        assert popup.text == text, \
            f'Некорректный текст сообщения об успехе: {popup.text}'

    def check_info_popup(self, text):
        popup = self.wait_element_enabled(MainPageLocators.INFO_POPUP)
        assert popup.text == text, \
            f'Некорректный текст инфо-сообщения: {popup.text}'

    def logout(self):
        self.click_user()
        self.click_logout()
