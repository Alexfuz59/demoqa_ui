import allure
from base.base_page import BasePage
from config.links import LinksElement
from selenium.webdriver.support import expected_conditions as EC


class RadioButton(BasePage):
    PAGE_URL = LinksElement.RADIO_BUTTON
    YES_STATUS = ('xpath', '//input[@id="yesRadio"]')
    YES = ('xpath', '//label[@for="yesRadio"]')
    IMPRESSIVE_STATUS = ('xpath', '//input[@id="impressiveRadio"]')
    IMPRESSIVE = ('xpath', '//label[@for="impressiveRadio"]')
    NO_STATUS = ('xpath', '//label[@for="noRadio"]')

    @allure.step("Click radio button Yes")
    def check_click_yes(self):
        button_yes = self.wait.until(EC.element_to_be_clickable(self.YES))
        button_yes.click()
        assert self.driver.find_element(*self.YES_STATUS).is_selected(), 'Radio button Yes not selected'

    @allure.step("Click radio button impressive")
    def check_click_impressive(self):
        button_impressive = self.wait.until(EC.element_to_be_clickable(self.IMPRESSIVE))
        button_impressive.click()
        assert self.driver.find_element(*self.IMPRESSIVE_STATUS).is_selected(), 'Radio button Impressive not selected'

    @allure.step("Click radio button No")
    def check_button_no(self):
        button_no = self.wait.until(EC.visibility_of_element_located(self.NO_STATUS))
        assert button_no.is_enabled(), 'Radio button No not selected'
