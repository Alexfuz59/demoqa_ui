import re
import allure
from base.base_page import BasePage
from config.links import LinkInteractions
from enums.error_enums import ErrorInter
from selenium.webdriver.support import expected_conditions as EC


class Droppable(BasePage):
    PAGE_URL = LinkInteractions.DROPPABLE
    SIMPLE = ('xpath', '//a[@id="droppableExample-tab-simple"]')
    ACCEPT = ('xpath', '//a[@id="droppableExample-tab-accept"]')
    PREVENT_PROPOGATION = ('xpath', '//a[@id="droppableExample-tab-preventPropogation"]')
    REVERT_DRAGGABLE = ('xpath', '//a[@id="droppableExample-tab-revertable"]')
    DRAG_ME_SIMPLE = ('xpath', '(//div[@class="drag-box mt-4 ui-draggable ui-draggable-handle"])[1]')
    DROP_SIMPLE = ('xpath', '(//div[@id="droppable"])[1]')
    ACCEPTABLE = ('xpath', '//div[@id="acceptable"]')
    NOT_ACCEPTABLE = ('xpath', '//div[@id="notAcceptable"]')
    DROP_ACCEPT = ('xpath', '(//div[@id="droppable"])[2]')
    NOT_GREEDY = ('xpath', '//div[@id="notGreedyDropBox"]')
    NOT_GREEDY_INNER = ('xpath', '//div[@id="notGreedyInnerDropBox"]')
    GREEDY = ('xpath', '//div[@id="greedyDropBox"]')
    GREEDY_INNER = ('xpath', '//div[@id="greedyDropBoxInner"]')
    DRAG_ME_PREVENT =('xpath', '//div[@id="dragBox"]')
    STATUS_DROPPED = lambda self, index: ('xpath', f'(//p)[{index}]')
    WILL_REVERT = ('xpath', '//div[@id="revertable"]')
    NOT_REVERT = ('xpath', '//div[@id="notRevertable"]')
    DROP_REVERT = ('xpath', '(//div[@id="droppable"])[3]')
    DROP_ACTIV = ('xpath', '(//div[@class="drag-box mt-4 ui-draggable ui-draggable-handle"])[6]')
    DROP_ACTIV_NOT_GREEDY = ('xpath', '//div[@class="drop-box ui-droppable ui-state-highlight" and @id="notGreedyInnerDropBox"]')
    DROP_ACTIV_GREEDY = ('xpath', '//div[@class="drop-box ui-droppable ui-state-highlight" and @id="greedyDropBoxInner"]')

    @allure.step("Click simple")
    def click_simple(self):
        self.wait.until(EC.visibility_of_element_located(self.SIMPLE)).click()

    @allure.step("Click accept")
    def click_accept(self):
        self.wait.until(EC.visibility_of_element_located(self.ACCEPT)).click()

    @allure.step("Click prevent propagation")
    def click_prevent_propagation(self):
        self.wait.until(EC.visibility_of_element_located(self.PREVENT_PROPOGATION)).click()

    @allure.step("Click revert draggable")
    def click_revert_draggable(self):
        self.wait.until(EC.visibility_of_element_located(self.REVERT_DRAGGABLE)).click()

    @allure.step("Drag and drop simple")
    def drop_object_simple(self):
        drag = self.wait.until(EC.visibility_of_element_located(self.DRAG_ME_SIMPLE))
        drop = self.wait.until(EC.visibility_of_element_located(self.DROP_SIMPLE))
        self.action.drag_and_drop(drag, drop).perform()
        return drop

    @allure.step("Checking for successful drag and drop")
    def check_drop(self, drop):
        attribute = drop.get_attribute('class')
        assert 'ui-state-highlight' in attribute, ErrorInter.ERROR_DROP_INACTIVE
        assert drop.text == "Dropped!", ErrorInter.ERROR_VALUE_DROP(drop.text)

    @allure.step("Checking for failed drag and drop")
    def check_not_drop(self, drop):
        attribute = drop.get_attribute('class')
        assert not 'ui-state-highlight' in attribute, ErrorInter.ERROR_DROP_ACTIVE
        assert drop.text == "Drop here", ErrorInter.ERROR_VALUE_DROP(drop.text)

    @allure.step("Checking for successful drag and drop 'greedy'")
    def check_drop_greedy(self, drop, index_status):
        attribute = drop.get_attribute('class')
        text = self.wait.until(EC.visibility_of_element_located(self.STATUS_DROPPED(index_status))).text
        assert 'ui-state-highlight' in attribute, ErrorInter.ERROR_DROP_INACTIVE
        assert text == "Dropped!", ErrorInter.ERROR_VALUE_DROP(drop.text)

    @allure.step("Checking for failed drag and drop 'greedy'")
    def check_drop_not_greedy(self, drop, index_status):
        attribute = drop.get_attribute('class')
        text = self.wait.until(EC.visibility_of_element_located(self.STATUS_DROPPED(index_status))).text
        assert not 'ui-state-highlight' in attribute, ErrorInter.ERROR_DROP_ACTIVE
        assert text == "Outer droppable", ErrorInter.ERROR_VALUE_DROP(text)

    @allure.step("Drag and drop accept")
    def drop_object_accept(self):
        drag = self.wait.until(EC.visibility_of_element_located(self.ACCEPTABLE))
        drop = self.wait.until(EC.visibility_of_element_located(self.DROP_ACCEPT))
        self.action.drag_and_drop(drag, drop).perform()
        return drop

    @allure.step("Drag and drop not accept")
    def drop_object_not_accept(self):
        drag = self.wait.until(EC.visibility_of_element_located(self.NOT_ACCEPTABLE))
        drop = self.wait.until(EC.visibility_of_element_located(self.DROP_ACCEPT))
        self.action.drag_and_drop(drag, drop).perform()
        return drop

    @allure.step("Drag and drop not greedy")
    def drop_object_not_greedy(self):
        drag = self.wait.until(EC.visibility_of_element_located(self.DRAG_ME_PREVENT))
        drop = self.wait.until(EC.visibility_of_element_located(self.NOT_GREEDY))
        drop_inner = self.wait.until(EC.visibility_of_element_located(self.NOT_GREEDY_INNER))
        self.action.drag_and_drop(drag, drop_inner).perform()
        self.wait.until(EC.visibility_of_element_located(self.DROP_ACTIV_NOT_GREEDY))
        self.check_drop_greedy(drop, 3)
        self.check_drop_greedy(drop_inner, 4)

    @allure.step("Drag and drop greedy")
    def drop_object_greedy(self):
        drag = self.wait.until(EC.visibility_of_element_located(self.DRAG_ME_PREVENT))
        drop = self.wait.until(EC.visibility_of_element_located(self.GREEDY))
        drop_inner = self.wait.until(EC.visibility_of_element_located(self.GREEDY_INNER))
        self.action.drag_and_drop(drag, drop_inner)\
            .pause(1)\
            .perform()
        self.wait.until(EC.visibility_of_element_located(self.DROP_ACTIV_GREEDY))
        self.check_drop_greedy(drop_inner, 6)
        self.check_drop_not_greedy(drop, 5)

    @allure.step("Drag and drop revert")
    def drop_will_revert(self):
        drag = self.wait.until(EC.visibility_of_element_located(self.WILL_REVERT))
        drop = self.wait.until(EC.visibility_of_element_located(self.DROP_REVERT))
        drag_not_revert = self.wait.until(EC.visibility_of_element_located(self.NOT_REVERT))
        self.action.drag_and_drop(drag, drag_not_revert).perform()
        drag_moving_button = self.wait.until(EC.visibility_of_element_located(self.WILL_REVERT))
        top_before, left_before = self.check_position(drag_moving_button)
        self.action.drag_and_drop(drag, drop).perform()
        self.check_drop(drop)
        drag_moving_drop = self.wait.until(EC.visibility_of_element_located(self.WILL_REVERT))
        top_after, left_after = self.check_position(drag_moving_drop)
        assert top_before == top_after, ErrorInter.ERROR_HEIGHT_REVERT
        assert left_before == left_after, ErrorInter.ERROR_WITH_REVERT

    @allure.step("Position determination")
    def check_position(self, drag):
        top_str = re.findall(r'\d+', drag.value_of_css_property("top"))
        left_str = re.findall(r'\d+', drag.value_of_css_property("left"))
        top = int(''.join(top_str))
        left = int(''.join(left_str))
        return top, left

    @allure.step("Drag and drop not revert")
    def drop_not_revert(self):
        drag = self.wait.until(EC.visibility_of_element_located(self.NOT_REVERT))
        drop = self.wait.until(EC.visibility_of_element_located(self.DROP_REVERT))
        drag_will_revert = self.wait.until(EC.visibility_of_element_located(self.WILL_REVERT))
        self.action.drag_and_drop(drag, drop).perform()
        self.check_drop(drop)
        self.wait.until(EC.presence_of_element_located(self.DROP_ACTIV))
        drag_moving_drop = self.wait.until(EC.visibility_of_element_located(self.NOT_REVERT))
        top_before, left_before = self.check_position(drag_moving_drop)
        self.action.drag_and_drop(drag, drag_will_revert).perform()
        self.wait.until(EC.presence_of_element_located(self.DROP_ACTIV))
        drag_after = self.wait.until(EC.visibility_of_element_located(self.NOT_REVERT))
        top_after, left_after = self.check_position(drag_after)
        assert top_before == top_after, ErrorInter.ERROR_HEIGHT_REVERT
        assert left_before == left_after, ErrorInter.ERROR_WITH_REVERT



