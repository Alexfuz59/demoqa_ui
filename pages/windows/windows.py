import allure
from base.base_page import BasePage
from config.links import LinkWindows
from selenium.webdriver.support import expected_conditions as EC
from enums.error_enums import ErrorWindows


class Windows(BasePage):
    PAGE_URL = LinkWindows.WINDOWS
    BUTTON_NEW_TAB = ('xpath', '//button[@id="tabButton"]')
    BUTTON_NEW_WINDOW = ('xpath', '//button[@id="windowButton"]')
    BUTTON_WINDOW_MESSAGE = ('xpath', '//button[@id="messageWindowButton"]')
    TEXT_NEW_TUB = ('xpath', '//h1[@id="sampleHeading"]')
    MESSAGE_NEW_OBJECT = 'This is a sample page'

    @allure.step("Click button new tab")
    def click_button_new_tab(self):
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_NEW_TAB)).click()

    @allure.step("Click button new window")
    def click_button_new_window(self):
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_NEW_WINDOW)).click()

    @allure.step("Click button window message")
    def click_button_window_message(self):
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_WINDOW_MESSAGE)).click()

    @allure.step("Checking new tab")
    def check_new_tab(self):
        old_tub = self.driver.current_window_handle
        self.click_button_new_tab()
        self.wait.until(EC.number_of_windows_to_be(2))
        tubs = self.driver.window_handles
        new_tub = tubs[1]
        self.driver.switch_to.window(new_tub)
        switch_new_tub = self.driver.current_window_handle
        text_new_tub = self.wait.until(EC.visibility_of_element_located(self.TEXT_NEW_TUB)).text
        self.driver.close()
        self.driver.switch_to.window(old_tub)
        assert old_tub != switch_new_tub, ErrorWindows.ERROR_NEW_TAB
        assert text_new_tub == self.MESSAGE_NEW_OBJECT, ErrorWindows.ERROR_OPEN_TAB

    @allure.step("Checking new window")
    def check_new_window(self):
        old_window = self.driver.current_window_handle
        self.click_button_new_window()
        self.wait.until(EC.number_of_windows_to_be(2))
        windows = self.driver.window_handles
        new_window = windows[1]
        self.driver.switch_to.window(new_window)
        switch_new_window = self.driver.current_window_handle
        text_new_window = self.wait.until(EC.visibility_of_element_located(self.TEXT_NEW_TUB)).text
        self.driver.close()
        self.driver.switch_to.window(old_window)
        assert old_window != switch_new_window, ErrorWindows.ERROR_NEW_WINDOW
        assert text_new_window == self.MESSAGE_NEW_OBJECT, ErrorWindows.ERROR_OPEN_WINDOW

    @allure.step("Checking window message")
    def check_window_message(self):
        old_window = self.driver.current_window_handle
        self.click_button_window_message()
        self.wait.until(EC.number_of_windows_to_be(2))
        windows = self.driver.window_handles
        new_window = windows[1]
        self.driver.switch_to.window(new_window)
        switch_new_window = self.driver.current_window_handle
        self.driver.close()
        assert old_window != switch_new_window, ErrorWindows.ERROR_OPEN_WINDOW_MESSAGE

