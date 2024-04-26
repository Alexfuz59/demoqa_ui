import os
import shutil
from selenium.webdriver.support.ui import WebDriverWait
import allure
from base.base_page import BasePage
from config.links import LinksElement
from enums.error_enums import ErrorElements
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image


class UploadDownload(BasePage):
    PAGE_URL = LinksElement.UPLOAD_DOWNLOAD
    UPLOAD = ('xpath', '//input[@type="file"]')
    DOWNLOAD = ('xpath', '//a[@id="downloadButton"]')
    UPLOAD_RESULT = ('xpath',  '//p[@id="uploadedFilePath"]')
    FILE_NAME = 'sampleFile.jpeg'

    def __init__(self, driver):
        super().__init__(driver)
        self.waitDonwload = WebDriverWait(driver, timeout=60, poll_frequency=1)

    @allure.step("Click button download")
    def click_button_download(self):
        self.wait.until(EC.element_to_be_clickable(self.DOWNLOAD)).click()

    @allure.step("Checking download")
    def check_download(self, tmpdir):
        self.waitDonwload\
            .until(lambda driver: any(self.FILE_NAME in f for f in os.listdir(str(tmpdir))))
        assert os.path.exists(os.path.join(tmpdir, self.FILE_NAME)), ErrorElements.ERROR_DOWNLOAD

    @allure.step("Checking format image")
    def check_format_file(self, tmpdir):
        if os.path.exists(os.path.join(tmpdir, self.FILE_NAME)):
            img = Image.open(os.path.join(tmpdir, self.FILE_NAME))
        else:
            raise FileNotFoundError("File not found at specified path")
        assert img.format == "JPEG", ErrorElements.INVALID_FILE_FORMAT(img.format)

    @allure.step("Upload file")
    def upload_file(self, tmpdir):
        self.wait.until(EC.visibility_of_element_located(self.UPLOAD))\
            .send_keys(os.path.join(tmpdir, self.FILE_NAME))

    @allure.step("Checking upload")
    def check_upload(self):
        result = self.wait.until(EC.visibility_of_element_located(self.UPLOAD_RESULT)).text
        assert self.FILE_NAME in result, ErrorElements.ERROR_UPLOAD

    @allure.step("Click button download")
    def save_image_directory(self, tmpdir):
        file_in_tmpdir = os.path.join(tmpdir, self.FILE_NAME)
        shutil.copy(file_in_tmpdir, os.getcwd())




