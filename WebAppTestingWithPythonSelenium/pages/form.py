import allure

from WebAppTestingWithPythonSelenium.common.base import Base


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
    _form_page_field_message = "message"
    _get_captcha = "captcha_image"
    _form_page_field_captcha = "captcha"
    _post_button = "btnContactUs"

    @allure.step
    def click_form(self):
        self.click_on_element(locator_value=self._form_page_link_name, locator_type="link")

    @allure.step
    def verify_form_page(self):
        element = self.is_element_displayed(locator_value=self._form_page_id, locator_type="id")
        assert element == True

    @allure.step
    def enter_name(self):
        self.send_text(locator_value=self._form_page_field_name, locator_type="id", text="Kazi")

    @allure.step
    def enter_email(self):
        self.send_text(locator_type="id", locator_value=self._form_page_field_email, text="kazi@kazi.com")

    @allure.step
    def enter_technology(self):
        self.send_text(locator_type="id", locator_value=self._form_page_field_technology, text="Automation Development")

    @allure.step
    def enter_message(self):
        self.send_text(locator_type="id", locator_value=self._form_page_field_message, text="Hi there!")

    @allure.step
    def get_captcha(self):
        captcha = self.get_text(locator_type="id", locator_value=self._get_captcha)
        return captcha

    @allure.step
    def enter_captcha(self):
        self.send_text(text=self.get_captcha(), locator_value=self._form_page_field_captcha, locator_type="id")

    @allure.step
    def click_on_post_button(self):
        self.scroll(locator_value=self._post_button, locator_type="id")
        self.click_on_element(locator_value=self._post_button, locator_type="id")

    @allure.step
    def click_radio_button(self):
        self.click_on_element(locator_value=self._form_page_field_gender, locator_type="id")
