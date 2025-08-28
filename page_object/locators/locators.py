from selenium.webdriver.common.by import By


class BasePageLocators:
    LOADER = (By.CSS_SELECTOR, ".oxd-form-loader")


class LoginPageLocators:
    USERNAME = (By.CSS_SELECTOR, "[placeholder='Username']")
    PASSWORD = (By.CSS_SELECTOR, '[placeholder="Password"]')
    LOGIN_BUTTON = (By.XPATH, '//button[@type="submit" and contains(@class, "login")]')
    LOGIN_TITLE = (By.XPATH, '//h5[contains(@class, "login-title")]')
    CREDENTIALS_ALERT = (By.CSS_SELECTOR, "[role = 'alert']")


class MainPageLocators:
    USER_DROPDOWN = (By.CSS_SELECTOR, '.oxd-userdropdown-name')
    LOGOUT = (By.XPATH, '//a[@class="oxd-userdropdown-link" and contains(text(),"Logout")]')
    MENU_PIM = (By.XPATH, '//*[contains(@class, "main-menu-item") and text()="PIM"]')
    SUCCESS_POPUP = (By.XPATH, '//div[contains(@class, "toast-content--success")]/p[contains(@class, "toast-message")]')
    INFO_POPUP = (By.XPATH, '//div[contains(@class, "toast-content--info")]/p[contains(@class, "toast-message")]')


class DashboardPageLocators:
    DASHBOARD_HEADER = (By.XPATH, '//h6[contains(@class, "topbar-header") and text()="Dashboard"]')


class PimPageLocators:
    ADD_BUTTON = (By.CSS_SELECTOR, '[class="oxd-icon bi-plus oxd-button-icon"]')
    SEARCH_BUTTON = (By.XPATH, "//button[contains(@class, 'orangehrm-left-space')]")
    EMPLOYEE_ID = (By.XPATH, "//label[text()='Employee Id']/ancestor::div[contains(@class, 'input-field')]//input")
    CELL_ID = (By.XPATH, "//div[@role='cell'][2]/div")
    CELL_LAST_NAME = (By.XPATH, "//div[@role='cell'][4]/div")
    EDIT_BUTTON = "//div[contains(text(), '{item}')]/ancestor::div[contains(@class, " \
                  "'oxd-table-row')]//i[contains(@class, 'pencil')]"  # Требует специального метода


class EmployeePageLocators:
    FIRST_NAME = (By.CSS_SELECTOR, "[placeholder='First Name']")
    LAST_NAME = (By.CSS_SELECTOR, "[placeholder='Last Name']")
    EMPLOYEE_ID = (By.XPATH, "//label[text()='Employee Id']/ancestor::div[contains(@class, 'input-field')]//input")
    SAVE_BUTTON = (By.CSS_SELECTOR, "[type='submit']")
    FIRST_NAME_VALIDATION = (By.XPATH, "//input[@placeholder='First Name']"
                                       "/ancestor::div[contains(@class, 'bottom-space')]//span")
    LAST_NAME_VALIDATION = (By.XPATH, "//input[@placeholder='Last Name']"
                                      "/ancestor::div[contains(@class, 'bottom-space')]//span")
    EMPLOYEE_ID_VALIDATION = (By.XPATH, "//input[@placeholder='Employee Id']"
                                        "/ancestor::div[contains(@class, 'bottom-space')]//span")


class PersonalPageLocators(EmployeePageLocators):
    EMPLOYEE_ID = (By.XPATH, "//label[text()='Employee Id']/ancestor::div[contains(@class, 'input-field')]//input")
    SAVE_NON_CUSTOM_BUTTON = (By.XPATH, "//div[contains(@class, 'horizontal-padding')]//button[@type='submit']")
    MARTIAL_STATUS = (By.XPATH, "//label[text()='Marital Status']/ancestor::div[contains(@class, 'bottom-space')]"
                                "//div[@class='oxd-select-text-input']")
    DROPDOWN_OPTION = "//div[@role='option']/span[text()='{text}']"  # Требует специального метода

