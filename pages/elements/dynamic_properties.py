import allure
from base.base_page import BasePage
from config.links import LinksElement
from selenium.webdriver.support import expected_conditions as EC


class DynamicProperties(BasePage):
    PAGE_URL = LinksElement.DYNAMIC_PROPERTIES
    ENABLE = ('xpath', '//button[@id="enableAfter"]')
    COLOR_CHANGE = ('xpath', '//button[@class="mt-4 text-danger btn btn-primary"]')
    VISIBLE_AFTER = ('xpath', '//button[@id="visibleAfter"]')

    @allure.step("Click enable button")
    def click_enable_button(self):
        self.wait.until(EC.element_to_be_clickable(self.ENABLE)).click()

    @allure.step("Click color change button")
    def click_color_change_button(self):
        self.wait.until(EC.presence_of_element_located(self.COLOR_CHANGE)).click()

    @allure.step("Click visible after button")
    def click_visible_after_button(self):
        self.wait.until(EC.visibility_of_element_located(self.VISIBLE_AFTER)).click()