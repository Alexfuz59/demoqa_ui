import allure
from base.base_page import BasePage
from config.links import LinkWindows
from selenium.webdriver.support import expected_conditions as EC


class Frame(BasePage):
    PAGE_URL = LinkWindows.FRAMES
    IFRAME_1 = ('xpath', '//iframe[@id="frame1"]')
    IFRAME_2 = ('xpath', '//iframe[@id="frame2"]')
    TEXT_IFRAME1 = ('xpath', '//h1[@id="sampleHeading"]')
    MESSAGE = "This is a sample page"

    @allure.step("Checking frame 1")
    def check_iframe1(self):
        iframe = self.wait.until(EC.visibility_of_element_located(self.IFRAME_1))
        self.driver.switch_to.frame(iframe)
        text = self.wait.until(EC.visibility_of_element_located(self.TEXT_IFRAME1)).text
        self.driver.switch_to.default_content()
        assert text == self.MESSAGE, 'Invalid message to frame'

    @allure.step("Checking frame 2")
    def check_iframe2(self):
        iframe = self.wait.until(EC.visibility_of_element_located(self.IFRAME_2))
        self.driver.switch_to.frame(iframe)
        text = self.wait.until(EC.visibility_of_element_located(self.TEXT_IFRAME1)).text
        self.driver.switch_to.default_content()
        assert text == self.MESSAGE, 'Invalid message to frame'
