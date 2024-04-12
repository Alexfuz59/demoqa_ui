import allure
from base.base_test import BaseTest


@allure.feature("Alert, Frame and Windows")
class TestWindows(BaseTest):
    @allure.title("Windows")
    def test_windows(self):
        self.windows.open()
        self.windows.is_opened()
        self.windows.check_new_tab()
        self.windows.check_new_window()
        self.windows.check_window_message()

    @allure.title("Alert")
    def test_alert(self):
        self.alert.open()
        self.alert.is_opened()
        self.alert.click_button_alert_see()
        self.alert.check_alert_see()
        self.alert.click_button_alert_time()
        self.alert.check_alert_time()
        self.alert.click_button_alert_confirme()
        self.alert.check_alert_confirme()
        self.alert.click_button_alert_promt()
        self.alert.check_alert_promt()

    @allure.title("Frame")
    def test_iframe(self):
        self.iframe.open()
        self.iframe.is_opened()
        self.iframe.check_iframe1()
        self.iframe.check_iframe2()

    @allure.title("Non-standard frame")
    def test_nested_frames(self):
        self.nested_frames.open()
        self.nested_frames.is_opened()
        self.nested_frames.check_nested_frames()

    @allure.title("Modal dialogs")
    def test_modal_dialogs(self):
        self.modal_dialogs.open()
        self.modal_dialogs.is_opened()
        self.modal_dialogs.click_button_small_modal()
        self.modal_dialogs.check_small_modal()
        self.modal_dialogs.click_button_large_modal()
        self.modal_dialogs.check_large_modal()

