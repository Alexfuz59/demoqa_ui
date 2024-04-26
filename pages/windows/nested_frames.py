import allure
from base.base_page import BasePage
from config.links import LinkWindows
from selenium.webdriver.support import expected_conditions as EC
from enums.error_enums import ErrorWindows


class NestedFrames(BasePage):
    PAGE_URL = LinkWindows.NESTED_FRAMES
    FRAME_FATHER =('xpath', '//iframe[@id="frame1"]')
    FRAME_CHILDREN = ('xpath', '//iframe')
    TEXT_FRAME_FATHER = ('xpath', '//body')
    TEXT_FRAME_CHILDREN = ('xpath', '//p')

    @allure.step('Checking a nonstandard frames')
    def check_nested_frames(self):
        self.wait.until(EC.frame_to_be_available_and_switch_to_it(self.FRAME_FATHER))
        frame_father = self.wait.until(EC.visibility_of_element_located(self.TEXT_FRAME_FATHER)).text
        self.wait.until(EC.frame_to_be_available_and_switch_to_it(self.FRAME_CHILDREN))
        frame_children = self.wait.until(EC.visibility_of_element_located(self.TEXT_FRAME_CHILDREN)).text
        self.driver.switch_to.default_content()
        self.driver.switch_to.default_content()
        assert frame_father == "Parent frame", ErrorWindows.ERROR_FRAME
        assert frame_children == "Child Iframe", ErrorWindows.ERROR_FRAME