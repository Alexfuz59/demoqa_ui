import allure
from base.base_page import BasePage
from config.links import LinkWidgets
from selenium.webdriver.support import expected_conditions as EC
from enums.error_enums import ErrorWidgets


class ToolTips(BasePage):
    PAGE_URL = LinkWidgets.TOOL_TIPS
    BUTTON_HOVER = ('xpath', '//button[@id="toolTipButton"]')
    INPUT_HOVER = ('xpath', '//input[@id="toolTipTextField"]')
    TOOLTIPS = ('xpath', '//div[@class="tooltip-inner"]')
    TEXT_CENTER = ('xpath', '//h1[@class="text-center"]')
    TOOLTIP_BUTTON = 'You hovered over the Button'
    TOOLTIP_INPUT = 'You hovered over the text field'

    @allure.step("Checking the button tooltip")
    def check_tool_tips_button(self):
        button = self.wait.until(EC.visibility_of_element_located(self.BUTTON_HOVER))
        self.action.move_to_element(button) \
                    .pause(1) \
                    .perform()
        tool_tips_text = self.wait.until(EC.visibility_of_element_located(self.TOOLTIPS)).text
        text_center = self.wait.until(EC.visibility_of_element_located(self.TEXT_CENTER))
        self.action.move_to_element(text_center).perform()
        self.wait.until(EC.invisibility_of_element_located(self.TOOLTIPS))
        assert tool_tips_text == self.TOOLTIP_BUTTON, ErrorWidgets.ERROR_TOOLTIP

    @allure.step("Checking the input tooltip")
    def check_tool_tips_input(self):
        input = self.wait.until(EC.visibility_of_element_located(self.INPUT_HOVER))
        self.action.move_to_element(input) \
                    .pause(1) \
                    .perform()
        tool_tips_text = self.wait.until(EC.visibility_of_element_located(self.TOOLTIPS)).text
        text_center = self.wait.until(EC.visibility_of_element_located(self.TEXT_CENTER))
        self.action.move_to_element(text_center).perform()
        self.wait.until(EC.invisibility_of_element_located(self.TOOLTIPS))
        assert tool_tips_text == self.TOOLTIP_INPUT, ErrorWidgets.ERROR_TOOLTIP

