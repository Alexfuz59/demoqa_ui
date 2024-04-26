import allure
from base.base_page import BasePage
from config.links import LinkInteractions
from enums.error_enums import ErrorInter
from selenium.webdriver.support import expected_conditions as EC


class Resizable(BasePage):
    PAGE_URL = LinkInteractions.RESIZABLE
    RESIZABLE_BOX = ('xpath', '//div[@id="resizableBoxWithRestriction"]')
    RESIZABLE = ('xpath', '//div[@id="resizable"]')

    @allure.step("Resizable box set size")
    def resizable_box_set_size(self, width, height):
        box = self.wait.until(EC.visibility_of_element_located(self.RESIZABLE_BOX))
        self.driver.execute_script(f'arguments[0].style.width = "{width}px"; arguments[0].style.height = "{height}px";', box)
        size = box.size
        assert size['width'] == width, ErrorInter.INVALID_WIDTH(size['width'])
        assert size['height'] == height, ErrorInter.INVALID_HEIGHT(size['height'])

    @allure.step("Resizable set size")
    def resizable_set_size(self, width, height):
        box = self.wait.until(EC.visibility_of_element_located(self.RESIZABLE))
        self.driver.execute_script(f'arguments[0].style.width = "{width}px"; arguments[0].style.height = "{height}px";', box)
        size = box.size
        assert size['width'] == width, ErrorInter.INVALID_WIDTH(size['width'])
        assert size['height'] == height, ErrorInter.INVALID_HEIGHT(size['height'])
