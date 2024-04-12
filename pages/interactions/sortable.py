import allure
from base.base_page import BasePage
from config.links import LinkInteractions
from selenium.webdriver.support import expected_conditions as EC


class Sortable(BasePage):
    PAGE_URL = LinkInteractions.SORTABLE
    LIST = ('xpath', '//a[@id="demo-tab-list"]')
    GRID = ('xpath', '//a[@id="demo-tab-grid"]')
    LINES_CELL = ('xpath', '//div[@class="list-group-item list-group-item-action"]')
    LINE = lambda self, numberLine: ('xpath', f'(//div[text()="{numberLine}"])[1]')
    CELL = lambda self, numberGrid, index: ('xpath', f'(//div[text()="{numberGrid}"])[{index}]')
    ACTIVE_GRID = ('xpath', '//div[contains(@style, "opacity: 0; visibility: hidden;")]')

    @allure.step("Click list")
    def click_list(self):
        self.wait.until(EC.visibility_of_element_located(self.LIST)).click()
        self.wait.until(EC.visibility_of_element_located(self.LINES_CELL))

    @allure.step("Click grid")
    def click_grid(self):
        self.wait.until(EC.visibility_of_element_located(self.GRID)).click()

    @allure.step("All value in list")
    def all_value(self):
        list_elements = self.driver.find_elements(*self.LINES_CELL)
        list_value = []
        for line in list_elements:
            list_value.append(line.text)
        list_value = list(filter(lambda x: x.strip(), list_value))
        return list_value

    @allure.step("Drag and drop value in the list in descending order")
    def moving_line_desc(self):
        all_value = self.all_value()
        for i in range(0, len(all_value)-1):
            elem1 = self.wait.until(EC.visibility_of_element_located(self.LINE(all_value[i])))
            elem2 = self.wait.until(EC.visibility_of_element_located(self.LINE(all_value[len(all_value)-1])))
            self.action.drag_and_drop(elem1, elem2).perform()

    @allure.step("Checking sorting desc")
    def check_sort(self, after_value, before_value):
        for i in range(0, len(after_value)-1):
            assert after_value[i] == before_value[-i-1], 'Incorrect descending sorting'

    @allure.step("Drag and drop value in the grid in descending order")
    def moving_grid_desc(self):
        all_value = self.all_value()
        for i in range(0, len(all_value)-1):
            if i >= 6:
                indexCell = 1
            else:
                indexCell = 2
            elem1 = self.wait.until(EC.visibility_of_element_located(self.CELL(all_value[i], indexCell)))
            elem2 = self.wait.until(EC.visibility_of_element_located(self.CELL(all_value[len(all_value)-1], 1)))
            self.action.drag_and_drop(elem1, elem2)\
                .pause(1)\
                .perform()
            self.wait.until(EC.invisibility_of_element_located(self.ACTIVE_GRID))




