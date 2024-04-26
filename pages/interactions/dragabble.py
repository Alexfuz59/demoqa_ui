import re
import allure
from base.base_page import BasePage
from config.links import LinkInteractions
from enums.error_enums import ErrorInter
from selenium.webdriver.support import expected_conditions as EC


class Dragabble(BasePage):
    PAGE_URL = LinkInteractions.DRAGABBLE
    BUTTON_SIMPLE = ('xpath', '//a[@id="draggableExample-tab-simple"]')
    BUTTON_AXIS_RESTRICTION = ('xpath', '//a[@id="draggableExample-tab-axisRestriction"]')
    BUTTON_CONTAINER_RESTRICTION = ('xpath', '//a[@id="draggableExample-tab-containerRestriction"]')
    BUTTON_CURSOR_STYLE = ('xpath', '//a[@id="draggableExample-tab-cursorStyle"]')
    DRAG_SIMPLE = ('xpath', '//div[@id="dragBox"]')
    DRAG_ONLY_X = ('xpath', '//div[contains(@class, "drag-box ui-draggable ui-draggable-handle") and @id="restrictedX"]')
    DRAG_ONLY_Y = ('xpath', '//div[contains(@class, "drag-box ui-draggable ui-draggable-handle") and @id="restrictedY"]')
    DRAG_CONTAINER = ('xpath', '//div[@class="draggable ui-widget-content ui-draggable ui-draggable-handle"]')
    CONTAINER = ('xpath', '//div[@id="containmentWrapper"]')

    @allure.step("Click button simple")
    def click_button_simple(self):
        self.wait.until(EC.visibility_of_element_located(self.BUTTON_SIMPLE)).click()

    @allure.step("Click button axis restriction")
    def click_button_axis_restriction(self):
        self.wait.until(EC.visibility_of_element_located(self.BUTTON_AXIS_RESTRICTION)).click()

    @allure.step("Click button container restriction")
    def click_button_container_restriction(self):
        self.wait.until(EC.visibility_of_element_located(self.BUTTON_CONTAINER_RESTRICTION)).click()

    @allure.step("Click button cursor style")
    def click_button_cursor_style(self):
        self.wait.until(EC.visibility_of_element_located(self.BUTTON_CURSOR_STYLE)).click()

    @allure.step("Checking the position after dragging 'simple'")
    def check_moved_object_simple(self, top, left):
        top_before, left_before = self.check_position_simple()
        drag = self.wait.until(EC.visibility_of_element_located(self.DRAG_SIMPLE))
        self.action.drag_and_drop_by_offset(drag, left, top).pause(2).perform()
        top_after, left_after = self.check_position_simple()
        assert top_before + top == top_after, ErrorInter.INVALID_HEIGHT(top_after)
        assert left_before + left == left_after, ErrorInter.INVALID_WIDTH(left_after)

    @allure.step("Position determination simple")
    def check_position_simple(self):
        drag = self.wait.until(EC.visibility_of_element_located(self.DRAG_SIMPLE))
        top_str = re.findall(r'\d+', drag.value_of_css_property("top"))
        left_str = re.findall(r'\d+', drag.value_of_css_property("left"))
        top = int(''.join(top_str))
        left = int(''.join(left_str))
        return top, left

    @allure.step("Checking the position after dragging 'drag' X")
    def check_moving_x(self, top, left):
        drag = self.wait.until(EC.visibility_of_element_located(self.DRAG_ONLY_X))
        top_before, left_before = self.check_position(drag)
        self.action.drag_and_drop_by_offset(drag, left, top).perform()
        drag = self.wait.until(EC.visibility_of_element_located(self.DRAG_ONLY_X))
        top_after, left_after = self.check_position(drag)
        assert top_after == 0, ErrorInter.INVALID_HEIGHT(top_after)
        assert left_after == left_before + left, ErrorInter.INVALID_WIDTH(left_after)

    @allure.step("Position determination")
    def check_position(self, drag):
        top_str = re.findall(r'\d+', drag.value_of_css_property("top"))
        left_str = re.findall(r'\d+', drag.value_of_css_property("left"))
        top = int(''.join(top_str))
        left = int(''.join(left_str))
        return top, left

    @allure.step("Checking the position after dragging 'drag' Y")
    def check_moving_y(self, top, left):
        drag = self.wait.until(EC.visibility_of_element_located(self.DRAG_ONLY_Y))
        top_before, left_before = self.check_position(drag)
        self.action.drag_and_drop_by_offset(drag, left, top).perform()
        drag = self.wait.until(EC.visibility_of_element_located(self.DRAG_ONLY_Y))
        top_after, left_after = self.check_position(drag)
        assert left_after == 0, ErrorInter.INVALID_WIDTH(left_after)
        assert top_after == top_before + top, ErrorInter.INVALID_HEIGHT(top_after)

    @allure.step("Checking container restriction")
    def check_container_restriction(self, top, left):
        drag = self.wait.until(EC.visibility_of_element_located(self.DRAG_CONTAINER))
        top_before, left_before = self.check_position(drag)
        self.action.drag_and_drop_by_offset(drag, left, top).perform()
        drag = self.wait.until(EC.visibility_of_element_located(self.DRAG_CONTAINER))
        top_after, left_after = self.check_position(drag)
        top_container, left_container = self.size_container()
        if top_before + top > top_container and left_before + left > left_container:
            assert top_after <= top_container, ErrorInter.ERROR_HEIGHT_CONTAINER(top_after, top_container)
            assert left_after <= left_container, ErrorInter.ERROR_WIDTH_CONTAINER(left_after, top_container)
        elif top_before + top > top_container:
            assert top_after <= top_container, ErrorInter.ERROR_HEIGHT_CONTAINER(top_after, top_container)
        elif left_before + left > left_container:
            assert left_after <= left_container, ErrorInter.ERROR_WIDTH_CONTAINER(left_after, top_container)
        else:
            assert top_before + top == top_after, ErrorInter.INVALID_HEIGHT(top_after)
            assert left_before + left == left_after, ErrorInter.INVALID_WIDTH(left_after)

    @allure.step("Size container ")
    def size_container(self):
        container = self.wait.until(EC.visibility_of_element_located(self.CONTAINER))
        size = container.size
        return size['height'], size['width']












