import allure
from base.base_page import BasePage
from config.links import LinkWidgets
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select


class SelectMenu(BasePage):
    PAGE_URL = LinkWidgets.SELECT_MENU
    INPUT_SELECT_VALUE = ('xpath', '//input[@id="react-select-2-input"]')
    VALUE_SELECT_OPTIONS = lambda self, text: ('xpath',  f'//div[text()="{text}"]')
    INPUT_GENDERS = ('xpath', '//input[@id="react-select-3-input"]')
    VALUE_SELECT_GENDERS = lambda self, text: ('xpath', f'//div[text()="{text}"]')
    COLORS_DROPDOWN = ('xpath', '//select[@id="oldSelectMenu"]')
    MULTISELECT = ('xpath', '//input[@id="react-select-4-input"]')
    COLORS_IN_MULTIPLE = ('xpath', '//div[@class="css-12jo7m5"]')
    DELETE_SELECT = lambda self, index_bttn: ('xpath', f'(//div[contains(@class, "css-xb97g8")])[{index_bttn}]')
    CARS_MULTISELECT = ('xpath', '//select[@id="cars"]')
    COLORS_LIST = ['Red', 'Blue', 'Green', 'Black']
    LIST_SELECT_DROPDOWN_OPTION = ["Group 1, option 1", "Group 1, option 2", "Group 2, option 1", "Group 2, option 2", "A root option", "Another root option"]
    LIST_SELECT_DROPDOWN_GENDERS = ['Dr.', 'Mr.', 'Ms.', 'Mrs.', 'Prof.', 'Other']

    @allure.step("Checking dropdown select value")
    def check_dropdown_select_value(self):
        input = self.wait.until(EC.visibility_of_element_located(self.INPUT_SELECT_VALUE))
        for select in self.LIST_SELECT_DROPDOWN_OPTION:
            input.send_keys(select)
            input.send_keys(Keys.ENTER)
            self.wait.until(EC.visibility_of_element_located(self.VALUE_SELECT_OPTIONS(select)))

    @allure.step("Checking dropdown genders")
    def check_dropdown_genders(self):
        input = self.wait.until(EC.visibility_of_element_located(self.INPUT_GENDERS))
        for select in self.LIST_SELECT_DROPDOWN_GENDERS:
            input.send_keys(select)
            input.send_keys(Keys.ENTER)
            self.wait.until(EC.visibility_of_element_located(self.VALUE_SELECT_GENDERS(select)))

    @allure.step("Checking dropdown colors")
    def check_colors_dropdown(self):
        Drop = Select(self.wait.until(EC.visibility_of_element_located(self.COLORS_DROPDOWN)))
        all_oprions = Drop.options
        for option in all_oprions:
            Drop.select_by_visible_text(option.text)
            selected_option = Drop.first_selected_option
            selected_option_text = selected_option.text
            assert option.text == selected_option_text, f'No value {option.text} in dropdown'

    @allure.step("Checking len colors in dropdown")
    def check_len_colors_dropdown(self):
        Drop = Select(self.wait.until(EC.visibility_of_element_located(self.COLORS_DROPDOWN)))
        all_oprions = Drop.options
        assert len(all_oprions) == 11, f'Wrong number of options in dropdown: {len(all_oprions)}'

    @allure.step("Selected colors in Multiselect")
    def color_in_multiple(self):
        selected_elem = self.driver.find_elements(*self.COLORS_IN_MULTIPLE)
        selected_color = []
        for i in selected_elem:
            selected_color.append(i.text)
        return selected_color

    @allure.step("Checking selected in Multiselect")
    def check_multiselect(self):
        input = self.wait.until(EC.visibility_of_element_located(self.MULTISELECT))
        for color in self.COLORS_LIST:
            input.send_keys(color)
            input.send_keys(Keys.ENTER)
            selected_color = self.color_in_multiple()
            assert color in selected_color, f'Value {color} is not selected in Multiselect'

    @allure.step("Delete value in Multiselect")
    def delete_selected_multiple(self):
        len_multiple = len(self.color_in_multiple())
        for index_bttn in range(len_multiple, 1, -1):
            button_delete = self.wait.until(EC.visibility_of_element_located(self.DELETE_SELECT(index_bttn)))
            self.driver.execute_script("arguments[0].click();", button_delete)

    @allure.step("Checking cars in Multiselect")
    def check_cars_multiselect(self):
        cars_multiselect = self.wait.until(EC.visibility_of_element_located(self.CARS_MULTISELECT))
        self.scroll_to_element(cars_multiselect)
        Multiselect = Select(cars_multiselect)
        all_cars = Multiselect.options
        for car in all_cars:
            Multiselect.select_by_visible_text(car.text)
            assert car.is_selected(), f'Value {car.text} is not selected in Multiselect'









