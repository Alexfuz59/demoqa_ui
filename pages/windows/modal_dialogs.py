import allure
from base.base_page import BasePage
from config.links import LinkWindows
from selenium.webdriver.support import expected_conditions as EC
from enums.error_enums import ErrorWindows


class ModalDialogs(BasePage):
    PAGE_URL = LinkWindows.MODAL_DIALOGS
    BUTTON_SMALL_MODAL = ('xpath', '//button[@id="showSmallModal"]')
    BUTTON_LARGE_MODAL = ('xpath', '//button[@id="showLargeModal"]')
    MODAL = ('xpath', '//div[@class="modal-content"]')
    LARGE_MODAL = ('xpath', '//div[@class="modal-content"]')
    MESSAGE_SMALL_MODAL = ('xpath', '//div[@class="modal-body"]')
    BUTTON_CLOSE_SMALL= ('xpath', '//button[@id="closeSmallModal"]')
    MESSAGE_LARGE_MODAL = ('xpath', '//div/p')
    BUTTON_CLOSE_LARGE = ('xpath', '//button[@id="closeLargeModal"]')
    TEXT_SMALL_MODAL = "This is a small modal. It has very less content"
    TEXT_LARGE_MODAL = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. \
    Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took \
    a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into \
    electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of \
    Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."

    @allure.step("Click button small modal")
    def click_button_small_modal(self):
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_SMALL_MODAL)).click()

    @allure.step("Click button large modal")
    def click_button_large_modal(self):
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_LARGE_MODAL)).click()

    @allure.step("Checking a small modal dialogs")
    def check_small_modal(self):
        self.wait.until(EC.visibility_of_element_located(self.MODAL))
        message = self.wait.until(EC.visibility_of_element_located(self.MESSAGE_SMALL_MODAL)).text
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_CLOSE_SMALL)).click()
        assert message == self.TEXT_SMALL_MODAL, ErrorWindows.INVALID_MESSAGE_MODAL

    @allure.step("Checking a large modal dialogs")
    def check_large_modal(self):
        self.wait.until(EC.visibility_of_element_located(self.MODAL))
        massage = self.wait.until(EC.visibility_of_element_located(self.MESSAGE_LARGE_MODAL)).text
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_CLOSE_LARGE)).click()
        assert massage == self.TEXT_LARGE_MODAL, ErrorWindows.INVALID_MESSAGE_MODAL

    @allure.step("Click button close small")
    def click_button_close_small(self):
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_CLOSE_SMALL)).click()
        self.wait.until(EC.invisibility_of_element_located(self.MESSAGE_SMALL_MODAL))

    @allure.step("Click button close large")
    def click_button_close_large(self):
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_CLOSE_LARGE)).click()
        self.wait.until(EC.invisibility_of_element_located(self.MESSAGE_LARGE_MODAL))


