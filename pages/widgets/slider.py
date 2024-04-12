import allure
from base.base_page import BasePage
from config.links import LinkWidgets
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys


class Slider(BasePage):
    PAGE_URL = LinkWidgets.SLIDER
    SLIDER = ('xpath', '//input[@type="range"]')
    VALUE_SLIDER =('xpath', '//input[@id="sliderValue"]')

    @allure.step("Checking slider")
    def check_moving_slider(self, value):
        slider = self.wait.until(EC.visibility_of_element_located(self.SLIDER))
        slider.click()
        initial_value = int(slider.get_attribute("value"))
        if value > initial_value:
            offset = (value - initial_value)
            for _ in range(offset):
                slider.send_keys(Keys.ARROW_RIGHT)
        elif value < initial_value:
            offset = (initial_value - value)
            for _ in range(offset):
                slider.send_keys(Keys.ARROW_LEFT)
        elif value == initial_value:
            pass
        slider_value = self.wait.until(EC.visibility_of_element_located(self.VALUE_SLIDER))
        assert value == int(slider.get_attribute("value")), 'Wrong slider value'
        assert value == int(slider_value.get_attribute("value")), 'Wrong slider value'






