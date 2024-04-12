import allure
import pytest
from base.base_test import BaseTest


@allure.feature("Practice form")
class TestPracticeForm(BaseTest):
    @allure.title("Form filling")
    @pytest.fixture()
    def filling_form(self):
        self.practice_form.open()
        self.practice_form.is_opened()
        self.practice_form.set_last_name()
        self.practice_form.set_first_name()
        self.practice_form.set_user_email()
        self.practice_form.click_radiobutton_male()
        self.practice_form.set_user_number()
        self.practice_form.set_date_birth()
        self.practice_form.set_subjects()
        self.practice_form.click_checkbox_sports()
        self.practice_form.click_checkbox_music()
        self.practice_form.upload_file()
        self.practice_form.set_current_address()
        self.practice_form.set_state()
        self.practice_form.set_city()
        self.practice_form.click_button_submit()
        self.practice_form.check_active_submitted_form()

    @allure.title("Successful completion of the form")
    def test_successful_form_completion(self):
        self.practice_form.open()
        self.practice_form.is_opened()
        self.practice_form.set_last_name()
        self.practice_form.set_first_name()
        self.practice_form.set_user_email()
        self.practice_form.click_radiobutton_male()
        self.practice_form.set_user_number()
        self.practice_form.set_date_birth()
        self.practice_form.set_subjects()
        self.practice_form.click_checkbox_sports()
        self.practice_form.click_checkbox_music()
        self.practice_form.upload_file()
        self.practice_form.set_current_address()
        self.practice_form.set_state()
        self.practice_form.set_city()
        self.practice_form.click_button_submit()
        self.practice_form.check_active_submitted_form()

    @allure.title("Checking the submitted form ")
    def test_submitting_the_form(self, filling_form):
        self.practice_form.check_student_name()
        self.practice_form.check_student_email()
        self.practice_form.check_gender()
        self.practice_form.check_mobile()
        self.practice_form.check_subjects_submitted_form()
        self.practice_form.check_hobbies_submitted_form()
        self.practice_form.check_picture()
        self.practice_form.check_address()
        self.practice_form.check_state_city()
        self.practice_form.check_birthday()
        self.practice_form.click_button_close()
        self.practice_form.check_no_active_submitted_form()



