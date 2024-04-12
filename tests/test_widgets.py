import pytest
import allure
from base.base_test import BaseTest


@allure.feature("Widgets")
class TestWidgets(BaseTest):
    @allure.title("Accordian")
    def test_accordian(self):
        self.accordian.open()
        self.accordian.is_opened()
        self.accordian.check_accordian_section_2()
        self.accordian.check_accordian_section_3()
        self.accordian.check_accordian_section_1()

    @allure.title("Auto Complete")
    def test_auto_complete(self):
        self.auto_complete.open()
        self.auto_complete.is_opened()
        self.auto_complete.check_multiple_empty()
        self.auto_complete.input_in_multiple()
        self.auto_complete.delete_selected_multiple()
        self.auto_complete.check_input_single_color()

    @pytest.mark.parametrize('value', [1, 25, 50])
    @allure.title("Slider set value: {value}")
    def test_slider(self, value):
        self.slider.open()
        self.slider.is_opened()
        self.slider.check_moving_slider(value)

    @allure.title("Progress bar")
    def test_progress_bar(self):
        self.progress_bar.open()
        self.progress_bar.is_opened()
        self.progress_bar.check_start()
        self.progress_bar.check_stop()
        self.progress_bar.check_start()
        self.progress_bar.check_reset()

    @allure.title("Tabs")
    def test_tabs(self):
        self.tabs.open()
        self.tabs.is_opened()
        self.tabs.click_origin()
        self.tabs.check_message_origin()
        self.tabs.click_use()
        self.tabs.check_message_use()
        self.tabs.click_what()
        self.tabs.check_message_what()
        self.tabs.check_tab_more()

    @allure.title("Tooltip")
    def test_tool_tips(self):
        self.tool_tips.open()
        self.tool_tips.is_opened()
        self.tool_tips.check_tool_tips_button()
        self.tool_tips.check_tool_tips_input()

    @allure.title("Menu")
    def test_menu(self):
        self.menu.open()
        self.menu.is_opened()
        self.menu.check_open_menu_2()
        self.menu.select_in_list()
        self.menu.select_sub_item_2()

    @allure.title("Select menu")
    def test_select_menu(self):
        self.select_menu.open()
        self.select_menu.is_opened()
        self.select_menu.check_dropdown_select_value()
        self.select_menu.check_dropdown_genders()
        self.select_menu.check_colors_dropdown()
        self.select_menu.check_len_colors_dropdown()
        self.select_menu.check_multiselect()
        self.select_menu.delete_selected_multiple()
        self.select_menu.check_cars_multiselect()

    @allure.title("Date calendar")
    def test_data(self):
        self.date_picker.open()
        self.date_picker.is_opened()
        self.date_picker.set_data()
        self.date_picker.check_data()

    @allure.title("Date and time calendar")
    def test_datatime(self):
        self.date_picker.open()
        self.date_picker.is_opened()
        self.date_picker.set_data_time()
        self.date_picker.check_datetime()


