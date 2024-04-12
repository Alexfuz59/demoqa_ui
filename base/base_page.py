import allure
from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as AC
from faker import Faker
from config.links import Links


class BasePage:
    PAGE_URL = None

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=8, poll_frequency=1)
        self.action = AC(driver)
        self.fake = Faker()

    @allure.step('Open URL')
    def open(self):
        self.driver.get(self.PAGE_URL)

    @allure.step('Check is opened URL')
    def is_opened(self):
        try:
            self.wait.until(EC.url_to_be(self.PAGE_URL))
        except TimeoutException:
            raise AssertionError("Wrong page opened")

    @allure.step('Checking open start page')
    def check_open_start_page(self):
        assert self.driver.current_url == Links.START_PAGE, "Wrong page opened"

    @allure.step('Scroll to element')
    def scroll_to_element(self, element):
        self.action.scroll_to_element(element).perform()
        self.driver.execute_script("""
        window.scrollTo({
            top: window.scrollY + 700,
        });
        """)
