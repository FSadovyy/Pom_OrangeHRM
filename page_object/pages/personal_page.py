from page_object.pages.main_page import MainPage
from page_object.locators.locators import PersonalPageLocators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class PersonalPage(MainPage):
    PAGE = ''

    def get_employee_id(self):
        return self.wait_element_enabled(PersonalPageLocators.EMPLOYEE_ID).get_attribute('value')

    def get_dropdown_option_by_text(self, text):
        return self.wait_element_enabled((By.XPATH, PersonalPageLocators.DROPDOWN_OPTION.format(text=text)))

    def fill_last_name(self, last_name):
        self.wait_loader()
        field = self.wait_element_enabled(PersonalPageLocators.LAST_NAME)
        field.click()
        field.send_keys(Keys.CONTROL + "a")
        field.send_keys(Keys.DELETE)
        field.send_keys(last_name)

    def check_success_updated(self):
        self.check_success_popup('Successfully Updated')

    def change_last_name(self, last_name):
        self.fill_last_name(last_name)
        self.save_non_custom_data()
        self.check_success_updated()
        current_data = self.wait_element_enabled(PersonalPageLocators.LAST_NAME).get_attribute('value')
        assert current_data == last_name, \
            f"Неверный Last Name, должен быть {last_name}, а не {current_data}"

    def change_martial_status(self, status: str):
        dropdown = self.wait_element_enabled(PersonalPageLocators.MARTIAL_STATUS)
        self.wait_loader()
        dropdown.click()
        option = self.get_dropdown_option_by_text(status)
        option.click()
        self.save_non_custom_data()
        self.check_success_updated()
        assert dropdown.text == status,\
            f"Неверный Martial Status, должен быть {status}, а не {dropdown.text}"

    def save_non_custom_data(self):
        self.wait_element_enabled(PersonalPageLocators.SAVE_NON_CUSTOM_BUTTON).click()
