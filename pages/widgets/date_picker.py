import allure
from base.base_page import BasePage
from config.links import LinkWidgets
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
from selenium.webdriver import Keys
from datetime import datetime

fake = Faker()


class DatePicker(BasePage):
    PAGE_URL = LinkWidgets.DATE_PICKER
    SELECT_DATA = ('xpath', '//input[@id="datePickerMonthYearInput"]')
    SELECT_DATA_TIME = ('xpath', '//input[@id="dateAndTimePickerInput"]')
    INPUT_DATA = ('xpath', '//input[@class="react-datepicker-ignore-onclickoutside"]')
    CALENDAR = ('xpath', '//div[@class="react-datepicker-popper"]')
    data_value = fake.date_of_birth(minimum_age=18, maximum_age=100)
    data = data_value.strftime('%m.%d.%Y')
    datetime_value = fake.date_time()
    datetime = datetime_value.strftime('%m.%d.%Y %I:%M %p')

    @allure.step("Set data in calendar")
    def set_data(self):
        input = self.wait.until(EC.visibility_of_element_located(self.SELECT_DATA))
        input.click()
        input.send_keys(Keys.CONTROL + 'A')
        input.send_keys(Keys.DELETE)
        input.send_keys(self.data)
        input.send_keys(Keys.ENTER)
        self.wait.until(EC.invisibility_of_element_located(self.INPUT_DATA))

    @allure.step("Checking date in calendar")
    def check_data(self):
        input = self.wait.until(EC.visibility_of_element_located(self.SELECT_DATA))
        data_value = datetime.strptime(input.get_attribute("value"), '%m/%d/%Y')
        value = data_value.strftime('%m.%d.%Y')
        assert value == self.data, 'Wrong date on the calendar'

    @allure.step("Set data and time in calendar")
    def set_data_time(self):
        input = self.wait.until(EC.visibility_of_element_located(self.SELECT_DATA_TIME))
        input.click()
        input.send_keys(Keys.CONTROL + 'A')
        input.send_keys(Keys.BACKSPACE)
        input.send_keys(self.datetime)
        input.send_keys(Keys.ENTER)
        self.wait.until(EC.invisibility_of_element_located(self.CALENDAR))

    @allure.step("Checking date and time in calendar")
    def check_datetime(self):
        input = self.wait.until(EC.visibility_of_element_located(self.SELECT_DATA_TIME))
        date_object = datetime.strptime(self.datetime, '%m.%d.%Y %I:%M %p')
        datatime = date_object.strftime('%B %e, %Y %I:%M %p')
        date_object_value = datetime.strptime(input.get_attribute("value"), '%B %d, %Y %I:%M %p')
        datatime_value = date_object_value.strftime('%B %e, %Y %I:%M %p')
        assert datatime_value == datatime, 'Wrong date and time on the calendar'
