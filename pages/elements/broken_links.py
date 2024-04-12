import allure
import requests
from base.base_page import BasePage
from config.links import LinksElement
from selenium.webdriver.support import expected_conditions as EC
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
            assert image.size[0] == 347 and image.size[1] == 100, 'Incorrect image size'
            assert imageSite.is_displayed(), 'Image not displayed on the page'
        else:
            raise AssertionError("Image Error")

    @allure.step("Checking the broken image")
    def check_broken_image(self):
        imageSite = self.wait.until((EC.visibility_of_element_located(self.BROKEN_IMAGE)))
        src = imageSite.get_attribute("src")
        response = requests.get(src)
        try:
            if response.status_code == 200:
                image = Image.open(BytesIO(response.content))
                assert imageSite.is_displayed(), 'Image not displayed on the page'
                assert image.size[0] > 16 and image.size[1] > 16, 'Incorrect image size'
            else:
                raise AssertionError("Image Error")
        except UnidentifiedImageError:
            raise AssertionError("Favicon, image failed to load")

    @allure.step("Checking the valid link")
    def click_valid_link(self):
        self.wait.until(EC.element_to_be_clickable(self.VALID_LINK)).click()

    @allure.step("Checking the broken link")
    def click_broken_link(self):
        self.wait.until(EC.element_to_be_clickable(self.BROKEN_LINK)).click()
