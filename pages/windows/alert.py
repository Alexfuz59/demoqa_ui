import allure
from base.base_page import BasePage
from config.links import LinkWindows
from selenium.webdriver.support import expected_conditions as EC


class Alert(BasePage):
    PAGE_URL = LinkWindows.ALERT
    BUTTON_ALERT_SEE = ('xpath', '//button[@id="alertButton"]')
    BUTTON_ALERT_TIME = ('xpath', '//button[@id="timerAlertButton"]')
    BUTTON_ALERT_CONFIRM = ('xpath', '//button[@id="confirmButton"]')
    BUTTON_ALERT_PROMT = ('xpath', '//button[@id="promtButton"]')
    RESULT_ALERT_CONFIRM = ('xpath', '//span[@id="confirmResult"]')
    RESULT_ALERT_PROMT = ('xpath', '//span[@id="promptResult"]')

    @allure.step("Click button alert see")
    def click_button_alert_see(self):
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_ALERT_SEE)).click()

    @allure.step("Click button alert time")
    def click_button_alert_time(self):
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_ALERT_TIME)).click()

    @allure.step("Click button alert confirme")
    def click_button_alert_confirme(self):
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_ALERT_CONFIRM)).click()

    @allure.step("Click button alert promt")
    def click_button_alert_promt(self):
        button = self.wait.until(EC.element_to_be_clickable(self.BUTTON_ALERT_PROMT))
        self.driver.execute_script("arguments[0].click();", button)

    @allure.step("Checking alert see")
    def check_alert_see(self):
        alert = self.wait.until(EC.alert_is_present())
        alert_message = alert.text
        alert.accept()
        assert alert_message in "You clicked a button", f'Invalid message in the alerts, message: {alert_message}'

    @allure.step("Checking alert time")
    def check_alert_time(self):
        alert = self.wait.until(EC.alert_is_present())
        alert_message = alert.text
        alert.accept()
        assert alert_message in "This alert appeared after 5 seconds", f'Invalid message in the alerts, message: {alert_message}'

    @allure.step("Checking alert confirme")
    def check_alert_confirme(self):
        alert = self.wait.until(EC.alert_is_present())
        alert_message = alert.text
        alert.accept()
        result_alert = self.wait.until(EC.visibility_of_element_located(self.RESULT_ALERT_CONFIRM)).text
        assert alert_message in "Do you confirm action?", f'Invalid message in the alerts, message: {alert_message}'
        assert result_alert == "You selected Ok", 'Incorrect result of the alerts'

    @allure.step("Checking alert promt")
    def check_alert_promt(self):
        alert = self.wait.until(EC.alert_is_present())
        alert_message = alert.text
        name = self.fake.first_name()
        alert.send_keys(name)
        alert.accept()
        result_alert = self.wait.until(EC.visibility_of_element_located(self.RESULT_ALERT_PROMT)).text
        assert alert_message in "Please enter your name", f'Invalid message in the alerts, message: {alert_message}'
        assert result_alert == f'You entered {name}', f'Invalid value:{name} entered the alerts:{result_alert}'