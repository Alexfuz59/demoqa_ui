import allure
from base.base_page import BasePage
from config.links import LinkWidgets
from selenium.webdriver.support import expected_conditions as EC
from enums.error_enums import ErrorWidgets


class Accordian(BasePage):
    PAGE_URL = LinkWidgets.ACCORDIAN
    SECTION1 = ('xpath', '//div[@id="section1Heading"]')
    SECTION2 = ('xpath', '//div[@id="section2Heading"]')
    SECTION3 = ('xpath', '//div[@id="section3Heading"]')
    MESSAGE_1 = ('xpath', '(//div/p)[1]')
    MESSAGE_2_1 = ('xpath', '(//div/p)[2]')
    MESSAGE_2_2 = ('xpath', '(//div/p)[3]')
    MESSAGE_3 = ('xpath', '(//div/p)[4]')

    TEXT_SECTION_1 = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. \
    Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer \
    took a galley of type and scrambled it to make a type specimen book. It has survived not only five \
    centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was \
    popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more \
    recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
    TEXT_SECTION_2_1 = 'Contrary to popular belief, Lorem Ipsum is not simply random text. \
    It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. \
    Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the \
    more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of \
    the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections \
    1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by \
    Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. \
    The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.'
    TEXT_SECTION_2_2 = 'The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for \
    those interested. Sections 1.10.32 and 1.10.33 from "de Finibus Bonorum et Malorum" by Cicero are \
    also reproduced in their exact original form, accompanied by English versions from the 1914 \
    translation by H. Rackham.'
    TEXT_SECTION_3 = "It is a long established fact that a reader will be distracted by the readable \
    content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a \
    more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making \
    it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum \
    as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. \
    Various versions have evolved over the years, sometimes by accident, sometimes on purpose \
    (injected humour and the like)."

    @allure.step("Click section 1")
    def click_section1(self):
        element = self.wait.until(EC.visibility_of_element_located(self.SECTION1))
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Click section 2")
    def click_section2(self):
        element = self.wait.until(EC.visibility_of_element_located(self.SECTION2))
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Click section 3")
    def click_section3(self):
        element = self.wait.until(EC.visibility_of_element_located(self.SECTION3))
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Checking accordian section 2")
    def check_accordian_section_2(self):
        self.click_section2()
        message1 = self.wait.until(EC.visibility_of_element_located(self.MESSAGE_2_1)).text
        message2 = self.wait.until(EC.visibility_of_element_located(self.MESSAGE_2_2)).text
        self.click_section1()
        self.wait.until(EC.invisibility_of_element_located(self.MESSAGE_2_1))
        assert message1 == self.TEXT_SECTION_2_1, ErrorWidgets.ERROR_SECTION_OPENED
        assert message2 == self.TEXT_SECTION_2_2, ErrorWidgets.ERROR_SECTION_OPENED

    @allure.step("Checking accordian section 3")
    def check_accordian_section_3(self):
        self.click_section3()
        message = self.wait.until(EC.visibility_of_element_located(self.MESSAGE_3)).text
        self.click_section2()
        self.wait.until(EC.invisibility_of_element_located(self.MESSAGE_3))
        assert message == self.TEXT_SECTION_3, ErrorWidgets.ERROR_SECTION_OPENED

    @allure.step("Checking accordian section 1")
    def check_accordian_section_1(self):
        self.click_section1()
        message = self.wait.until(EC.visibility_of_element_located(self.MESSAGE_1)).text
        self.click_section3()
        self.wait.until(EC.invisibility_of_element_located(self.MESSAGE_1))
        assert message == self.TEXT_SECTION_1, ErrorWidgets.ERROR_SECTION_OPENED







