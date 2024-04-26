import allure
import requests
from base.base_page import BasePage
from config.links import LinksElement
from selenium.webdriver.support import expected_conditions as EC
from enums.error_enums import ErrorElements
from PIL import Image, UnidentifiedImageError
from io import BytesIO


class BrokenLinks(BasePage):
    PAGE_URL = LinksElement.BROKEN_LINKS
    VALID_IMAGE = ('xpath', '(//img[@src="/images/Toolsqa.jpg"])[2]')
    BROKEN_IMAGE = ('xpath', '//img[@src="/images/Toolsqa_1.jpg"]')
    VALID_LINK = ('xpath', '//a[text()="Click Here for Valid Link"]')
    BROKEN_LINK = ('xpath', '//a[text()="Click Here for Broken Link"]')

    @allure.step("Checking the valid image")
    def check_valid_image(self):
        imageSite = self.wait.until((EC.visibility_of_element_located(self.VALID_IMAGE)))
        src = imageSite.get_attribute("src")
        response = requests.get(src)
        if response.status_code == 200:
            image = Image.open(BytesIO(response.content))
            assert image.size[0] == 347 and image.size[1] == 100, ErrorElements.ERROR_IMAGE_SIZE
            assert imageSite.is_displayed(), ErrorElements.ERROR_IMAGE_NOT_DISPLAYED
        else:
            raise AssertionError(ErrorElements.ERROR_IMAGE)

    @allure.step("Checking the broken image")
    def check_broken_image(self):
        imageSite = self.wait.until((EC.visibility_of_element_located(self.BROKEN_IMAGE)))
        src = imageSite.get_attribute("src")
        response = requests.get(src)
        try:
            if response.status_code == 200:
                image = Image.open(BytesIO(response.content))
                assert imageSite.is_displayed(), ErrorElements.ERROR_IMAGE_NOT_DISPLAYED
                assert image.size[0] > 16 and image.size[1] > 16, ErrorElements.ERROR_IMAGE_SIZE
            else:
                raise AssertionError(ErrorElements.ERROR_IMAGE)
        except UnidentifiedImageError:
            raise AssertionError(ErrorElements.ERROR_FAVICON)

    @allure.step("Checking the valid link")
    def click_valid_link(self):
        self.wait.until(EC.element_to_be_clickable(self.VALID_LINK)).click()

    @allure.step("Checking the broken link")
    def click_broken_link(self):
        self.wait.until(EC.element_to_be_clickable(self.BROKEN_LINK)).click()
