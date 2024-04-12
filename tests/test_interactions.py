import pytest
import allure
from base.base_test import BaseTest


@allure.feature("Interactions")
class TestInteractions(BaseTest):
    @allure.title("Sorting list")
    def test_sortable_list(self):
        self.sortable.open()
        self.sortable.is_opened()
        self.sortable.click_grid()
        self.sortable.click_list()
        after_list = self.sortable.all_value()
        self.sortable.moving_line_desc()
        before_list = self.sortable.all_value()
        self.sortable.check_sort(after_list, before_list)

    @allure.title("Sorting grid")
    def test_sortable_grid(self):
        self.sortable.open()
        self.sortable.is_opened()
        self.sortable.click_grid()
        after_grid = self.sortable.all_value()
        self.sortable.moving_grid_desc()
        before_grid = self.sortable.all_value()
        self.sortable.check_sort(after_grid, before_grid)

    @allure.title("Selectable list")
    def test_selectable_list(self):
        self.selectable.open()
        self.selectable.is_opened()
        self.selectable.click_grid()
        self.selectable.click_list()
        self.selectable.check_selectable_list()

    @allure.title("Selectable grid")
    def test_selectable_grid(self):
        self.selectable.open()
        self.selectable.is_opened()
        self.selectable.click_grid()
        self.selectable.check_selectable_grid()

    @pytest.mark.parametrize("width, height", [(150, 150), (200, 200), (500, 300)])
    @allure.title("Resizable box in box with height: {height} and width: {width}")
    def test_resizable_box(self, width, height):
        self.resizable.open()
        self.resizable.is_opened()
        self.resizable.resizable_box_set_size(width, height)

    @allure.title("Resizable box with height: {height} and width: {width}")
    @pytest.mark.parametrize("width, height", [(500, 500), (200, 200), (700, 700)])
    def test_resizable(self, width, height):
        self.resizable.open()
        self.resizable.is_opened()
        self.resizable.resizable_set_size(width, height)

    @allure.title("Drop drag simple")
    def test_drop_drag_simple(self):
        self.droppable.open()
        self.droppable.is_opened()
        self.droppable.click_accept()
        self.droppable.click_simple()
        drop = self.droppable.drop_object_simple()
        self.droppable.check_drop(drop)

    @allure.title("Drop drag accept")
    def test_drop_drag_accept(self):
        self.droppable.open()
        self.droppable.is_opened()
        self.droppable.click_accept()
        drop = self.droppable.drop_object_accept()
        self.droppable.check_drop(drop)

    @allure.title("Drop drag not accept")
    def test_drop_drag_not_accept(self):
        self.droppable.open()
        self.droppable.is_opened()
        self.droppable.click_accept()
        drop = self.droppable.drop_object_not_accept()
        self.droppable.check_not_drop(drop)

    @allure.title("Drop drag prevent propagation")
    def test_prevent_propagation(self):
        self.droppable.open()
        self.droppable.is_opened()
        self.droppable.click_prevent_propagation()
        self.droppable.drop_object_not_greedy()
        self.droppable.drop_object_greedy()

    @allure.title("Drop drag will revert")
    def test_will_revert(self):
        self.droppable.open()
        self.droppable.is_opened()
        self.droppable.click_revert_draggable()
        self.droppable.drop_will_revert()

    @allure.title("Drop drag not revert")
    def test_not_revert(self):
        self.droppable.open()
        self.droppable.is_opened()
        self.droppable.click_revert_draggable()
        self.droppable.drop_not_revert()

    @allure.title("Dragging by coordinates simple with height: {top} and width: {left}")
    @pytest.mark.parametrize("top, left", [(50, 40), (90, 70), (130, 130)])
    def test_dragabble_simple(self, top, left):
        self.dragabble.open()
        self.dragabble.is_opened()
        self.dragabble.click_button_cursor_style()
        self.dragabble.click_button_simple()
        self.dragabble.check_moved_object_simple(top, left)

    @allure.title("Axis restriction with height: {top} and width: {left}")
    @pytest.mark.parametrize("top, left", [(50, 40), (90, 70), (130, 130)])
    def test_axis_restricted(self, top, left):
        self.dragabble.open()
        self.dragabble.is_opened()
        self.dragabble.click_button_axis_restriction()
        self.dragabble.check_moving_x(top, left)
        self.dragabble.check_moving_y(top, left)

    @allure.title("Container restriction with height: {top} and width: {left}")
    @pytest.mark.parametrize("top, left", [(50, 40), (90, 70), (100, 130)])
    def test_container_restriction(self, top, left):
        self.dragabble.open()
        self.dragabble.is_opened()
        self.dragabble.click_button_container_restriction()
        self.dragabble.check_container_restriction(top, left)





