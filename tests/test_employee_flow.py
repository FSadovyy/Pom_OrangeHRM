import pytest

from page_object.pages.dashboard_page import DashboardPage
from page_object.pages.employee_page import EmployeePage
from page_object.pages.personal_page import PersonalPage
from page_object.pages.pim_page import PimPage
from utils.data_generator import first_name as f, last_name as ln, custom_id as c
from fixtures.auth import ui_login


@pytest.fixture(scope='function')
def go_to_employee_page(browser, ui_login):
    page = PimPage(browser)
    page.open()
    page.click_add_employee()
    page = EmployeePage(browser)
    return page


@pytest.fixture(scope='function')
def new_employee(browser, go_to_employee_page):
    first_name, last_name, custom_id = f(), ln(), c()

    page = go_to_employee_page
    page.create_employee(first_name, last_name, custom_id)
    page = PersonalPage(browser)
    return page, first_name, last_name, custom_id


@pytest.mark.positive
class TestEmployeeFlow:

    def test_employee_flow(self, browser, ui_login):
        first_name, last_name, custom_id = f(), ln(), c()

        page = DashboardPage(browser)
        page.go_to_pim_page()
        page = PimPage(browser)
        page.click_add_employee()
        page = EmployeePage(browser)
        page.create_employee(first_name, last_name, custom_id)
        page = PersonalPage(browser)
        employee_id = page.get_employee_id()
        page.go_to_pim_page()
        page = PimPage(browser)
        page.search_existing_by_id(employee_id)
        page.go_to_edit_employee(employee_id)
        page = PersonalPage(browser)
        page.change_martial_status('Married')
        page.logout()

@pytest.mark.negative
class TestEmployeeNegative:

    def test_employee_with_empty_fields(self, browser, go_to_employee_page):
        page = go_to_employee_page
        page.fill_required_fields('', '')
        page.save_employee()
        page.check_first_name_validation()
        page.check_last_name_validation()

    def test_search_not_existing_employee(self, browser, go_to_employee_page):
        page = go_to_employee_page
        employee_id = page.get_employee_id()
        page.go_to_pim_page()
        page = PimPage(browser)
        page.search_not_existing_by_id(employee_id)

    def test_changes_saved(self, browser, new_employee):
        page, _, last_name, employee_id = new_employee

        new_last_name = last_name + "a"
        page.change_last_name(new_last_name)
        page.go_to_pim_page()
        page = PimPage(browser)
        page.search_existing_by_id(employee_id)
        page.check_last_name_in_table(new_last_name)

    def test_changes_not_saved(self, browser, new_employee):
        page, _, last_name, employee_id = new_employee

        new_last_name = last_name + "a"
        page.fill_last_name(new_last_name)
        page.go_to_pim_page()
        page = PimPage(browser)
        page.search_existing_by_id(employee_id)
        page.check_last_name_in_table(last_name)




