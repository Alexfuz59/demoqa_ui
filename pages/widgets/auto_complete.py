import allure
from base.base_page import BasePage
from config.links import LinkWidgets
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from enums.error_enums import ErrorWidgets


class AutoComplete(BasePage):
    PAGE_URL = LinkWidgets.AUTO_COMPLETE
    COLOR_LIST = ['Red', 'Blue', 'Yellow', 'Purple', 'White', 'Voilet', 'Magenta']
    MULTIPLE = ('xpath', '//input[@id="autoCompleteMultipleInput"]')
    COLORS_IN_MULTIPLE = ('xpath', '//div[@class="css-12jo7m5 auto-complete__multi-value__label"]')
    DELETE_SELECT = lambda self, index_bttn: ('xpath', f'(//div[contains(@class, "css-xb97g8")])[{index_bttn}]')
    INPUT_SINGLE_COLOR = ('xpath', '//input[@id="autoCompleteSingleInput"]')
    SELECTED_INPUT_SINGLE_COLOR = ('xpath', '//div[contains(@class, "css-1uccc91-singleValue")]')
    COLOR_IN_MULTIPLE = lambda self, color: ('xpath', f'//div[text()="{color}"]')

    @allure.step("Selected colors in Multiselect")
    def color_in_multiple(self):
        selected_elem = self.driver.find_elements(*self.COLORS_IN_MULTIPLE)
        selected_color = []
        for i in selected_elem:
            selected_color.append(i.text)
        return selected_color

    @allure.step("Multiselect empty check")
    def check_multiple_empty(self):
        total = len(self.color_in_multiple())
        assert total == 0, ErrorWidgets.ERROR_MULTISELECT_EMPTY

    @allure.step("Set values in Multiselect")
    def input_in_multiple(self):
        for color in self.COLOR_LIST:
            multiple = self.wait.until(EC.visibility_of_element_located(self.MULTIPLE))
            multiple.send_keys(color)
            multiple.send_keys(Keys.ENTER)
            self.wait.until(EC.visibility_of_element_located(self.COLOR_IN_MULTIPLE(color)))
            selected_color = self.color_in_multiple()
            assert color in selected_color, ErrorWidgets.ERROR_MULTISELECT_VALUE(color)

    @allure.step("Delete value in Multiselect")
    def delete_selected_multiple(self):
        len_multiple = len(self.color_in_multiple())
        for index_bttn in range(len_multiple, 1, -1):
            button_delete = self.wait.until(EC.visibility_of_element_located(self.DELETE_SELECT(index_bttn)))
            self.driver.execute_script("arguments[0].click();", button_delete)

    @allure.step("Set values in input single color")
    def check_input_single_color(self):
        for color in self.COLOR_LIST:
            input = self.wait.until(EC.visibility_of_element_located(self.INPUT_SINGLE_COLOR))
            input.send_keys(color)
            input.send_keys(Keys.ENTER)
            input.click()
            selected = self.wait.until(EC.visibility_of_element_located(self.SELECTED_INPUT_SINGLE_COLOR)).text
            assert color == selected, ErrorWidgets.ERROR_MULTISELECT_SINGLE(color)

