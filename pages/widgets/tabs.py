import allure
from base.base_page import BasePage
from config.links import LinkWidgets
from selenium.webdriver.support import expected_conditions as EC
from enums.error_enums import ErrorWidgets


class Tabs(BasePage):
    PAGE_URL = LinkWidgets.TABS
    WHAT = ('xpath', '//a[@id="demo-tab-what"]')
    ORIGIN = ('xpath', '//a[@id="demo-tab-origin"]')
    USE = ('xpath', '//a[@id="demo-tab-use"]')
    MORE = ('xpath', '//a[@id="demo-tab-more"]')
    MASSAGE_WHAT = ('xpath', '(//p[@class="mt-3"])[1]')
    MASSAGE_ORIGIN = ('xpath', '(//p[@class="mt-3"])[2]')
    MASSAGE_USE = ('xpath', '(//p[@class="mt-3"])[3]')
    TEXT_ORIGIN = "Contrary to popular belief, Lorem Ipsum is not simply random text. \
    It has roots in a piece of classical Latin literature from 45 BC"
    TEXT_USE = "It is a long established fact that a reader will be distracted by the \
    readable content of a page when looking at its layout."
    TEXT_WHAT = "Lorem Ipsum is simply dummy text of the printing and typesetting \
    industry. Lorem Ipsum has been"

    @allure.step("Click tab origin")
    def click_origin(self):
        self.wait.until(EC.element_to_be_clickable(self.ORIGIN)).click()

    @allure.step("Checking message origin")
    def check_message_origin(self):
        message = self.wait.until(EC.visibility_of_element_located(self.MASSAGE_ORIGIN)).text
        assert self.TEXT_ORIGIN in message, ErrorWidgets.INVALID_MESSAGE_TAB

    @allure.step("Click tab use")
    def click_use(self):
        self.wait.until(EC.element_to_be_clickable(self.USE)).click()

    @allure.step("Checking message use")
    def check_message_use(self):
        message = self.wait.until(EC.visibility_of_element_located(self.MASSAGE_USE)).text
        assert self.TEXT_USE in message, ErrorWidgets.INVALID_MESSAGE_TAB

    @allure.step("Click tab what")
    def click_what(self):
        self.wait.until(EC.element_to_be_clickable(self.WHAT)).click()

    @allure.step("Checking message what")
    def check_message_what(self):
        message = self.wait.until(EC.visibility_of_element_located(self.MASSAGE_WHAT)).text
        assert self.TEXT_WHAT in message, ErrorWidgets.INVALID_MESSAGE_TAB

    @allure.step("Checking inactive tab more")
    def check_tab_more(self):
        tab_more = self.wait.until(EC.presence_of_element_located(self.MORE)).is_enabled()
        assert tab_more, ErrorWidgets.ERROR_ACTIV_TAB
