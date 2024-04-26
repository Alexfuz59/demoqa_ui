import allure
from base.base_page import BasePage
from config.links import LinkInteractions
from enums.error_enums import ErrorInter
from selenium.webdriver.support import expected_conditions as EC


class Selectable(BasePage):
    PAGE_URL = LinkInteractions.SELECTABLE
    LIST = ('xpath', '//a[@id="demo-tab-list"]')
    GRID = ('xpath', '//a[@id="demo-tab-grid"]')
    LINE_LIST = ('xpath', '//li[@class="mt-2 list-group-item list-group-item-action"]')
    CELL_GRID = ('xpath', '//li[@class="list-group-item list-group-item-action"]')

    @allure.step("Click list")
    def click_list(self):
        self.wait.until(EC.visibility_of_element_located(self.LIST)).click()

    @allure.step("Click grid")
    def click_grid(self):
        self.wait.until(EC.visibility_of_element_located(self.GRID)).click()

    @allure.step("Checking selectable list")
    def check_selectable_list(self):
        line_list = self.driver.find_elements(*self.LINE_LIST)
        for line in line_list:
            self.driver.execute_script("arguments[0].click();", line)
            attribute = line.get_attribute("class")
            assert 'active' in attribute, ErrorInter.ERROR_SELECTED_LINE

    @allure.step("Checking selectable grid")
    def check_selectable_grid(self):
        line_list = self.driver.find_elements(*self.CELL_GRID)
        for cell in line_list:
            self.driver.execute_script("arguments[0].click();", cell)
            attribute = cell.get_attribute("class")
            assert 'active' in attribute, ErrorInter.ERROR_SELECTED_CELL
