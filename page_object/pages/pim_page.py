from page_object.pages.main_page import MainPage
from page_object.locators.locators import PimPageLocators
from selenium.webdriver.common.by import By


class PimPage(MainPage):
    PAGE = '/pim/viewEmployeeList'

    def get_employee_edit_button(self, item):
        return self.wait_element_enabled((By.XPATH, PimPageLocators.EDIT_BUTTON.format(item=item)))

    def click_add_employee(self):
        self.wait_element_enabled(PimPageLocators.ADD_BUTTON).click()

    def enter_employee_id(self, employee_id):
        self.wait_element_enabled(PimPageLocators.EMPLOYEE_ID).send_keys(employee_id)

    def click_search_employee(self):
        self.wait_element_enabled(PimPageLocators.SEARCH_BUTTON).click()

    def check_number_of_records(self, number):
        try:
            self.wait.until(lambda x: len(x.find_elements(*PimPageLocators.CELL_ID)) == number)
        except:
            raise Exception(f'Неверное колличество строк в таблице: {number}')

    def search_existing_by_id(self, employee_id):
        self.enter_employee_id(employee_id)
        self.click_search_employee()
        self.check_number_of_records(1)

    def search_not_existing_by_id(self, employee_id):
        self.enter_employee_id(employee_id)
        self.click_search_employee()
        self.check_number_of_records(0)

    def check_last_name_in_table (self, last_name):
        text = self.wait_element_enabled(PimPageLocators.CELL_LAST_NAME).text
        assert text == last_name,\
            f'Неверный текст в ячейке у работника с last name {last_name}: {text}'

    def check_id_in_table(self, employee_id):
        text = self.wait_element_enabled(PimPageLocators.CELL_ID).text
        assert text == employee_id, \
            f'Неверный текст в ячейке у работника с id {employee_id}: {text}'

    def go_to_edit_employee(self, employee_id):
        self.check_id_in_table(employee_id)
        self.get_employee_edit_button(employee_id).click()

    def check_no_records(self):
        self.wait.until(lambda x: len(x.find_elements(*PimPageLocators.CELL_ID)) == 0)
        self.check_info_popup('No Records Found')






