import WebAppTesting.utilities.customLogger as logger
from WebAppTesting.common.base import Base


class FormPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _form_page_link_name = "Form"
    _form_page_id = "reused_form"
    _form_page_field_name = "name"
    _form_page_field_email = "email"
    _form_page_field_gender = "g"
    _form_page_field_technology = "tech"
    _form_page_field_message = "messag"
    _get_captcha = "captcha_image"
    _form_page_field_captcha = "captcha"
    _post_button = "btnContactUs"

    def click_form(self):
        self.click_on_element(locator_value=self._form_page_link_name, locator_type="link")
        logger.allure_logs("Clicked on Form page")

    def verify_form_page(self):
        element = self.is_element_displayed(locator_value=self._form_page_id, locator_type="id")
        assert element == True
        logger.allure_logs("Verified Form page")

    def enter_name(self):
        self.send_text(locator_value=self._form_page_field_name, locator_type="id", text="Kazi")
        logger.allure_logs("Entered text in the name field")

    def enter_email(self):
        self.send_text(locator_type="id", locator_value=self._form_page_field_email, text="kazi@kazi.com")
        logger.allure_logs("Entered email in the email field")

    def enter_technology(self):
        self.send_text(locator_type="id", locator_value=self._form_page_field_technology, text="Automation Development")
        logger.allure_logs("Entered technology in the technology field")

    def enter_message(self):
        self.send_text(locator_type="id", locator_value=self._form_page_field_message, text="Hi there!")
        logger.allure_logs("Entered a message in the message field")

    def get_captcha(self):
        captcha = self.get_text(locator_type="id", locator_value=self._get_captcha)
        logger.allure_logs("Got Captcha")
        return captcha

    def enter_captcha(self):
        self.send_text(text=self.get_captcha(), locator_value=self._form_page_field_captcha, locator_type="id")
        logger.allure_logs("Entered Captcha in the Captcha field")

    def click_on_post_button(self):
        self.scroll(locator_value=self._post_button, locator_type="id")
        self.click_on_element(locator_value=self._post_button, locator_type="id")
        logger.allure_logs("Click on post button")

    def click_radio_button(self):
        self.click_on_element(locator_value=self._form_page_field_gender, locator_type="id")
        logger.allure_logs("Selected Gender from the radio buttons")
