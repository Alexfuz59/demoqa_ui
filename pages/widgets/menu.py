import allure
from base.base_page import BasePage
from config.links import LinkWidgets
from selenium.webdriver.support import expected_conditions as EC


class Menu(BasePage):
    PAGE_URL = LinkWidgets.MENU
    MENU_ITEM_2 = ('xpath', '//a[text()="Main Item 2"]')
    SUB_LIST = ('xpath', '//a[text()="SUB SUB LIST »"]')
    SUB_ITEM_2 = ('xpath', '//a[text()="Sub Sub Item 2"]')

    @allure.step("Open menu 2")
    def check_open_menu_2(self):
        menu2 = self.wait.until(EC.visibility_of_element_located(self.MENU_ITEM_2))
        self.action.move_to_element(menu2).perform()
        self.wait.until(EC.visibility_of_element_located(self.SUB_LIST))

    @allure.step("Select Sub List")
    def select_in_list(self):
        select = self.wait.until(EC.visibility_of_element_located(self.SUB_LIST))
        self.action.move_to_element(select) \
            .pause(1) \
            .perform()
        self.wait.until(EC.visibility_of_element_located(self.SUB_ITEM_2))

    @allure.step("Select Sub Item 2")
    def select_sub_item_2(self):
        select_item2 = self.wait.until(EC.visibility_of_element_located(self.SUB_ITEM_2))
        self.action.move_to_element(select_item2) \
            .pause(1) \
            .click() \
            .perform()


