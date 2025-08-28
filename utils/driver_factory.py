from selenium import webdriver
from selenium.webdriver.chrome.options import Options as OptionsChrome
from selenium.webdriver.firefox.options import Options as OptionsFirefox


class DriverFactory:
    @staticmethod
    def get_driver(browser_name, settings):
        if browser_name == "chrome":
            options = OptionsChrome()

            if settings.HEADLESS:
                options.add_argument("--headless=new")
                options.add_argument("--screen-info={1920x1080}")
                options.add_argument("user-agent=Chrome/139.0.0.0")
            options.add_argument("--start-maximized")
            options.add_argument("--ignore-certificate-errors")
            options.add_argument("--whitelisted-ips")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-crash-reporter")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-setuid-sandbox")
            options.add_argument("--disable-background-timer-throttling")
            options.add_argument("--disable-gpu")
            options.add_argument("--disable-infobars")
            options.add_argument("--disable-oopr-debug-crash-dump")
            options.add_argument("--disable-notifications")
            options.add_argument("--incognito")
            options.add_argument("--enable-logging")
            options.add_argument("--disable-extensions")
            options.add_argument("--log-level=1")

            print("\nstart chrome browser for test..")
            driver = webdriver.Chrome(options=options)
            driver.maximize_window()
            return driver

        elif browser_name == "firefox":
            options = OptionsFirefox()

            if settings.HEADLESS:
                options.add_argument("--headless")
                options.add_argument("--width=1920")
                options.add_argument("--height=1080")
                options.add_argument("user-agent=Mozilla/5.0")
            options.add_argument("--start-maximized")
            options.add_argument("--disable-infobars")
            options.add_argument("--disable-extensions")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-application-cache")
            options.add_argument("--disable-gpu")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--log-level=1")

            print("\nstart firefox browser for test..")
            driver = webdriver.Firefox(options=options)
            driver.maximize_window()
            return driver

        raise Exception("Provide valid driver name")
