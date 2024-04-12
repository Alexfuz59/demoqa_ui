import allure
from base.base_page import BasePage
from config.links import LinksElement
from selenium.webdriver.support import expected_conditions as EC


class Checkbox(BasePage):
    PAGE_URL = LinksElement.CHECKBOX
    TOGGLE = lambda self, id: ('xpath', f'(//button[@title = "Toggle"])[{id}]')
    CHECKBOX_CLICK_HOME = ('xpath', '(//span[@class="rct-checkbox"])[1]')
    CHECKBOX_STATUS = lambda self, id: ('xpath', f'(//input[@type="checkbox"])[{id}]')

    @allure.step("Click checkbox home")
    def click_checkbox_home(self):
        self.wait.until(EC.visibility_of_element_located(self.CHECKBOX_CLICK_HOME)).click()

    @allure.step("Open all toggle")
    def open_all_toggle(self):
        for i in range(1, 6):
            self.wait.until(EC.element_to_be_clickable(self.TOGGLE(i))).click()

    @allure.step("Checking all checkbox")
    def check_all_checkbox(self):
        for i in range(1, 10):
            checkbox = self.wait.until(EC.presence_of_element_located(self.CHECKBOX_STATUS(i)))
            assert checkbox.is_selected(), f'Checkbox {i} not selected'





