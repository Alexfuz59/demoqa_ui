import os
from datetime import datetime
import allure
from base.base_page import BasePage
from config.links import LinkForms
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
from selenium.webdriver import Keys
from random import choice, randint

fake = Faker()


class PracticeForm(BasePage):
    PAGE_URL = LinkForms.PRACTICE_FORM
    INPUT_FIRST_NAME = ('xpath', '//input[@id="firstName"]')
    INPUT_LAST_NAME = ('xpath', '//input[@id="lastName"]')
    INPUT_USER_EMAIL = ('xpath', '//input[@id="userEmail"]')
    INPUT_USER_NUMBER = ('xpath', '//input[@id="userNumber"]')
    INPUT_DATE_BIRTH = ('xpath', '//input[@id="dateOfBirthInput"]')
    INPUT_SUBJECTS = ('xpath', '//input[@id="subjectsInput"]')
    TEXTAREA_CURRENT_ADDRESS = ('xpath', '//textarea[@id="currentAddress"]')
    DROP_STATE = ('xpath', '//input[@id="react-select-3-input"]')
    DROP_CITY = ('xpath', '//input[@id="react-select-4-input"]')
    BUTTON_SUBMIT = ('xpath', '//button[@id="submit"]')
    RADIOBUTTON_MALE = ('xpath', '(//div[@class="custom-control custom-radio custom-control-inline"])[1]')
    RADIOBUTTON_FEMALE = ('xpath', '(//div[@class="custom-control custom-radio custom-control-inline"])[2]')
    RADIOBUTTON_OTHER = ('xpath', '(//div[@class="custom-control custom-radio custom-control-inline"])[3]')
    CHECKBOX_SPORTS = ('xpath', '(//div[@class="custom-control custom-checkbox custom-control-inline"])[1]')
    CHECKBOX_READING = ('xpath', '(//div[@class="custom-control custom-checkbox custom-control-inline"])[2]')
    CHECKBOX_MUSIC = ('xpath', '(//div[@class="custom-control custom-checkbox custom-control-inline"])[3]')
    SELECT_PICTURE = ('xpath', '//input[@id="uploadPicture"]')
    SUBMITTED_FORM = ('xpath', '//div[@class="modal-content"]')
    VALUE_INPUT_STATE = ('xpath', '//div[@class=" css-1uccc91-singleValue"]')
    UNIVERSE_DATA = lambda self, data: ('xpath', f'//input[@value="{data}"]')
    STUDENT_NAME = ('xpath', '(//td)[2]')
    STUDENT_EMAIL = ('xpath', '(//td)[4]')
    GENDER = ('xpath', '(//td)[6]')
    MOBILE = ('xpath', '(//td)[8]')
    BIRTHDAY = ('xpath', '(//td)[10]')
    SUBJECTS = ('xpath', '(//td)[12]')
    HOBBIES = ('xpath', '(//td)[14]')
    PICTURE = ('xpath', '(//td)[16]')
    ADDRESS = ('xpath', '(//td)[18]')
    STATE_CITY = ('xpath', '(//td)[20]')
    BUTTON_CLOSE = ('xpath', '//button[@id="closeLargeModal"]')
    first_name = fake.first_name()
    last_name = fake.last_name()
    user_email = fake.ascii_free_email()
    phone_number = randint(1000000000, 9999999999)
    current_address = fake.address()
    birthdate = fake.date_of_birth(minimum_age=18, maximum_age=100)
    date_birth = birthdate.strftime('%d.%m.%Y')
    subjects_list = ['English', 'Chemistry', 'Computer Science', 'Commerce', 'Social Studies', 'Economics', 'Arts', 'Accounting', 'Maths']
    state_list = ['NCR', 'Uttar Pradesh', 'Haryana', 'Rajasthan']
    city_list = {"Rajasthan": ['Jaiselmer', 'Jaipur'],
                 'NCR': ["Delhi", "Noida", "Gurgaon"],
                 'Uttar Pradesh': ["Merrut", "Agra", "Lucknow"],
                 'Haryana': ["Panipat", "Karnal"]
                 }
    gender_list = ['Male', 'Female', 'Other']
    hobbies_list = ['Sports', 'Reading', 'Music']
    FILE_PATH = os.getcwd() + "/sampleFile.jpeg"

    @allure.step("Set first name")
    def set_first_name(self):
        self.wait.until(EC.visibility_of_element_located(self.INPUT_FIRST_NAME)).send_keys(self.first_name)

    @allure.step("Set last name")
    def set_last_name(self):
        self.wait.until(EC.visibility_of_element_located(self.INPUT_LAST_NAME)).send_keys(self.last_name)

    @allure.step("Set email")
    def set_user_email(self):
        self.wait.until(EC.visibility_of_element_located(self.INPUT_USER_EMAIL)).send_keys(self.user_email)

    @allure.step("Set phone number")
    def set_user_number(self):
        self.wait.until(EC.visibility_of_element_located(self.INPUT_USER_NUMBER)).send_keys(self.phone_number)

    @allure.step("Set birthdate")
    def set_date_birth(self):
        input = self.wait.until(EC.visibility_of_element_located(self.INPUT_DATE_BIRTH))
        self.scroll_to_element(input)
        input.click()
        input.send_keys(Keys.CONTROL + 'A')
        input.send_keys(self.date_birth)
        self.wait.until(EC.visibility_of_element_located(self.UNIVERSE_DATA(self.date_birth)))
        input.send_keys(Keys.TAB)
        input.send_keys(Keys.ENTER)

    @allure.step("Set subjects")
    def set_subjects(self):
        for subject in self.subjects_list:
            input = self.wait.until(EC.visibility_of_element_located(self.INPUT_SUBJECTS))
            input.send_keys(subject)
            input.send_keys(Keys.ENTER)

    @allure.step("Set current address")
    def set_current_address(self):
        input = (self.wait.until(EC.visibility_of_element_located(self.TEXTAREA_CURRENT_ADDRESS)))
        self.scroll_to_element(input)
        input.send_keys(self.current_address)

    @allure.step("Set state")
    def set_state(self):
        input = (self.wait.until(EC.visibility_of_element_located(self.DROP_STATE)))
        self.scroll_to_element(input)
        input.send_keys(choice(self.state_list))
        input.send_keys(Keys.TAB)

    @allure.step("Set city")
    def set_city(self):
        value_state = (self.wait.until(EC.visibility_of_element_located(self.VALUE_INPUT_STATE))).text
        input = self.wait.until(EC.element_to_be_clickable(self.DROP_CITY))
        self.scroll_to_element(input)
        if value_state in self.city_list:
            input = self.wait.until(EC.element_to_be_clickable(self.DROP_CITY))
            input.send_keys(choice(self.city_list[value_state]))
            input.send_keys(Keys.TAB)

    @allure.step("Click button submit")
    def click_button_submit(self):
        button = self.wait.until(EC.element_to_be_clickable(self.BUTTON_SUBMIT))
        self.scroll_to_element(button)
        button.click()

    @allure.step("Click radiobutton male")
    def click_radiobutton_male(self):
        radiobutton = self.wait.until(EC.element_to_be_clickable(self.RADIOBUTTON_MALE))
        self.scroll_to_element(radiobutton)
        radiobutton.click()

    @allure.step("Click radiobutton female")
    def click_radiobutton_female(self):
        radiobutton = self.wait.until(EC.element_to_be_clickable(self.RADIOBUTTON_FEMALE)).click()
        self.scroll_to_element(radiobutton)
        radiobutton.click()

    @allure.step("Click radiobutton other")
    def click_radiobutton_other(self):
        radiobutton = self.wait.until(EC.element_to_be_clickable(self.RADIOBUTTON_OTHER)).click()
        self.scroll_to_element(radiobutton)
        radiobutton.click()

    @allure.step("Click checkbox sports")
    def click_checkbox_sports(self):
        checkbox = self.wait.until(EC.visibility_of_element_located(self.CHECKBOX_SPORTS))
        self.scroll_to_element(checkbox)
        checkbox.click()

    @allure.step("Click checkbox reading")
    def click_checkbox_reading(self):
        checkbox = self.wait.until(EC.visibility_of_element_located(self.CHECKBOX_READING))
        self.scroll_to_element(checkbox)
        checkbox.click()

    @allure.step("Click checkbox music")
    def click_checkbox_music(self):
        checkbox = self.wait.until(EC.visibility_of_element_located(self.CHECKBOX_MUSIC))
        self.scroll_to_element(checkbox)
        checkbox.click()

    @allure.step("Upload file")
    def upload_file(self):
        self.wait.until(EC.visibility_of_element_located(self.SELECT_PICTURE)).send_keys(self.FILE_PATH)

    @allure.step("Checking active submitted form")
    def check_active_submitted_form(self):
        submitted_form = self.wait.until(EC.visibility_of_element_located(self.SUBMITTED_FORM))
        assert submitted_form.is_displayed(), 'Submitted form did not open'

    @allure.step("Checking inactive submitted form")
    def check_no_active_submitted_form(self):
        self.wait.until(EC.invisibility_of_element_located(self.SUBMITTED_FORM))

    @allure.step("Checking subjects in submitted form")
    def check_subjects_submitted_form(self):
        subjects = self.wait.until(EC.visibility_of_element_located(self.SUBJECTS)).text
        subjects_list = subjects.split(',')
        for subject in subjects_list:
            assert subject.strip() in self.subjects_list, f'Wrong subjects: {subject}'

    @allure.step("Checking hobbies in submitted form")
    def check_hobbies_submitted_form(self):
        hobbies = self.wait.until(EC.visibility_of_element_located(self.HOBBIES)).text
        hobbies_list = hobbies.split(", ")
        for hobby in hobbies_list:
            assert hobby in self.hobbies_list, f'Wrong hobbies: {hobby}'

    @allure.step("Checking state and city in submitted form")
    def check_state_city(self):
        state_city = self.wait.until(EC.visibility_of_element_located(self.STATE_CITY)).text
        state_city_list = state_city.split()
        state = state_city_list[0]
        if state in self.city_list:
            assert state_city_list[-1] in self.city_list[state]
        else:
            raise AssertionError("Wrong city")
        assert state_city_list[0] in self.state_list, f'Wrong state:{state_city_list[-1]} and city:{state_city_list[0]}'

    @allure.step("Checking student name in submitted form")
    def check_student_name(self):
        student_name = self.wait.until(EC.visibility_of_element_located(self.STUDENT_NAME)).text
        assert self.first_name in student_name, f'Wrong first_name: {student_name}'
        assert self.last_name in student_name, f'Wrong last_name: {student_name}'

    @allure.step("Checking email in submitted form")
    def check_student_email(self):
        student_email = self.wait.until(EC.visibility_of_element_located(self.STUDENT_EMAIL)).text
        assert self.user_email == student_email, f'Wrong user email: {student_email}'

    @allure.step("Checking gender in submitted form")
    def check_gender(self):
        gender = self.wait.until(EC.visibility_of_element_located(self.GENDER)).text
        assert gender in self.gender_list, f'Wrong gender: {gender}'

    @allure.step("Checking number mobile in submitted form")
    def check_mobile(self):
        mobile = self.wait.until(EC.visibility_of_element_located(self.MOBILE)).text
        assert self.phone_number == int(mobile), f'Wrong phone number: {mobile}'

    @allure.step("Checking picture in submitted form")
    def check_picture(self):
        picture = self.wait.until(EC.visibility_of_element_located(self.PICTURE)).text
        assert picture in self.FILE_PATH, f'Wrong picture'

    @allure.step("Checking birthday in submitted form")
    def check_birthday(self):
        birthday_str = self.wait.until(EC.visibility_of_element_located(self.BIRTHDAY)).text
        birthday = datetime.strptime(birthday_str, "%d %B,%Y")
        birthday_format = birthday.strftime("%m.%d.%Y")
        assert birthday_format == self.date_birth, f'Wrong birthday: {birthday_format}'

    @allure.step("Checking address in submitted form")
    def check_address(self):
        address = self.wait.until(EC.visibility_of_element_located(self.ADDRESS)).text
        assert address.strip() == self.current_address.replace('\n', " ").strip(), f'Wrong birthday: {address}'

    @allure.step("Click button close")
    def click_button_close(self):
        button = self.wait.until(EC.element_to_be_clickable(self.BUTTON_CLOSE))
        self.driver.execute_script("arguments[0].click();", button)





