import allure
from base.base_page import BasePage
from config.links import LinksElement
from selenium.webdriver.support import expected_conditions as EC


class TextBox(BasePage):
    PAGE_URL = LinksElement.TEXTBOX
    USER_NAME = ('xpath', '//input[@id="userName"]')
    CURRENT_ADDRESS = ('xpath', '//textarea[@id="currentAddress"]')
    USER_EMAIL = ('xpath', '//input[@id="userEmail"]')
    PERMANENT_ADDRESS = ('xpath', '//textarea[@id="permanentAddress"]')
    BUTTON_SUBMIT = ('xpath', '//button[text()="Submit"]')
    DISPLAY_USER_NAME = ('xpath', '//p[@id="name"]')
    DISPLAY_USER_EMAIL = ('xpath', '//p[@id="email"]')
    DISPLAY_CURRENT_ADDRESS = ('xpath', '//p[@id="currentAddress"]')
    DISPLAY_PERMANENT_ADDRESS = ('xpath', '//p[@id="permanentAddress"]')

    @allure.step("Checking placeholders")
    def check_placeholder(self):
        placeholders = {self.USER_NAME: "Full Name",
                        self.CURRENT_ADDRESS: "Current Address",
                        self.USER_EMAIL: "name@example.com",
                        }
        for key, value in placeholders.items():
            input = self.wait.until(EC.presence_of_element_located(key))
            placeholder = input.get_attribute('placeholder')
            assert value == placeholder, f'Invalid placeholder: {value}'

    @allure.step("Set value in input user name")
    def set_value_user_name(self):
        input = self.wait.until(EC.presence_of_element_located(self.USER_NAME))
        value = self.fake.first_name()
        input.send_keys(value)
        self.click_button_submit()
        value_input = self.wait.until(EC.presence_of_element_located(self.DISPLAY_USER_NAME)).text
        assert value in value_input, 'Invalid user name'

    @allure.step("Set value in input current address")
    def set_value_current_address(self):
        input = self.wait.until(EC.presence_of_element_located(self.CURRENT_ADDRESS))
        input.clear()
        value = self.fake.address()
        input.send_keys(value)
        self.click_button_submit()
        value_input = self.wait.until(EC.presence_of_element_located(self.DISPLAY_CURRENT_ADDRESS)).text
        value = value.replace('\n', " ").strip()
        value_input = value_input.replace('Current Address :', " ").strip()
        assert value == value_input, 'Invalid current address'

    @allure.step("Set value in input permanent address(")
    def set_value_permanent_address(self):
        input = self.wait.until(EC.presence_of_element_located(self.PERMANENT_ADDRESS))
        value = self.fake.address()
        input.send_keys(value)
        self.click_button_submit()
        value_input = self.wait.until(EC.presence_of_element_located(self.DISPLAY_PERMANENT_ADDRESS)).text
        value = value.replace('\n', " ").strip()
        value_input = value_input.replace('Permananet Address :', " ").strip()
        assert value == value_input, 'Invalid permanent address'

    @allure.step("Set value in input user email")
    def set_value_user_email(self):
        input = self.wait.until(EC.presence_of_element_located(self.USER_EMAIL))
        value = self.fake.ascii_free_email()
        input.send_keys(value)
        self.click_button_submit()
        value_input = self.wait.until(EC.presence_of_element_located(self.DISPLAY_USER_EMAIL)).text
        assert value in value_input, 'Invalid user email'

    @allure.step("Click button submit")
    def click_button_submit(self):
        button = self.driver.find_element(*self.BUTTON_SUBMIT)
        self.driver.execute_script("arguments[0].click();", button)










