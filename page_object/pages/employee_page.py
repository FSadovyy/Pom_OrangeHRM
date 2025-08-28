from page_object.pages.main_page import MainPage
from page_object.locators.locators import EmployeePageLocators
from selenium.webdriver.common.keys import Keys
from retry import retry


class EmployeePage(MainPage):

    PAGE = ''

    def save_employee(self):
        self.wait_loader()
        self.wait_element_enabled(EmployeePageLocators.SAVE_BUTTON).click()

    def fill_first_name(self, first_name):
        self.wait_element_enabled(EmployeePageLocators.FIRST_NAME).send_keys(first_name)

    def fill_last_name(self, last_name):
        self.wait_element_enabled(EmployeePageLocators.LAST_NAME).send_keys(last_name)

    @retry(tries=2, delay=0.2)
    def fill_custom_id(self, custom_id):
        field = self.wait_element_enabled(EmployeePageLocators.EMPLOYEE_ID)
        self.wait_loader()
        field.click()
        field.send_keys(Keys.CONTROL + "a")
        field.send_keys(Keys.DELETE)
        field.send_keys(custom_id)
        self.wait_element_is_not_enabled(EmployeePageLocators.EMPLOYEE_ID_VALIDATION)

    def get_employee_id(self):
        return self.wait_element_enabled(EmployeePageLocators.EMPLOYEE_ID).get_attribute('value')

    def check_success_saved(self):
        self.check_success_popup('Successfully Saved')

    def fill_required_fields(self, *args):
        self.fill_first_name(args[0])
        self.fill_last_name(args[1])

    def create_employee(self, first_name, last_name, custom_id=None):
        self.fill_required_fields(first_name, last_name)
        if custom_id:
            self.fill_custom_id(custom_id)
        self.save_employee()
        self.check_success_saved()

    def check_first_name_validation(self):
        message = self.wait_element_enabled(EmployeePageLocators.FIRST_NAME_VALIDATION)
        assert message.text == 'Required', \
            f'Некорректный текст сообщения об ошибке: {message.text}'

    def check_last_name_validation(self):
        message = self.wait_element_enabled(EmployeePageLocators.LAST_NAME_VALIDATION)
        assert message.text == 'Required', \
            f'Некорректный текст сообщения об ошибке: {message.text}'

