import allure
from base.base_test import BaseTest


@allure.feature("Elements")
class TestElements(BaseTest):
    @allure.title("Text box")
    def test_text_box(self):
        self.text_box.open()
        self.text_box.is_opened()
        self.text_box.check_placeholder()
        self.text_box.set_value_user_name()
        self.text_box.set_value_user_email()
        self.text_box.set_value_current_address()
        self.text_box.set_value_permanent_address()

    @allure.title("Checkbox")
    def test_checkbox(self):
        self.checkbox.open()
        self.checkbox.is_opened()
        self.checkbox.click_checkbox_home()
        self.checkbox.open_all_toggle()
        self.checkbox.check_all_checkbox()

    @allure.title("Radio button)")
    def test_radio_button(self):
        self.radio_button.open()
        self.radio_button.is_opened()
        self.radio_button.check_click_yes()
        self.radio_button.check_click_impressive()
        self.radio_button.check_button_no()

    @allure.title("Buttons")
    def test_buttons(self):
        self.buttons.open()
        self.buttons.is_opened()
        self.buttons.double_click()
        self.buttons.check_double_click()
        self.buttons.right_button_click()
        self.buttons.check_right_click()
        self.buttons.dynamic_button_click()
        self.buttons.check_dynamic_click()

    @allure.title("Dynamic buttons")
    def test_dynamic_properties(self):
        self.dynamic_properties.open()
        self.dynamic_properties.is_opened()
        self.dynamic_properties.click_enable_button()
        self.dynamic_properties.click_visible_after_button()
        self.dynamic_properties.click_color_change_button()

    @allure.title("Image")
    def test_image(self):
        self.broken_links.open()
        self.broken_links.is_opened()
        self.broken_links.check_valid_image()
        self.broken_links.check_broken_image()

    @allure.title("Broken links")
    def test_broken_link(self):
        self.broken_links.open()
        self.broken_links.is_opened()
        self.broken_links.click_broken_link()
        self.broken_links.check_open_start_page()

    @allure.title("Valid links")
    def test_valid_link(self):
        self.broken_links.open()
        self.broken_links.is_opened()
        self.broken_links.click_valid_link()
        self.broken_links.check_open_start_page()

    @allure.title("Download and Upload file")
    def test_download_upload(self, tmpdir):
        self.upload_download.open()
        self.upload_download.is_opened()
        self.upload_download.click_button_download()
        self.upload_download.check_download(tmpdir)
        self.upload_download.check_format_file(tmpdir)
        self.upload_download.upload_file(tmpdir)
        self.upload_download.check_upload()
        self.upload_download.save_image_directory(tmpdir)















