import allure
import time
from base.base_page import BasePage
from config.links import LinkWidgets
from selenium.webdriver.support import expected_conditions as EC


class ProgressBar(BasePage):
    PAGE_URL = LinkWidgets.PROGRESS_BAR
    PROGRESS_BAR = ('xpath', '//div[@role="progressbar"]')
    BUTTON_START = ('xpath', '//button[@id="startStopButton"]')
    BUTTON_STOP = ('xpath', '//button[@id="startStopButton"]')
    BUTTON_RESET = ('xpath', '//button[@id="resetButton"]')

    @allure.step("Click button start")
    def click_button_start(self):
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_START)).click()

    @allure.step("Click button stop")
    def click_button_stop(self):
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_STOP)).click()

    @allure.step("Click button reset")
    def click_button_reset(self):
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_RESET)).click()

    @allure.step("Start progress bar")
    def check_start(self):
        self.wait.until(EC.visibility_of_element_located(self.BUTTON_START))
        progress_bar = self.wait.until(EC.presence_of_element_located(self.PROGRESS_BAR))
        value_progress_bar = int(progress_bar.get_attribute("aria-valuenow"))
        self.click_button_start()
        self.wait.until(EC.visibility_of_element_located(self.BUTTON_STOP))
        time.sleep(2)
        value_start = int(progress_bar.get_attribute("aria-valuenow"))
        assert value_progress_bar != value_start, 'The progress bar did not start'

    @allure.step("Stop progress bar")
    def check_stop(self):
        self.wait.until(EC.visibility_of_element_located(self.BUTTON_STOP))
        progress_bar = self.wait.until(EC.presence_of_element_located(self.PROGRESS_BAR))
        self.click_button_stop()
        self.wait.until(EC.visibility_of_element_located(self.BUTTON_START))
        value = int(progress_bar.get_attribute("aria-valuenow"))
        time.sleep(2)
        before_value = int(progress_bar.get_attribute("aria-valuenow"))
        assert value == before_value, 'Progress bar loading has not stopped'

    @allure.step("Reset progress bar")
    def check_reset(self):
        progress_bar = self.wait.until(EC.presence_of_element_located(self.PROGRESS_BAR))
        progress = int(progress_bar.get_attribute("aria-valuenow"))
        while progress < 100:
            progress = int(progress_bar.get_attribute("aria-valuenow"))
        before_value = int(progress_bar.get_attribute("aria-valuenow"))
        self.click_button_reset()
        self.wait.until(EC.visibility_of_element_located(self.BUTTON_START))
        after_value = int(progress_bar.get_attribute("aria-valuenow"))
        assert before_value == 100, 'Progress bar did not load all the way'
        assert after_value == 0, 'Progress bar did not update to 0'


