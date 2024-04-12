import allure
from base.base_page import BasePage
from config.links import LinksElement
from selenium.webdriver.support import expected_conditions as EC


class Buttons(BasePage):
    PAGE_URL = LinksElement.BUTTONS
    DOUBLE_BUTTON = ('xpath', '//button[@id="doubleClickBtn"]')
    CHECK_DOUBLE_CLICK = ('xpath', '//p[@id="doubleClickMessage"]')
    RIGHT_BUTTON = ('xpath', '//button[@id="rightClickBtn"]')
    CHECK_RIGHT_CLICK = ('xpath', '//p[@id="rightClickMessage"]')
    CLICK_ME_BUTTON = ('xpath', '//button[text()="Click Me"]')
    CHECK_CLICK_ME_BUTTON = ('xpath', '//p[@id="dynamicClickMessage"]')

    @allure.step("Double click")
    def double_click(self):
        button = self.wait.until(EC.element_to_be_clickable(self.DOUBLE_BUTTON))
        self.action.move_to_element(button).double_click(button).perform()

    @allure.step("Checking double click")
    def check_double_click(self):
        text_double_click = self.wait.until(EC.visibility_of_element_located(self.CHECK_DOUBLE_CLICK)).text
        assert text_double_click == 'You have done a double click', 'Double-click button broken'

    @allure.step("Right button click")
    def right_button_click(self):
        button = self.wait.until(EC.element_to_be_clickable(self.RIGHT_BUTTON))
        self.action.context_click(button).perform()

    @allure.step("Checking right click")
    def check_right_click(self):
        text_right_click = self.wait.until(EC.visibility_of_element_located(self.CHECK_RIGHT_CLICK)).text
        assert text_right_click == 'You have done a right click', 'Right click button broken'

    @allure.step("Click a button with dynamic attributes")
    def dynamic_button_click(self):
        self.wait.until(EC.element_to_be_clickable(self.CLICK_ME_BUTTON)).click()

    @allure.step("Checking button with dynamic attributes")
    def check_dynamic_click(self):
        text_dynamic_click = self.wait.until(EC.visibility_of_element_located(self.CHECK_CLICK_ME_BUTTON)).text
        assert text_dynamic_click == 'You have done a dynamic click', 'Dynamic button broken'




